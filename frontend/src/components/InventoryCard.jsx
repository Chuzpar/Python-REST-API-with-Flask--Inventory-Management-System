import { useState } from "react";
function InventoryCard({ item }) {

    const [isEditing, setIsEditing] = useState(false);
console.log(isEditing);
    return (

        <div className="card">

            <h2>{item.product_name}</h2>

            <p>Brand: {item.brands}</p>

            <p>Price: ${item.price}</p>

            <p>Stock: {item.stock}</p>

            <button onClick={() => setIsEditing(true)}>
                Edit
            </button>
        </div>

    );

}

export default InventoryCard;