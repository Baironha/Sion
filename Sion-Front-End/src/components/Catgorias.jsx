import "../style/CategoriasProductHome.css";
import CatPerfumes from "../Img/CategoriaPerfumes.png"
import CatElectrodomesticos from "../Img/categoriaElectrodomesticos.jpg"
import CatTecnologia from "../Img/CategoriaTecnologia.jpg"
import CatHerramintas_Jardineria from '../Img/CatHerramientas_Jardineria.png'
import CatAccesoriosPersonales from "../Img/CategoriaAccesorios.jpg"
import CatDiversion_Deporte from '../Img/CategoriaDiversion_Deporte.png'
import CatDescuento from '../Img/CategoriaDescuento.jpg'
import CAtAll from '../Img/CategoriaAll.png'





function Categorias() {
  const categorias = [
    { nombre: "Todo", link: "/todo", img:  CAtAll },
    { nombre: "Descuentos", link: "/descuentos", img: CatDescuento },
    { nombre: "Electrodomésticos", link: "/electrodomesticos", img: CatElectrodomesticos },
    { nombre: "Tecnologia", link: "/electronicos", img: CatTecnologia },
    { nombre: "Perfumes", link: "/perfumes", img: CatPerfumes },
    { nombre: "Herramientas y Jardinería", link: "/jardineria", img: CatHerramintas_Jardineria },
    { nombre: "Accesorios personales", link: "/accesorios", img: CatAccesoriosPersonales },
    { nombre: "Diversión y Deporte", link: "/diversion", img: CatDiversion_Deporte },
  ];

  return (
    <div>
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <div className="categorias-container">
            <h1>Categoria de productos</h1>
            {categorias.map((cat, index) => (
                <a href={cat.link} key={index} className="categoria-card">
                <div className="categoria-img">
                    <img src={cat.img} alt={cat.nombre} />
                </div>
                <span>{cat.nombre}</span>
                </a>
            ))}
        </div>
    </div>
    );
}

export default Categorias;
