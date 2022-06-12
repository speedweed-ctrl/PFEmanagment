import React from 'react'
import './Header.css'
import { Link } from 'react-router-dom'
import image1 from './image1.png'
import image2 from './image2.png'
function Header() {
    return (

        <>
            <header>
                    <center><h1><div ></div>
                    <div className="img1"> <img src={image1}/></div>
                    <span style={{color:'royalblue'}}>I</span>nstitut
                    <span style={{color:'royalblue'}}>N</span>ational de <span style={{color:'royalblue'}}>R</span>echerche du<span style={{color:'royalblue'}}> G</span>énie <span style={{color:'royalblue'}}>R</span>ural, <span style={{color:'royalblue'}}>E</span>aux et <span style={{color:'royalblue'}}>F</span>orêts</h1></center>
                    <div className="img2"><img src={image2} /></div>
                    <div className="topnav">
                    <Link className="active" to='/Home'>Home</Link>
                    <Link to='/add'>Ajouter Un Dossier PFE</Link>
                    <Link to='/trouver'>Trouver Un Dossier PFE</Link>
                    </div>
            </header>
        </>
    )
}

export default Header
