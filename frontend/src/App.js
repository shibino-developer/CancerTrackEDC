// Simple React component written in JavaScript
// imports an SVG file named logo.svg. 
// This file is assumed to be located in the same directory as the current JavaScript file (App.js). 
// The imported logo variable holds the URL or path to this SVG file.

import logo from './logo.svg';
// imports a CSS file named App.css located in the same directory as the current JavaScript file.
import './App.css';
// This is a functional component named App. In React, components are building blocks for UI elements. 
// Functional components are defined using JavaScript functions.
function App() {
  // Component return, The return statement returns JSX (JavaScript XML), 
  // which represents the structure of the component's UI.
  // It returns a <div> element with the class name App, which corresponds to the CSS class defined in App.css.
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
// Inside the <div className="App">, there's a <header> element with the class name App-header.
// Inside the header, there's an <img> element with the src attribute set to the logo variable, which holds 
// the path to the logo SVG file imported earlier. It also has a class name App-logo.
// There's a <p> element containing a message about editing the src/App.js file.
// Finally, there's an <a> element with the class name App-link, which links to the React documentation.
export default App;
