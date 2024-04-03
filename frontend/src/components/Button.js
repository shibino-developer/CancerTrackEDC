// src/components/Button.js

// code defines a React functional component named Button, 
// which represents a reusable button component that can be used throughout the application

import React from 'react'; //imports the React module from the 'react' package

function Button({ onClick, children, className }) { //This is a functional component named Button.
  //  It takes three props as arguments: onClick, children, and className. 
  // These props allow customization and functionality of the button component.
  return (         //Component return, 
    <button className={`button ${className}`} onClick={onClick}>
      {children}
    </button>
  );
}

// returns a <button> element with the following attributes:
//      className: This is a string interpolation that combines the button class with any additional classes 
                        // passed via the className prop. This allows for easy styling of the button.
        // onClick: This is a reference to the onClick prop, which specifies the function to be called 
            //           when the button is clicked.
// The content of the button ({children}) is dynamic and determined by whatever is nested 
// within the <Button> tags when the component is used. 
// This allows for flexibility in the text or elements displayed within the button.

export default Button;     //exports the Button component as the default export from this module.

