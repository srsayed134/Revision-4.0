import React, { useState } from 'react'

const TodoList = () => {
  // useState([]) This is the place of array where todos will store
  // todos is tore
  // setTodos by this we change list of todos
  const [ todos, setTodos ] = useState([])

  // useState("") place where input is stpring
  // inputValue is getting input from form inout
  // setInputValue can change inputValue 
  const [inputValue, setInputValue] = useState("")
 
  
  //When we type on input box this function run 
  const handleChange = e => {
    setInputValue(e.target.value) //e → the event object target → the HTML element that triggered the event (the <input>) value → the current value of that input
  }
  
  //When we click submit handleSubmit come with e and we should prevent of that 
  //by if we chack input is trimed and copy all previous todos and paste it to setTodos()
  //after we clear input value by setInputValue("")
  const handleSubmit = e => {
    e.preventDefault() //Browser does not reload iteself when submit is clicked without any action browser always do default action in default action refresh is one of them. If browser refresh todos info will gone
    if(inputValue.trim()){
      setTodos([...todos, inputValue]);
      setInputValue("")
    }
  }


  return (
    <div>
      <h1>List of to do</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" value={inputValue} onChange={handleChange} placeholder='Add a new todo'/>
        <button type='submit'>Add todo</button>
      </form>

      <ul>
        {todos.map((todo, index)=> <li key={index}>{todo}</li>)}
      </ul>
    </div>
  )
}

export default TodoList