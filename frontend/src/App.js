import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react'

function App() {
  const [cars, setCars] = useState([])
  useEffect(()=>{
    fetch('/api/v1/cars').then(value => value.json()).then(value => setCars(value.data))
  },[])
  return (
    <div>
      {cars.map(value => (<div key={value.id}>{JSON.stringify(value)}</div>))}
    </div>
  );
}

export default App;
