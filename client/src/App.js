//import React from "react";
import React, { useState } from "react";
import RegistrationForm from "./RegistrationForm"; // Assuming RegistrationForm.jsx is in the same directory
import Login from "./Login"; // Assuming Login.jsx is in the same directory
import WelcomePage from "./WelcomePage"; // Import the new Dashboard component
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  Navigate,
} from "react-router-dom";
import "./styles.css"; // Import styles.css

function App() {
  //const [isLoggedIn, setIsLoggedIn] = useState(false); // Optional: Initial login state (default to false)
  const [username, setUsername] = useState("");

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/login" element={<Login setUsername={setUsername} />} />
          <Route path="/register" element={<RegistrationForm />} />
          <Route
            path="/welcome"
            element={<WelcomePage username={username} />}
          />
          <Route
            path="/dashboard"
            element={<WelcomePage username={username} />}
          />
          <Route path="/" element={<Navigate to="/login" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
