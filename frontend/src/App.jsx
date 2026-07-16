import { useEffect, useState } from "react";

function App() {

  const [inventory, setInventory] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:5000/inventory")
      .then((response) => response.json())
      .then((data) => setInventory(data))
      .catch((error) => console.error(error));

  }, []);

  return (
    <div>
      <h1>Inventory Management</h1>

      {inventory.map((item) => (
        <div key={item.id}>
          <h3>{item.product_name}</h3>

          <p>Brand: {item.brands}</p>

          <p>Price: ${item.price}</p>

          <p>Stock: {item.stock}</p>

          <hr />
        </div>
      ))}
    </div>
  );
}

export default App;