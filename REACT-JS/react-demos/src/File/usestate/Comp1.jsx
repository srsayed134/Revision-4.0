import React from 'react'

const Comp1 = ({ count, onClickHandler }) => {
    const handleClick = () => onClickHandler()
    return (
        <div>
            <h1>The number {count}</h1>
            <button onClick={handleClick}>+</button>
        </div>
    )
}

export default Comp1