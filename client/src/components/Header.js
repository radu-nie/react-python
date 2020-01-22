import React from "react";
import { NavLink } from "react-router-dom";

class Header extends React.Component {
  constructor(props) {
    super();
  }

  render() {
    return (
      <ul className="nav nav-tabs bg-primary">
        <li className="nav-item">
          <NavLink exact to="/" className="nav-link">
            Home
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink to="/about" className="nav-link">
            About
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink to="/contacts" className="nav-link">
            Contacts
          </NavLink>
        </li>
      </ul>
    );
  }
}

export default Header;
