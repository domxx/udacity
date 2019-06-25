import React, { Component } from 'react'


class Shelf extends Component {

  render(){
    const {myBooks, shelf, onMoveBook, getAuthors} = this.props
    return (
      <div className="bookshelf">
        <h2 className="bookshelf-title">{shelf}</h2>
        <div className="bookshelf-books">
        <ol className="books-grid">
          {myBooks.map((one_book) => (
            one_book.shelf === shelf && (
            <li key={one_book.id} className='list-books-content'>
              <div className="book">
                <div className="book-top">
                  <div className="book-cover" style={{ width: 128, height: 188, backgroundImage: `url(${"imageLinks" in one_book && one_book.imageLinks.smallThumbnail})` }}></div>
                  <div className="book-shelf-changer">
                    <select onChange={(event) => onMoveBook(one_book, event.target.value)} defaultValue={one_book.shelf}>
                      <option value="move" disabled>Move to...</option>
                      <option value="currentlyReading">Currently Reading</option>
                      <option value="wantToRead">Want to Read</option>
                      <option value="read">Read</option>
                      <option value="none">None</option>
                    </select>
                  </div>
                </div>
                <div className="book-title">{one_book.title}</div>
                <div className="book-authors">{getAuthors(one_book.authors)}</div>
              </div>
            </li>
          )
          ))}
          </ol>
        </div>
      </div>
    )}
}

export default Shelf
