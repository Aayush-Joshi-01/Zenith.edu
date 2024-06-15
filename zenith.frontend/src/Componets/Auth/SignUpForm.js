import axios from "axios";
import React, { useState } from "react";
import { toast } from "react-toastify";

const SignUpForm = ({ handleToggle }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [userData, setUserData] = useState({
    FirstName: "",
    LastName: "",
    Username: "",
    Email: "",
    Password: "",
  });
  const [validationErrors, setValidationErrors] = useState({
    FirstName: false,
    LastName: false,
    Username: false,
    Email: false,
    Password: false,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUserData({ ...userData, [name]: value });
    validateInput(name, value);
  };

  const validateInput = (name, value) => {
    let isValid = true;

    if (name === "Email") {
      isValid = isValidEmail(value);
    } else if (name === "Username" || name === "Password") {
      isValid = value.length >= 6;
    }

    setValidationErrors({ ...validationErrors, [name]: !isValid });
  };

  const handleClick = async () => {
    setIsLoading(true);

    // Basic validations
    if (
      userData.Email === "" ||
      userData.Password === "" ||
      userData.Username === "" ||
      validationErrors.Username ||
      validationErrors.Email ||
      validationErrors.Password
    ) {
      setIsLoading(false);
      return toast.error("Please fill all fields correctly.");
    }

    try {
      const res = await axios.post("http://localhost:3001/auth/register", userData);

      if (res.data.success) {
        setIsLoading(false);
        toast.success(res.data.message);
        handleToggle();
        setUserData({
          FirstName: "",
          LastName: "",
          Username: "",
          Email: "",
          Password: "",
        });
        setValidationErrors({
          FirstName: false,
          LastName: false,
          Username: false,
          Email: false,
          Password: false,
        });
      } else {
        setIsLoading(false);
        toast.info(res.data.message);
      }
    } catch (err) {
      setIsLoading(false);
      toast.error("Error signing up. Please try again.");
    }
  };

  const isValidEmail = (email) => {
    // Simple email validation regex
    return /\S+@\S+\.\S+/.test(email);
  };

  const getInputClassName = (name) => {
    return validationErrors[name] ? "Login-input error" : "Login-input";
  };

  return (
    <>
      <form>
        {isLoading ? (
          <div className="spinner"></div>
        ) : (
          <>
            <input
              type="text"
              placeholder="First Name"
              autoComplete="off"
              name="FirstName"
              value={userData.FirstName}
              onChange={handleChange}
              className={getInputClassName("FirstName")}
              required
            />
            <input
              type="text"
              placeholder="Last Name"
              autoComplete="off"
              name="LastName"
              value={userData.LastName}
              onChange={handleChange}
              className={getInputClassName("LastName")}
            />
            <input
              type="text"
              placeholder="Username (min 6 characters)"
              className={getInputClassName("Username")}
              autoComplete="off"
              name="Username"
              value={userData.Username}
              onChange={handleChange}
              required
              minLength="6"
            />
            <input
              type="email"
              className={getInputClassName("Email")}
              placeholder="Enter valid Email"
              autoComplete="off"
              name="Email"
              value={userData.Email}
              onChange={handleChange}
              required
            />
            <input
              type="password"
              placeholder="Password (min 6 characters)"
              className={getInputClassName("Password")}
              autoComplete="off"
              name="Password"
              value={userData.Password}
              onChange={handleChange}
              required
              minLength="6"
            />
            <button
              type="button"
              className="Login-btn bg-color-purple-700"
              onClick={handleClick}
            >
              Sign Up
            </button>
          </>
        )}
      </form>
    </>
  );
};

export default SignUpForm;
