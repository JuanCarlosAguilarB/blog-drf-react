import React, { useState } from "react";
import "./login.css";
import { Link } from "react-router-dom";
import loginimg from "assets/login.jpg";
import { login, logout } from "features/counter/userSlice";
import { useDispatch } from "react-redux";



const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();

    dispatch(
      login({
        email: email,
        password: password,
        loggedIn: true,
      })
    );

    setEmail("");
    setPassword("");
  };

  return (
    <div className="login">
      <div>
        <img src={loginimg} />
      </div>

      <div className="main-container">
        <p>Welcome!</p>


        <form className="login__form" onSubmit={(e) => handleSubmit(e)}>
          <input className="input-login"
            type="email"
            value={email}
            placeholder="Email"
            onChange={(e) => setEmail(e.target.value)}
          />
          <input className="input-login"
            type="password"
            value={password}
            placeholder="Password"
            onChange={(e) => setPassword(e.target.value)}
          />

          <div  className="container-login-options">
            <div className="container-login-options-checkbox">
               <input type="checkbox" value="remember" id="checkbox-remember"/>
                <label htmlFor="checkbox-remember">Remember me </label>
            </div>


            <Link className="container-login-options-Link " to="" > Forgot password</Link>
          </div>
          
          <button type="submit" className="submit__btn">
            Submit
          </button>


        </form>


      </div>
    </div>
  );
};

export default Login;
