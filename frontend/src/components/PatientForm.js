// src/components/PatientForm.js
//React component named PatientForm, which represents a form for collecting patient information.
import React, { useState } from 'react'; //imports the React module from the 'react' package
import axios from 'axios'; //imports the axios library, which is used to make HTTP requests. 
// This will be used to send form data to a backend API.

function PatientForm() {  //functional component 'PatientForm' represents a form for collecting patient information.
  // State variables to store form data
  // uses the useState hook to initialize a state variable named formData, which holds the data entered by the user 
  // in the form fields (firstName, lastName, and age).

  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    age: '',
    // Add more fields as needed
    //Each property in formData corresponds to an input field in the form.
  });

  // Function to handle form input changes
  // This function is called whenever there's a change in any of the form input fields. 

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({                       // It updates the formData state with the new values entered by the user.
      ...formData,
      [name]: value,
    });
  };

  // Function to handle form submission
  // called when the form is submitted.
  const handleSubmit = async (e) => {
    e.preventDefault(); //prevents the default form submission behavior.
    try {
      // Make a POST request to your Django backend API endpoint
      const response = await axios.post('http://localhost:8000/patients/', formData);
      console.log('Form submitted successfully:', response.data); // logs the response data if successful.
      // Optionally, you can redirect the user or show a success message here
    } catch (error) {
      console.error('Error submitting form:', error); // Error handling is also implemented to log any errors that occur 
      // during the submission process.
      // Optionally, you can show an error message to the user here
    }
  };
 
  return (     //Inside the return statement, a <form> element is defined with 
  // an onSubmit event handler set to handleSubmit.
  // Input fields for collecting the patient's first name, last name, and age are defined using <input> elements. 
  // Each input field is associated with a corresponding property in the formData state, 
  // and their values are updated via the handleInputChange function.
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          id="firstName"
          name="firstName"
          value={formData.firstName}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label htmlFor="lastName">Last Name:</label>
        <input
          type="text"
          id="lastName"
          name="lastName"
          value={formData.lastName}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label htmlFor="age">Age:</label>
        <input
          type="number"
          id="age"
          name="age"
          value={formData.age}
          onChange={handleInputChange}
        />
      </div>
      {/* Add more form fields here */}
      {/* A submit button is provided to allow users to submit the form data. */}
      <button type="submit">Submit</button>
    </form>
  );
}

export default PatientForm;
