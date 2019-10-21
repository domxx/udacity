import React, {Fragment} from 'react'
import {Redirect, Route} from 'react-router-dom'
import {connect} from 'react-redux'
import {Container, Row} from 'reactstrap'
import Nav from './Nav'

const PrivateRoute = ({component: Component, isAuthenticated, ...rest}) => (
  <Route {...rest} render={(props) => {
    return (
      isAuthenticated
      ?
      <Fragment>
        <Nav/>
        <Container>
          <Row>
            <Component {...props}/>
          </Row>
        </Container>
      </Fragment>
      : <Redirect to={{
        pathname: '/login',
        state: {from: props.location}
      }}/>
    )
  }}/>
)

function mapStateToProps({authedUser}) {
  let auth = false
  for (let key in authedUser) {
    if (authedUser.hasOwnProperty(key))
      auth = true
      break
  }
  return {isAuthenticated: auth}
}

export default connect(mapStateToProps, null, null, {pure: false,})(PrivateRoute)
