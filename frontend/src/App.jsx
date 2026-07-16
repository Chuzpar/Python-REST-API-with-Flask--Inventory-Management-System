import { useEffect, useState } from "react";
import "./App.css";

function App() {

  const [inventory, setInventory] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:5000/inventory")
      .then((response) => response.json())
      .then((data) => setInventory(data))
      .catch((error) => console.error(error));

  }, []);

  return (

<div className="container">

<h1>Inventory Management</h1>

{inventory.map((item)=>(

<div className="card" key={item.id}>

<h2>{item.product_name}</h2>

<p>Brand: {item.brands}</p>

<p>Price: ${item.price}</p>

<p>Stock: {item.stock}</p>

</div>

))}

</div>

);
}

export default App;