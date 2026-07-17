import { useEffect, useState } from "react";
import "./App.css";
import InventoryCard from "./components/InventoryCard";
import AddProductForm from "./components/AddProductForm";

function App() {

    const [inventory, setInventory] = useState([]);

    function fetchInventory() {

        fetch("http://127.0.0.1:5000/inventory")
            .then((response) => response.json())
            .then((data) => setInventory(data))
            .catch((error) => console.error(error));

    }

    useEffect(() => {

        fetchInventory();

    }, []);

    return (

        <div className="container">

            <h1>Inventory Management</h1>

            <AddProductForm onProductAdded={fetchInventory} />

            {inventory.map((item) => (

                <InventoryCard
                    key={item.id}
                    item={item}
                />

            ))}

        </div>

    );

}

export default App;