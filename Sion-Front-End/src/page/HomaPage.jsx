import React from "react";
import NavbarUsuario from "../components/NavbarUsuario";
import Header from "../components/Header";
import Categorias from "../components/Catgorias";
import Carrusel from "../components/Carrusel"
function HomePage(){
    return(
        <div>
            <NavbarUsuario/>
            <Header/>
            <Categorias/>
            <Carrusel/>
        </div>
    )
}
export default HomePage;