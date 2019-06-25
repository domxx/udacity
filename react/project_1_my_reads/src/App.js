import React from 'react'
import * as BooksAPI from './BooksAPI'
import './App.css'
import { Route } from 'react-router-dom'
import SearchBook from './searchBook'
import Books from './books'

class BooksApp extends React.Component {
  state = {
    books_query: '',
    my_books: []
  }

  componentDidMount() {
    BooksAPI.getAll().then((my_books) => {
      this.setState(() => ({
        my_books: my_books
      }))
    })
  }

  searchBook = (book) => {
    if (book === ''){
      this.setState(() => ({
        books_filtered: []
      }))
    }
    else {
      BooksAPI.search(book).then((new_books) => {
        let filtered_books = new_books

        if ('error' in filtered_books){
          this.setState(() => ({
            books_filtered: filtered_books
          }))
        }
        else {

          for (let filtered_book of filtered_books){
            for (let my_book of this.state.my_books){
              if (filtered_book.id === my_book.id){
                filtered_book.shelf = my_book.shelf
              }
            }
            if (typeof(filtered_book.shelf) === 'undefined'){
              filtered_book.shelf = "none"
            }
          }
          this.setState(() => ({
            books_filtered: filtered_books
          }))
        }
      })
    }
  }

  moveBook = (book, shelf) => {
    BooksAPI.update(book, shelf).then((resp) => {
      this.setState((currentState) =>{
        let new_state = currentState
        if (   (!this.state.my_books.includes(book)   )    &&    (shelf !== 'none')   )
          new_state.my_books.push(book)

        for (let my_book of new_state.my_books){
          if (my_book.id === book.id)
            my_book.shelf = shelf
        }
        return new_state
      })

    })
}

  myBooks = () => {
    BooksAPI.getAll().then((my_books) => {
      this.setState(() => ({
        my_books: my_books
      }))
    })
  }

  format_authors = (authors) => {
    if (typeof(authors) === 'undefined')
      return 'Unkown Author'
    return authors.join(', ')
  }

  render() {
    return (
      <div>
      <Route exact path='/' render = {() => (
          <Books
            myBooks={this.state.my_books}
            onMoveBook={this.moveBook}
            getAuthors={this.format_authors}
          />
        )}/>
        <Route path='/search' render = {({history}) => (
          <SearchBook
            books_filtered={this.state.books_filtered}
            onSearchBooks={(book) => {
              this.searchBook(book)
            }}
            onMoveBook={this.moveBook}
            getAuthors={this.format_authors}
            myBooks={this.state.my_books}
          />
        )}/>
      </div>
    );
  }
}

export default BooksApp
