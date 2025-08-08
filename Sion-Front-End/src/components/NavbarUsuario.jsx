
import "../style/NavbarUsuario.css";
import React, { useState } from "react";
import { FaHome, FaStore, FaPhoneAlt, FaUserCircle, FaBars, FaTimes } from "react-icons/fa";
import LogoSion from '../Img/LogoSion1.png'
function NavbarUsuario() {
    const [menuAbierto, setMenuAbierto] = useState(false);

    const toggleMenu = () => {
        setMenuAbierto(!menuAbierto);
    };

    const cerrarMenu = () => {
        setMenuAbierto(false);
    };

    return (
        <nav className="navbar-usuario">
        <div className="logo-usuario"><img src={LogoSion} alt="" width={50} /><span>Sion</span></div>

        <div className="menu-icon" onClick={toggleMenu}>
            {menuAbierto ? <FaTimes /> : <FaBars />}
        </div>

        <ul className={menuAbierto ? "links-usuario activo" : "links-usuario"}>
            <li><a href="#inicio" onClick={cerrarMenu}><FaHome /> Inicio</a></li>
            <li><a href="#tienda" onClick={cerrarMenu}><FaStore /> Tienda</a></li>
            <li><a href="#contacto" onClick={cerrarMenu}><FaPhoneAlt /> Contacto</a></li>
            <li><a href="#perfil" onClick={cerrarMenu}><FaUserCircle /> Mi Cuenta</a></li>
        </ul>
        </nav>
    );
}

export default NavbarUsuario;








