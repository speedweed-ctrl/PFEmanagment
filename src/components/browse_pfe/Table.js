import React , {useState , useEffect } from 'react'
import { Form , Col , Row ,  } from 'react-bootstrap'
import axios from 'axios'
import {AiOutlineSearch} from 'react-icons/ai'
import './styling/table.css'
import { AiFillEye , AiFillDelete } from 'react-icons/ai'

function Table() {

     const [data , setData] = useState([])
     const [search , setSearch] = useState('student')
     const [pk , setpk] = useState('')
     const[message , setMessage] = useState('')

     useEffect(()=>{

         async function getData(){
             const {data} = await axios.get('http://127.0.0.1:8000/api/PFE/getAll')
             setData(data)
         }
         
         getData()
     }, [])

     
     
     console.log(search)
     
     const submitHandler = async (e) =>{
        e.preventDefault()
        const {data} = await axios.get(`http://127.0.0.1:8000/api/PFE/unique_PFE/${search}/${pk}`)
        try{
            setData(data)
        }catch(error){
            setData([])
        }

       
     }

     const deleteHandler = async(e , id) =>{
        
        const {res} = await axios.delete(`http://127.0.0.1:8000/api/PFE/Delete/${id}`)

        /* used this function to reaload the page after a delete*/ 
        window.location.reload()
        
        
        try{
            setMessage(res)
        }catch(error){
            setMessage('an error has happend could not delete')
        }
     }
     console.log(data)
     

    return (
        <div className='body'>
        <div className="tableContainer" >
            <Form onSubmit={submitHandler}>
            <Row className="g-2 SearchContainer">
                <Col md className='input'>
                        <Form.Control  value={pk} type="text" placeholder={`search by ${search}`} onChange={(e)=>setpk(e.target.value)}  /> 
                </Col>
                <Col md>
                    
                    
                       <select className='searchSelector'  onChange={(e)=>setSearch(e.target.value)  }  >
                           <option value='student'>search by student name</option>
                           <option value = 'year' >search by year</option>
                           <option value = 'institue'>search by institue</option>
                       </select>
                </Col>
                <Col md>
                    <button type='submit' disabled={!pk} className='searchButton'><AiOutlineSearch/></button>
                </Col>
            </Row><br/>
            </Form>

            <table className="table table-dark">
                <thead>
                    <tr>
                        <th scope="col"></th>
                        <th scope="col">nom etudiant</th>
                        <th scope="col">numero cin</th>
                        <th scope="col">institue</th>
                        <th scope="col">anne scolair</th>
                        <th scope="col">id</th>
                        <th scope="col">visit or delete</th>
                        
                    </tr>
                </thead>
                <tbody>
                    {data.map((data)=>{
                        return(
                            <tr>
                            <th scope="row">{data.id}</th>
                            <td>{data.nomEtudian}</td>
                            <td>{data.cin}</td>
                            <td>{data.institue}</td>
                            <td>{data.anneScolere}</td>
                            <td>{data.uniqueID}</td>
                            <td><button className='delete' onClick={(e)=>deleteHandler(e , data.id)} ><AiFillDelete/></button></td>
                        </tr>
                        )
                         
                    })}
                </tbody>
            </table>
        </div>
    </div>
    )
}

export default Table
