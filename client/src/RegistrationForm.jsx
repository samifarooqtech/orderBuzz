import React, { useState } from "react";
import axios from "axios";  // for making API requests
import './styles.css'; // Import styles.css
import { Link, Navigate } from "react-router-dom"; // Import Link and Navigate

function RegistrationForm() {
  const [usernameReg, setUsernameReg] = useState("");
  const [passwordReg, setPasswordReg] = useState("");
  const [firstNameReg, setFirstNameReg] = useState("");
  const [lastNameReg, setLastNameReg] = useState("");
  const [emailReg, setEmailReg] = useState("");
  const [phoneReg, setPhoneReg] = useState("");
  const [errorMessageReg, setErrorMessageReg] = useState("");
  const [successMessageReg, setSuccessMessageReg] = useState("");
  const [isRegistered, setIsRegistered] = useState(false); // State to track registration status



  const handleRegistrationSubmit = async (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    const userData = {
        firstName: firstNameReg,
        lastName: lastNameReg,
        email: emailReg,
        phone: phoneReg,
        username: usernameReg,
        password: passwordReg,
      };
    try {
      const response = await axios.post("http://localhost:5000/create-user", {
        firstName: firstNameReg,
        lastName: lastNameReg,
        email: emailReg,
        phone: phoneReg,
        username: usernameReg,
        password: passwordReg,
      });

      if (response.status === 201) {
        setSuccessMessageReg("User created successfully!..");
        setFirstNameReg("");
        setLastNameReg("");
        setEmailReg("");
        setPhoneReg("");
        setUsernameReg("");
        setPasswordReg("");
        setIsRegistered(true); // Set registration status to true
        setErrorMessageReg("")
      } else {
        setErrorMessageReg("An error occurred. Please try again.");
      }
    } catch (error) {
      console.error(error);
      setErrorMessageReg("An error occurred. Please try again.");
    }
  };

  return (
    <div className="registration-form">
      <h3>Registration</h3>
      {errorMessageReg && <p className="error">{errorMessageReg}</p>}
      {successMessageReg && <p className="success">{successMessageReg}</p>}
      <form onSubmit={handleRegistrationSubmit}>
        <div>
          <label htmlFor="username-reg">Username:</label>
          <input
            type="text"
            id="username-reg"
            value={usernameReg}
            onChange={(e) => setUsernameReg(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password-reg">Password:</label>
          <input
            type="password"
            id="password-reg"
            value={passwordReg}
            onChange={(e) => setPasswordReg(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="first-name">First Name:</label>
          <input
            type="text"
            id="first-name"
            value={firstNameReg}
            onChange={(e) => setFirstNameReg(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="last-name">Last Name:</label>
          <input
            type="text"
            id="last-name"
            value={lastNameReg}
            onChange={(e) => setLastNameReg(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={emailReg}
            onChange={(e) => setEmailReg(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="phone">Phone:</label>
          <input
            type="tel"
            id="phone"
            value={phoneReg}
            onChange={(e) => setPhoneReg(e.target.value)}
            pattern="[0-9()-]+" // Optional: basic phone number pattern
            required
          />
        </div>
        <button type="submit">Register</button>
      </form>
       {/* Link to login page */}
       <p>Already have an account? <Link to="/login">Login here</Link></p>
    </div>
  );
}

export default RegistrationForm;
