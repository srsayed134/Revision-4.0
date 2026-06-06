// 1. Function reserved key
/*
function App(){
  return <h1>Hello, this is test</h1>
}
export default App; 
*/
// 2. Arrow function 
/*
const App = () => {
     return <h1>Sayed</h1>
}
export default App; */

// Challenge 1 :- 

import React from 'react'
import Greet from './Challenges/01. Create Greet/Greet'

function App() {
  return (
    <div><Greet></Greet></div>
  )
}

export default App
