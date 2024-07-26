import { useState } from "react";
import axios from "axios";
function App(){
  const [precipitation,setPrecipitationData]=useState("");
  const [humidity,setHumidityData]=useState("");
  const [temperature,setTemperatureData]=useState("");
  const [outputData,setOutputData]=useState("");
  const[error,setError]=useState(null);
  const handleSubmit=async event =>{
    event.preventDefault();
    try{
      const params={
        Temperature:parseFloat(temperature),
        Humidity:parseFloat(humidity),
        Precipitation:parseFloat(precipitation),
      }
      const response= await axios.post("http://127.0.0.1:5000/predict",params)
      setOutputData(response.data);
    }catch(error){
      setError(error);
    }
  };
  const handlePrecipitationChange= event=>{
    setPrecipitationData(event.target.value);
  };
  const handleHumidityChange= event=>{
    setHumidityData(event.target.value);
  };
  const handleTemperatureChange= event=>{
    setTemperatureData(event.target.value);
  };
    
  return(
    <div>
      <h1 style={{border:"1px solid black",padding:"10 px",color:"blue"}}> Weather predicting app</h1>
      <h2 style={{border:"1px solid red",padding:"10px",color:"green"}}>Welcome to our weather predicting app</h2>
      <form onSubmit={handleSubmit}>
        <label>
          
          <h3 style={{color:"black"}}>enter precipitation</h3>
          <input type="number" value={precipitation} onChange={handlePrecipitationChange} placeholder="Enter precipitation" />
          <h3 style={{color:"black"}}>enter humidity</h3>
          <input type="number" value={humidity} onChange={handleHumidityChange} placeholder="Enter humidity"/>
          <h3 style={{color:"black"}}>enter temperature </h3>
          <input type="number" value={temperature} onChange={handleTemperatureChange} placeholder="Enter temperature"/>
        </label>
        <button type="submit" style={{width:"100%",height:"50px",color:"green",position:"relative"}}>Submit</button>
      </form>
      {error && <div>Error:{error.message}</div>}
      {outputData && <div>{JSON.stringify(outputData)}</div>}
      
      
    </div>
    

    
  );
}
export default App
