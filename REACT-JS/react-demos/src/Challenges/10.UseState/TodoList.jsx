import React, { useState } from 'react'

const TodoList = () => {
   const [todos, setTodo] = useState([])
   const [inputValue, setInputValue] = useState("")


  return (
    <div>
        <h1>List: {todos.map(todo => <li key={Math.random()}>{todo}</li>)}</h1>
        f
    </div>
  )
}

export default TodoList