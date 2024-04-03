// src/components/App.js
// This code is another React component named App, but it's more structured compared to the previous example. 
// imports the React module from the 'react' package. 
// React is necessary for defining React components and using JSX.

// The other import statements import three custom components: Header, Footer, and MainContent. 
// These components are assumed to be located in separate files (Header.js, Footer.js, and MainContent.js) 
// within a components directory relative to the current file (App.js).

import React from 'react';
import Header from './Header';
import Footer from './Footer';
import MainContent from './MainContent';
// This is a functional component named App
function App() {
  return (                                 //Component return, The return statement returns JSX representing 
                                            // the structure of the component's UI. components (Header, 
                                            // MainContent, and Footer) are JSX tags
    <div className="app">
      <Header />
      <MainContent />
      <Footer />
    </div>
  );
}

export default App;                        //  exports the App component as the default export from this module,
