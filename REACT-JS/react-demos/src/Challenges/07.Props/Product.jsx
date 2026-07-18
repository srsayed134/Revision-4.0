import React from 'react'

const Product = ({name, price}) => {
  return (
    <div>
        <h1>The product is {name} and price {price}</h1>
    </div>
  )
}

export default Product