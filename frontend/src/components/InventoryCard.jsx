import { useState } from "react";
function InventoryCard({ item }) {

    const [isEditing, setIsEditing] = useState(false);
    
    const [editedPrice, setEditedPrice] = useState(item.price);
    const [editedStock, setEditedStock] = useState(item.stock);
    
 return (

    <div className="card">

        <h2>{item.product_name}</h2>

        <p>Brand: {item.brands}</p>

        {isEditing ? (

            <>

                <p>Price</p>

                <input
                    type="number"
                    value={editedPrice}
                    onChange={(event) => setEditedPrice(event.target.value)}
                />

                <p>Stock</p>

                <input
                    type="number"
                    value={editedStock}
                    onChange={(event) => setEditedStock(event.target.value)}
                />

                <br /><br />

                <button>Save</button>

            </>

        ) : (

            <>

                <p>Price: ${item.price}</p>

                <p>Stock: {item.stock}</p>

                <button onClick={() => setIsEditing(true)}>
                    Edit
                </button>

            </>

        )}

    </div>

);
}

export default InventoryCard;