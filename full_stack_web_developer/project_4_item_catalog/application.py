from flask import Flask, render_template, request, redirect, \
    url_for, jsonify, flash, session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from database import Car, Model

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

import random
import string

CLIENT_ID = json.loads(
    open('cars_secret.json', 'r').read()
)['web']['client_id']

engine = create_engine('sqlite:///cars.db', echo=True)
app = Flask(__name__)

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/delete_all_items')
def cleanup():
    # function to clean up the database
    meta = Model.metadata
    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
        session.commit()

    meta = Car.metadata
    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
        session.commit()
    return "Deleted"


@app.route('/')
@app.route('/cars')
def cars():
    # Homepage of the app. Lists all cars and their models.
    cars = session.query(Car)
    models = session.query(Model)
    try:
        login_session['access_token']
        logged_in = True
    except KeyError:
        logged_in = False
    return render_template(
        'cars.html',
        cars=cars,
        models=models,
        logged_in=logged_in
    )


@app.route('/cars/new', methods=['GET', 'POST'])
def create_car():
    # Function for creating a new Car item.
    if request.method == 'POST':
        newItem = Car(name=request.form['name'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('cars'))
    else:
        return render_template('new_car.html')


@app.route('/models/<int:car_id>/new', methods=['GET', 'POST'])
def create_model(car_id):
    # Function for creating a car model.
    try:
        login_session['access_token']
        logged_in = True
    except KeyError:
        logged_in = False
    if logged_in:
        if request.method == 'POST':
            newItem = Model(
                name=request.form['name'],
                car_id=car_id,
                username=login_session['username']
            )
            session.add(newItem)
            session.commit()
            return redirect(url_for('cars'))
        else:
            return render_template('new_model.html', car_id=car_id)
    else:
        return "You have no rights to create models."


@app.route('/delete_model/<int:model_id>')
def delete_model(model_id):
    # Function for deleting a car model.
    try:
        login_session['access_token']
        logged_in = True
    except KeyError:
        logged_in = False

    itemToDelete = session.query(Model).filter_by(id=model_id).one()
    authorized = True if itemToDelete.username == login_session['username'] \
        else False

    if logged_in and authorized:
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('cars'))
    else:
        return "You have no rights to delete this model."


@app.route('/edit_model/<int:model_id>', methods=['GET', 'POST'])
def edit_model(model_id):
    # Function for editing a car model.
    try:
        login_session['access_token']
        logged_in = True
    except KeyError:
        logged_in = False

    itemToEdit = session.query(Model).filter_by(id=model_id).one()
    authorized = True if itemToEdit.username == login_session['username'] \
        else False

    if logged_in and authorized:
        if request.method == 'POST':
            itemToEdit.name = request.form['name']
            session.commit()
            return redirect(url_for('cars'))
        else:
            return render_template('edit_model.html', model_id=model_id)
    else:
        return "You have no rights to edit models."


@app.route('/cars/<int:car_id>/json')
def cars_json_id(car_id):
    # Endpoint returning a json data for a specific car.
    car = session.query(Car).filter_by(id=car_id).one()
    return jsonify(car.serialize)


@app.route('/cars/json')
def cars_json_all():
    # Endpoint returning json data for all cars and their models.
    cars = session.query(Car).options(joinedload(Car.model)).all()
    return jsonify(
        [(
            car.serialize, [model.serialize for model in car.model]
        ) for car in cars]
    )


@app.route('/login')
def login():
    # Function used for generating random state and handling logging page.
    state = ''.join(
        random.choice(
            string.ascii_uppercase + string.digits
        ) for x in xrange(32)
    )
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Function used for handling google sign in and logging in.
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('cars_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'),
            200
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '  # noqa
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/gdisconnect')
def gdisconnect():
    # Function used for loging out a user and deleting all his session data.
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(
            json.dumps('Current user not connected.'),
            401
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(
            json.dumps('Successfully disconnected.'),
            200
        )
        response.headers['Content-Type'] = 'application/json'

        return redirect(url_for('cars'))
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400)
        )
        response.headers['Content-Type'] = 'application/json'


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'fnhwh3(#$&h37tf9qfo23@'
    app.run(host='0.0.0.0', port=5000)
