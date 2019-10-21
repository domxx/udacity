export const ADD_QUESTION = "ADD_QUESTION"
export const RECEIVE_QUESTIONS = "RECEIVE_QUESTIONS"

export default function questions(state = {}, action) {
  switch (action.type) {
    case RECEIVE_QUESTIONS:
      return {
        ...state,
        ...action.questions
      }
    case ADD_QUESTION:
      let {question} = action
      return {
        ...state,
        [question.id]: question
      }
    default:
      return state
  }
}
