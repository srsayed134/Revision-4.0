import React from 'react'

const Person = (props) => {
  return (
    <div>
        <h1>Name is {props.name}</h1>
        <h1>Name is {props.age}</h1>
    </div>
  )
}

export default Person