import { useState } from "react";

function AddProductForm() {

    return (
        <div>
            <h2>Add Product</h2>

            <form>

                <input
                    type="text"
                    placeholder="Product Name"
                />

                <br /><br />

                <input
                    type="text"
                    placeholder="Brand"
                />

                <br /><br />

                <input
                    type="text"
                    placeholder="Ingredients"
                />

                <br /><br />

                <input
                    type="number"
                    placeholder="Price"
                />

                <br /><br />

                <input
                    type="number"
                    placeholder="Stock"
                />

                <br /><br />

                <button>Add Product</button>

            </form>
        </div>
    );
}

export default AddProductForm;