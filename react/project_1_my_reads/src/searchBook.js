import React, { Component } from 'react';
import { Link } from 'react-router-dom'

class SearchBook extends Component {
  state = {
    books_query: '',
  }

  updateQuery = (query) => {
    this.setState(() => ({
      books_query: query.trim()
    }))
    if (this.props.onSearchBooks)
      this.props.onSearchBooks(query)
  }

  deleteSearch = () => {
    this.setState(() => ({
      books_query: ''
    }))
  }



  render () {
    const {books_filtered, onMoveBook, getAuthors} = this.props

    return (
      <div>
        <div className="search-books">
          <div className="search-books-bar">
          <Link
            className='close-search'
            to='/'
            onClick={this.deleteSearch}
          >
            <button className="close-search">Close</button>
          </Link>
            <div className="search-books-input-wrapper">
              <input
                type="text"
                placeholder="Search by title or author"
                onChange={(event) => this.updateQuery(event.target.value)}
              />
            </div>
          </div>
          <div className="search-books-results">
            <ol className="books-grid">

              {Array.isArray(books_filtered) && (books_filtered.map((one_book) => (
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
              )))}

              {typeof(books_filtered) === 'object' && 'items' in books_filtered && books_filtered.items.length === 0 && (
                <li>
                  No books found.
                </li>
              )}
            </ol>
          </div>
        </div>
      </div>
    )
  }
}

export default SearchBook
