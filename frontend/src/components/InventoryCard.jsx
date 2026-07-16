function InventoryCard({ item }) {

    return (

        <div className="card">

            <h2>{item.product_name}</h2>

            <p>Brand: {item.brands}</p>

            <p>Price: ${item.price}</p>

            <p>Stock: {item.stock}</p>

            <button>Edit</button>

        </div>

    );

}

export default InventoryCard;