import React from 'react'

const Greting = () => {
    const name = "John";
    let date = new Date();
  return (
    <div>
        <h1>This is {name}</h1>
        <p>{name} today is {date.toDateString()}</p>
    </div>
  )
}

export default Greting