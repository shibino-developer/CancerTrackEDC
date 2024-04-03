// src/components/MainContent.js
//code defines a React component named MainContent responsible for 
// rendering the main content section of the application.
import React from 'react'; //imports the React module from the 'react' package
import Button from './Button'; //imports the Button component from the './Button' file, 
// allowing us to use the Button component within the MainContent component.

function MainContent() {   //React functional component,  represents the main content section of the application.
  return (   //Component return, returns a <div> element with the class name main-content. 
  // Inside this <div>, there's an <h2> element containing the text "Welcome to My App".
  // Additionally, it includes a <Button> component with the text "Click Me" as its content. 
  // This demonstrates the usage of the Button component within the MainContent component
    <div className="main-content"> 
      <h2>Welcome to My App</h2>
      <Button>Click Me</Button>
    </div>
  );
}

export default MainContent;  //exports the MainContent component as the default export from this module
