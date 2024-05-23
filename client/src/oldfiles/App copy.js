import React, { useState } from "react";
import axios from "axios";

const Login = () => {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });
  //const [errorMessage, setErrorMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [username, setUsername] = useState("");
  const handleChange = (event) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post(
        "http://localhost:5000/login",
        formData,
        {
          method: "post", // Specify POST method
        }
      );
      const responseData = response.data;

      if (response.status >= 400) {
        const em = responseData.data.message;
        alert("test");
        setErrorMessage(em); // Log state update
        console.log("errorMessage:", em);
      } else {
        // Handle successful login
        console.log("Success:", formData);
        setUsername(responseData.message);
        setErrorMessage(""); // Log state update
      }
      console.log("Login data sent:", formData);
      console.log("Login response:", response.data);
      // Handle successful login (redirect, etc.)
    } catch (error) {
      alert("test");
      setErrorMessage("Error, Failed"); // Log state update
      console.log("errorMessage:", "test");
      // ... handle errors
    }
  };

  return (
    <div className="login-container">
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          name="username"
          value={formData.username}
          onChange={handleChange}
          required
        />
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <>
          {errorMessage && <p className="error-message">{errorMessage}</p>}
          <p> {username} </p>
        </>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;
