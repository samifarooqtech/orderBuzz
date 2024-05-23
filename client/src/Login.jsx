import React, { useState } from "react";
import axios from "axios"; // for making API requests
import './styles.css'; // Import styles.css
import { useNavigate,Link } from "react-router-dom";
//import { useHistory } from "react-router-dom"; // Import useHistory
import { Navigate } from "react-router-dom"; 
function Login({ setUsername }) {
  const navigate = useNavigate(); // Hook for navigation
  const [usernameLogin, setUsernameLogin] = useState("");
  const [passwordLogin, setPasswordLogin] = useState("");
  const [errorMessageLogin, setErrorMessageLogin] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false); // Flag for login status



  const handleLoginSubmit = async (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    try {
      const response = await axios.post("http://localhost:5000/login", {
        username: usernameLogin,
        password: passwordLogin,
      });
      alert('Status:'+ response.status)
      if (response.status === 200) {
        // Handle successful login (e.g., redirect to protected area)
        console.log("Login successful!");
        setUsernameLogin(response.data.username);
        setUsername(response.data.username);
        setIsLoggedIn(true); // Set login status to true
        //history.push("/welcome");
        //navigate("/dashboard"); // Navigate to the dashboard route
        console.log('Login successful! Redirected to dashboard');
        // Replace with your logic for handling successful login (e.g., redirect)
      } else {
        setErrorMessageLogin(
          "Invalid username or password. Please try again."
        );
      }
    } catch (error) {
      console.error(error);
      if (error.response && error.response.status === 401) {
        // Handle 401 Unauthorized error
        console.log("Unauthorized. Please log in.");
        setErrorMessageLogin("Invalid Username or Password. Please try again.");
      } else {
        console.error("An error occurred:", error.message);
        setErrorMessageLogin("An error occurred. Please try again" );
      }
      
    }
  };
 // Redirect to welcome page if logged in
 if (isLoggedIn) {
  return <Navigate to="/welcome" />;
}
  return (
    <div className="login-form">
      <h3>Login</h3>
      {errorMessageLogin && <p className="error">{errorMessageLogin}</p>}
      <form onSubmit={handleLoginSubmit}>
        <div>
          <label htmlFor="username-login">Username:</label>
          <input
            type="text"
            id="username-login"
            value={usernameLogin}
            onChange={(e) => setUsernameLogin(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password-login">Password:</label>
          <input
            type="password"
            id="password-login"
            value={passwordLogin}
            onChange={(e) => setPasswordLogin(e.target.value)}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
      {/* Link to RegistrationForm */}
      <p>New user? <Link to="/register">Register here</Link></p>
    </div>
  );
}

export default Login;
