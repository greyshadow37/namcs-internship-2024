import { useState } from "react";
import axios from "axios";
function App(){
  const [data,setData]=useState(null);
  const[error,setError]=useState(null);
  const fetchAPI=async() =>{
    try{
      const response= await axios.get("http://127.0.0.1:5000/predict")
      setData(response.data);
    }catch(error){
      setError(error);
    }
  }
  const Click=()=>{
    fetchAPI();
  };
    
  return(
    <div>
      <h1 style={{border:"1px solid black",padding:"10 px",color:"blue"}}> Weather predicting app</h1>
      <h2 style={{border:"1px solid red",padding:"10px",color:"green"}}>Welcome to our weather predicting app</h2>
      <h3 style={{color:"black"}}>enter precipitation</h3>
      <input type="number" placeholder="Enter precipitation" />
      <h3 style={{color:"black"}}>enter humidity</h3>
      <input type="number" placeholder="Enter humidity"/>
      <h3 style={{color:"black"}}>enter temperature </h3>
      <input type="number" placeholder="Enter temperature"/>
      <button type="submit" style={{width:"100%",height:"50px",color:"green",position:"relative"}} onClick={Click}>enter</button>
      {error && <div>Error:{error.message}</div>}
      {data && <div>Predicted weather: {JSON.stringify(data)}</div>}
      
      
    </div>
    

    
  );
}
export default App
