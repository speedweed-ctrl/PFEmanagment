import React from 'react'
import { NavDropdown } from 'react-bootstrap'
import './Header/Header.css'
function Header() {
    return ( 
    <div>
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary p" >
            <div className="container-fluid p-4 parentDiv">
                    <h1 className="tspace" href="#">Navbar</h1>
                    
                        <center>
                        <ul className="navbar-nav me-auto">   
                            <li className="nav-item dropdown ispace">
                            <NavDropdown title="Dropdown" id="basic-nav-dropdown" as='h4'>
                                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                            </NavDropdown>
                            </li>
                            <li className="nav-item dropdown ispace">
                            <NavDropdown title="Dropdown" id="basic-nav-dropdown" as='h4'>
                                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                            </NavDropdown>
                            </li>
                            <li className="nav-item dropdown ispace">
                            <NavDropdown title="Dropdown" id="basic-nav-dropdown" as='h4'>
                                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                            </NavDropdown>
                            </li>
                        </ul>
                        </center>
                        <h3 className='ml-3'> loged in as</h3>
                    
            </div>
        </nav>
    </div>

    )       
        

    
}

export default Header
