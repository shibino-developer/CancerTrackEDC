// src/components/Header.js
// This code defines a React component named Header 
// responsible for rendering the header section of the application. 
// imports the React module from the 'react' package, which is necessary for defining 
// React components and using JSX.
import React from 'react';

function Header() {           // React functional component
// It returns a <header> element with the class name header. Inside the header, there's an <h1> element 
// containing the text "My App".
//This component provides a basic structure for the header section of the application. You can customize it by 
// adding navigation links, logos, or any other elements as needed.

  return (                      // Component return
    <header className="header">
      <h1>My App</h1>
      {/* Add navigation links or other elements here */}
    </header>
  );
}

export default Header;  //exports the Header component as the default export
