import React, { useState } from 'react';
import { fetchPrediction } from '../service/api';
import '../App.css';

function App() {
  const [temperature, setTemperature] = useState("");
  const [precipitation, setPrecipitation] = useState("");
  const [humidity, setHumidity] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Convert input values to numeric before sending
      const params = {
        Temperature: parseFloat(temperature),
        Precipitation: parseFloat(precipitation),
        Humidity: parseFloat(humidity),
      };
      const result = await fetchPrediction(params);
      setData(result);
      setError(null);
    } catch (err) {
      setError(err);
      setData(null);
    }
  };

  return (
    <div>
      <h1 style={{ border: "1px solid black", padding: "10px", color: "blue" }}>
        Weather Prediction App
      </h1>
      <h2 style={{ border: "1px solid red", padding: "10px", color: "green" }}>
        Welcome to our weather prediction app
      </h2>
      <form onSubmit={handleSubmit}>
        <div>
          <h3 style={{ color: "black" }}>Enter temperature</h3>
          <input
            type="number"
            value={temperature}
            onChange={(e) => setTemperature(e.target.value)}
            placeholder="Enter temperature"
          />
        </div>
        <div>
          <h3 style={{ color: "black" }}>Enter precipitation</h3>
          <input
            type="number"
            value={precipitation}
            onChange={(e) => setPrecipitation(e.target.value)}
            placeholder="Enter precipitation"
          />
        </div>
        <div>
          <h3 style={{ color: "black" }}>Enter humidity</h3>
          <input
            type="number"
            value={humidity}
            onChange={(e) => setHumidity(e.target.value)}
            placeholder="Enter humidity"
          />
        </div>
        <button
          type="submit"
          style={{ width: "100%", height: "50px", color: "green" }}
        >
          Enter
        </button>
      </form>
      {error && <div>Error: {error.message}</div>}
      {data && <div>Predicted weather: {data['Weather Condition']}</div>}
    </div>
  );
}

export default App;
