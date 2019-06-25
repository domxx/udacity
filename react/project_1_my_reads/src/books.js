import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import Shelf from './shelf'


class Books extends Component {
  render(){
    const {myBooks, onMoveBook, getAuthors} = this.props

    return (
      <div className="list-books">
        <div className="list-books-title">
          <h1>MyReads</h1>
        </div>
        <div className="list-books-content">
          <div>
            <Shelf
              myBooks={myBooks}
              getAuthors={getAuthors}
              shelf='currentlyReading'
              onMoveBook={onMoveBook}
            />
            <Shelf
              myBooks={myBooks}
              getAuthors={getAuthors}
              shelf='wantToRead'
              onMoveBook={onMoveBook}
            />
            <Shelf
              myBooks={myBooks}
              getAuthors={getAuthors}
              shelf='read'
              onMoveBook={onMoveBook}
            />
          </div>
        </div>
        <div className="open-search">
          <Link
            to='/search'
            className = 'add-book'>
            <button>Add a book</button>
          </Link>
        </div>
      </div>
    )}
}

export default Books
