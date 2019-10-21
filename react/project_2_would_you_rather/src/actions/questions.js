import {hideLoading, showLoading} from 'react-redux-loading'
import {saveQuestion, saveQuestionAnswer} from "../utils/api"
import {handleInitialData} from "./shared"

export const ADD_QUESTION = "ADD_QUESTION"
export const RECEIVE_QUESTIONS = "RECEIVE_QUESTIONS"

export function receiveQuestions(questions) {
  return {
    type: RECEIVE_QUESTIONS,
    questions
  }
}

export function addQuestion(question) {
  return {
    type: ADD_QUESTION,
    question
  }
}

export function handleAddQuestion(optionOneText, optionTwoText) {
  return (dispatch, getState) => {
    const {authedUser} = getState()
    dispatch(showLoading())
    return saveQuestion({
      optionOneText,
      optionTwoText,
      author: authedUser
    })
    .then(() => {
      dispatch(handleInitialData())
      dispatch(hideLoading())
    })
  }
}

export function handleAnswerQuestion(qid, answer) {
  return (dispatch, getState) => {
    const {authedUser} = getState()
    dispatch(showLoading())
    return saveQuestionAnswer(authedUser, qid, answer)
      .then(() => {
        dispatch(handleInitialData())
        dispatch(hideLoading())
      })
  }
}
