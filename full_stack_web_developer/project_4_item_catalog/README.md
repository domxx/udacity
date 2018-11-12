# Car Catalog
This application lists cars and their models. After logging in using Google Signin user can create, edit or delete models. Cars, however, can be created by anyone (even users not logged in).

This app repository consist of
  - ``templates`` folder containing all html templates
  - ``cars`` file containinf database models and data
  - ``cars_secret`` file containing information needed for google login
  - ``application`` file containing all backend logic
  - ``readme`` file

### App requirements
1. - if using windows - download and install Git Bash from [here](https://gitforwindows.org/) 
    - if using linux - just use linux terminal
2. download and install VirtualBox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
3. download and install Vagrant from [here](https://www.vagrantup.com/downloads.html)

### How to start the app
1. go to ``vagrant`` folder
2. execute following commands in git bash / linux terminal
```sh
$ vagrant up
```
```sh
$ vagrant ssh
```
3. move to ``catalog`` directory
```sh
$ cd /vagrant/catalog
```
4. excute following command
```sh
$ python application.py
```

Now your app should be up and running. You can visit the homepage of the app.
``http://localhost:5000/cars``

### JSON Endpoints
This app provides JSON endpoint with the coresponding datas.
- ``http://localhost:5000/cars/json`` lists all cars with their models
- ``http://localhost:5000/cars/<car_id>/json`` lists a car with coresponding id and its models
