# My Reads

### Description
This project is your personal book library. You can search for books and add them to one of your three shelves.

The homepage is your library - you have the option to move your books between the different shelves (currently reading, want to read, read), or discard them.

The search page is a (let's say) shop - you can look up different books and buy them - add them to one of your shelves.

### Technical description
Front end functionality is done using React.
Backend is handled by utilizing a udacity API endpoints for searching, updating and getting books.
Books are stored in a udacity database.
Application was developd by cloning [`this repository`](https://github.com/udacity/reactnd-project-myreads-starter) and all of the code was added / changed in the _src_ folder.

### How to start the application
1. navigate to the folder with the application
2. install required packages
```sh
$ npm install
```

3. run following command and the browser will open
```sh
$ npm start
```

### Important
The backend API uses a fixed set of cached search results and is limited to a particular set of search terms, which can be found in [SEARCH_TERMS.md](SEARCH_TERMS.md). That list of terms are the _only_ terms that will work with the backend, so don't be surprised if your searches for Basket Weaving or Bubble Wrap don't come back with any results.

### Create React App

This project was bootstrapped with [Create React App](https://github.com/facebookincubator/create-react-app). You can find more information on how to perform common tasks [here](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md).
