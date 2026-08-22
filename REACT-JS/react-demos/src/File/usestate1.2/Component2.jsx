import React from 'react'

const Component2 = ({count, onClickHandler}) => {
  const handleClick = () => onClickHandler()
  return (
    <div>
      <p>{count}</p>
      <button onClick={onClickHandler}>Increment</button>
    </div>
  )
}

export default Component2