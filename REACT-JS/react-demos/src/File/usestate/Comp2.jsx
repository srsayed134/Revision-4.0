import React from 'react'

const Comp2 = ({ count, onClickHandler }) => {
    const handleClick = () => onClickHandler()
    return (
        <div>
            <h1>The number is {count}</h1>
            <button onClick={handleClick}>-</button>
        </div>
    )
}

export default Comp2