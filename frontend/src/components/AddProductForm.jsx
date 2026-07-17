import { useState } from "react";

function AddProductForm({ onProductAdded }) {

    const [productName, setProductName] = useState("");
    const [brand, setBrand] = useState("");
    const [ingredients, setIngredients] = useState("");
    const [price, setPrice] = useState("");
    const [stock, setStock] = useState("");

    async function handleSubmit(event) {

        event.preventDefault();

        const newProduct = {
            product_name: productName,
            brands: brand,
            ingredients_text: ingredients,
            price: Number(price),
            stock: Number(stock)
        };

        console.log("Sending to Flask:", newProduct);

        const response = await fetch("http://127.0.0.1:5000/inventory", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(newProduct)
        });

        console.log("Status:", response.status);

        if (response.ok) {

            console.log("Product added successfully!");

            setProductName("");
            setBrand("");
            setIngredients("");
            setPrice("");
            setStock("");

            if (onProductAdded) {
                onProductAdded();
            }

        } else {

            alert("Failed to add product.");

        }

    }

    return (
        <div>

            <h2>Add Product</h2>

            <form onSubmit={handleSubmit}>

                <input
                    type="text"
                    placeholder="Product Name"
                    value={productName}
                    onChange={(event) => setProductName(event.target.value)}
                />

                <br /><br />

                <input
                    type="text"
                    placeholder="Brand"
                    value={brand}
                    onChange={(event) => setBrand(event.target.value)}
                />

                <br /><br />

                <input
                    type="text"
                    placeholder="Ingredients"
                    value={ingredients}
                    onChange={(event) => setIngredients(event.target.value)}
                />

                <br /><br />

                <input
                    type="number"
                    placeholder="Price"
                    value={price}
                    onChange={(event) => setPrice(event.target.value)}
                />

                <br /><br />

                <input
                    type="number"
                    placeholder="Stock"
                    value={stock}
                    onChange={(event) => setStock(event.target.value)}
                />

                <br /><br />

                <button type="submit">Add Product</button>

            </form>

        </div>
    );

}

export default AddProductForm;