
import'../style/HeaderStyle.css';
import imgheader1 from '../Img/HeaderImage1.jpg'

function Header(){
    return(
        <div className="container-header">
            <div className="header">
                <h1 className='Titulo_1_sion'>Sion</h1>
                <h2 className='Titulo2_sion'>LA TIENDA DEL PUEBLO</h2>
                <img className='imgHeader' src={imgheader1} alt="headerOption1" />
            </div>
        </div>
    )
}
export default Header