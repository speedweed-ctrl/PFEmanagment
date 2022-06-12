import React, { useState } from 'react'
import { Col, Form, Row } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import {IoMdAddCircle} from 'react-icons/io'
import axios from 'axios'
import './styling/add.css'

function Add() {
    const [name , setname] = useState('')
    const [cin , setCin] = useState('')
    const [Institue , setInstitue] = useState('')
    const [annee , setAnnee] = useState('')
    const [notes , setNotes] = useState('')
    const [file , setFile] = useState()


    

    console.log(file)

    const changeHandler = (e)=>{
        setFile(e.target.files[0])
    }
    
        
    const submitHandler = async(e)=>{
        e.preventDefault()

        const formdata = new FormData()

        formdata.append('File' , file)
    
        const payload ={
        'institue':Institue,
        'anneScolere':annee,
        'cin':cin,
        'nomEtudian':name,
        'file':formdata, 
    }
     const config ={
            headers:{
                'enctype':'multipart/form-data'
            }
        }

        
        
        await axios.post("http://127.0.0.1:8000/api/PFE/add" , payload , config  )
        console.log('submit')

        try{
            window.location.replace("/trouver");
        }catch(error){
            console.error(error)
        }
        
    }
   
    return (
        <div className='body'>
        <div className="Container" >
            
            <Form onSubmit={submitHandler} >
            <div className='textFields'>
                
                <Row className="g-2  ">
                    
                    <Col md as='div' className='form-floating' >
                            <Form.Control   type="text" placeholder='nom de l`etudiant'  id = 'student name' className='inputField' value = {name} onChange={(e)=>setname(e.target.value)} required  /> 
                            
                            <label for= 'student name'>nom de l`etudiant</label>
                    </Col>
                    
                </Row><br/>
                
                <Row>
                    <Col md as='div' className='form-floating'>
                        <Form.Control placeholder='numero cin' type='text' id='cin'  className='inputField' value = {cin} onChange={(e)=>setCin(e.target.value)} required  maxLength='8' minLength='8' />
                        <label fro='cin'> numero cin</label>
                    </Col>
                </Row><br/>
                <Row>
                    <Col md as='div' className='form-floating'>
                        <Form.Control placeholder='institue' type='text' id='institue' className='inputField' value = {Institue} onChange={(e)=>setInstitue(e.target.value)} required  />
                        <label for='institue'>institue</label>
                    </Col>
                </Row><br/>
                <Row >
                    <Col md as='div' className='form-floating'>
                        <Form.Control placeholder='année scolaire' type='text' id='année scolaire'  className='inputField' value = {annee} onChange={(e)=>setAnnee(e.target.value)} required />
                        <label for ='année scolaire'>année scolaire</label>
                    </Col>
                </Row><br/>
                {/*
                <Row>
                    <Col md as='div' className='form-floating'>
                        <Form.Control placeholder='les remarque' type='text' id='notes'  className=' notes' value = {notes} onChange={(e)=>setNotes(e.target.value)}/>
                        <label for='notes' >les remarque</label>
                    </Col>
                </Row><br/>*/} 
                
                <Row>
                
                    <Col>
                    
                       <Form.Control type='file' className='fileInput' onChange={changeHandler}/> 
                    </Col>
                </Row>

                 <Row>
                    <Col>
                        <button className='addButton' type='submit'><IoMdAddCircle/></button>
                    </Col>
                </Row>
                
            </div>
            
                
                
            
            </Form>
           
            

            
        </div>
    </div>
    )
}



    

export default Add
