import React, { useState } from 'react'

const ExampleOne = () => {

    const [count, setCount] = useState(() => {
        const initialCount = 10;
        return initialCount
    })

    const handleIncrement = () => {
        setCount((prevCount) => prevCount + 1)
    }

  return (
    <div>
        <h1>{count}</h1>
        <button onClick={handleIncrement}>Increment</button>
    </div>
  )
}

export default ExampleOne