import React, { useState } from 'react'

const ExampleTwo = () => {
    const [randomNumber, setRendomNumber] = useState(() => Math.floor(Math.random() * 100))

    const genNewNumber = () => {
        const newNumber = Math.floor(Math.random() * 100);
        setRendomNumber(newNumber)
    }
  return (
    <div>
        <h1>Random Numbrs: {randomNumber}</h1>
        <button onClick={genNewNumber}>New Random number</button>
    </div>
  )
}

export default ExampleTwo