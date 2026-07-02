import React from 'react'

const Productinfo2 = () => {
    const products = {
        name: "Laptop",
        price: 1200,
        stock: "Available",
    }
  return (

    <div>
        <h1>The product is {products.name} and 
            price will be {products.price} and
             i think it is {products.stock}
        </h1>
    </div>
  )
}

export default Productinfo2