export const AUTHENTICATE_USER = "AUTHENTICATE_USER"
export const SIGN_OUT = "SIGN_OUT"

export default function authedUser(state = {}, action) {
  switch (action.type) {
    case AUTHENTICATE_USER:
      return action.id
    case SIGN_OUT:
      return {}
    default:
      return state
  }
}
