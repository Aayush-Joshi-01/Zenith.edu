import React, { useEffect, useRef, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

export default function CoursesNavbar() {
  const navigate = useNavigate();
  const username = sessionStorage.getItem("Username");
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const menuRef = useRef(null);
  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };
  const handleClickOutside = (event) => {
    if (menuRef.current && !menuRef.current.contains(event.target)) {
      setIsMenuOpen(false);
    }
  };

  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  return (
    <nav className="flex bg-gray-900 text-white justify-start items-center p-4">
      <Link to="/courses" className="flex items-center">
        <img src="/logo.png" className="h-6 ml-5 sm:h-9" alt="Logo" />
      </Link>
      
    </nav>
  );
}
