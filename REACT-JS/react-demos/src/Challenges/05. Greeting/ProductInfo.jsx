import React from 'react'

const ProductInfo = () => {

    const name = "Laptop";
    const price = "$1200";
    const availability = "In Stock";

  return (
    <div>
      <p>The product is {name} this will cost around {price} , i think it is {availability}
      </p>
    </div>
  )
}

export default ProductInfo