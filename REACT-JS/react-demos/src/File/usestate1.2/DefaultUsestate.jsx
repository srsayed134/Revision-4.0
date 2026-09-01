import React, { useState } from 'react'

const DefaultUsestate = () => {
    const [count, setCount] = useState(() => {
        const initialCount = 20;
        return initialCount
    })
    
    //When we click Increment this funtion will run and inside of this increment there is another setCount func run
    const increment = () => {
        setCount((currentCount) => currentCount + 5)
        console.log(count) //In this line see count is change after function
    }
    

  return (
    <div>
        <h1>{count}</h1>
        <button onClick={increment}>Increment</button>

    </div>
  )
}

export default DefaultUsestate