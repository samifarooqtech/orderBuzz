import React from "react";
import RegistrationForm from "../RegistrationForm"; // Assuming RegistrationForm.jsx is in the same directory
import Login from "../Login"; // Assuming Login.jsx is in the same directory

function App() {
  return (
    <div className="App">
      <h2>Welcome</h2>
      <RegistrationForm /> {/* Render the RegistrationForm component */}
      <Login /> {/* Render the Login component */}
    </div>
  );
}

export default App;
