// 1. Function reserved key+++++++++++++
/*
function App(){
  return <h1>Hello, this is test</h1>
}
export default App; 
*/
// 2. Arrow function +++++++++++++++++++
/*
const App = () => {
     return <h1>Sayed</h1>
}
export default App; */
// Challenge 1 :- ----------------------
// import React from 'react'
// import Greet from './Challenges/01. Create Greet/Greet'
// const App = () => {
//   return (
//     <div><Greet/></div>
//   )
// }
// export default App
//Challenge 2 :-------------------------
// import React from 'react'
// import Footer from './Challenges/02. Layout/Footer'
// function App() {
//   return (
//     <div>
//       <Footer/>
//     </div>
//   )
// }
// export default App 
// 3. Jsx +++++++++++++++++++++++++++++
// import React from 'react'
// const App = () => {
//   return (
//     <div>
//       <section>
//         <p>This is test</p>
//       </section>
//     </div>
//   )
// }
// export default App
//Challenge 3 :-------------------------
/*
import React from 'react'
import Jsx from './Challenges/03. JSX/Jsx'
const App = () => {
  return (
    <div>
      <Jsx/>
    </div>
  )
}
export default App
*/
//Challenge 4 :-------------------------
/*
import React from 'react'
import Jsxrules from './Challenges/04. JSX rules/Jsxrules'
const App = () => {
  return (
    <div>
      <Jsxrules/>
    </div>
  )
}
export default App
*/
// 4. _jsx is how react compile simple html to js  ++++++++++
// Type: 1
/*
import React from 'react'
function App() {
  return (
    <section>
      <article>
        <h1>My website</h1>
        <p className='text'>Paragraph content</p>
      </article>
    </section>
  )
}
export default App
*/
// Type: 2
// copy section from type 1 to bable js website
// 5. Expression in js ++++++++++++++++++++++
/*
import React from 'react'
export default function App() {
  return (
    <div>2 + 2</div>
  )
} */
// but 
/*
import React from 'react'
const App = () => {
  return (
    <div>{2+2}</div>
  )
}
export default App
*/
//but
/*
import React from 'react'
const App = () => {
  const name = "Sayed";
  const multiply = (a, b) => a*b;
  const customClass = "simple-class";
  return (
    <div>
      <h1>This is {name}</h1>
      <p>{multiply(2, 10)}</p>
      <p>Friends list : {["Alex", "Jhon", "Wahed", "Jordan"]}</p>
      <p className={customClass}>This customized class</p>
    </div>
  )
}
export default App
*/
// Challenge 5 :--------------------------------
/*
import React from 'react'
import Greting from './Challenges/05. Greeting/Greting'
const App = () => {
  return (
    <div><Greting/></div>
  )
}
export default App
*/
/*
import React from 'react'
import ProductInfo from './Challenges/05. Greeting/ProductInfo'
const App = () => {
  return (
    <div>
      <ProductInfo/>
    </div>
  )
}
export default App
*/
/*
import React from 'react'
import Productinfo2 from './Challenges/05. Greeting/Productinfo2'
const App = () => {
  return (
    <div>
      <Productinfo2/>
    </div>
  )
}
export default App
*/
// 6. Lists in react +++++++++++++++++++++++
/*
import React from 'react'

const App = () => {
  const numbers = [1,2,3,4,5,6,7]
  return (
    <div>
        {numbers.map(number => (
          <ul key={number}>
            <li>{number}</li>
          </ul>
        ))}
    </div>
  )
}

export default App
*/
// 07.Rendering Lists Of Data+++++++++++++++++++++
/*
import React from 'react'

const App = () => {

  const userInfo = [
    {name: "Maxwell",
      dob: 2003,
      place: "Welington"
    },
    {
      name: "Jhon",
      dob: 2005,
      place: "Dunkin"
    },{
      name: "Inor",
      dob: 2000,
      place: "Snispol"
    },
  ]

  return (
    <div>
         {userInfo.map(user => (
          <ul key={user.dob}>
            <li>{user.name}</li>
            <li>{user.dob}</li>
            <li>{user.place}</li>
          </ul>
         ))}
    </div>
  )
}

export default App
*/
// Destructuring+++++++++++++++++++++++
/*
import React from 'react'

const App = () => {
  const userInfo = [
    {name: "Maxwell",
      dob: 2003,
      place: "Welington"
    },
    {
      name: "Jhon",
      dob: 2005,
      place: "Dunkin"
    },{
      name: "Inor",
      dob: 2000,
      place: "Snispol"
    },
  ]

  return (
    <div>
      {userInfo.map(({name, dob, place})=> (
        <ul>
          <li>{name}</li>
          <li>{dob}</li>
          <li>{place}</li>
        </ul>
      ))}
    </div>
  )
}

export default App
*/

// Challenge 6: ----------------------
/*

import React from 'react'
import UserList from './Challenges/06. Lists/UserList'
import ProductList from './Challenges/06. Lists/ProductList'

const App = () => {
  return (
    <div>
      <UserList/>
      <ProductList/>
    </div>
  )
}

export default App
*/

// 08. Props +++++++++++++++++++++++++++
/*
import React from 'react'

const App = () => {
  return <User name="Huxn" age={22} isMarried={false} hobbies={["Codding", "Reading", "Watching Movies"]} />
}
const User = (props) => {
  return (<section>
    <h1>Name: {props.name}</h1>
    <h1>Age: {props.age}</h1>
    <h1>Martitial Status: {props.isMarried}</h1>
    <h1>Hobbies: {props.hobbies}</h1>
  </section>
  )
}

export default App
*/

//Props destrucring++++++++++++++++++++++
/*
import React from 'react'

const App = () => {
  return <User name="Huxn" age={22} isMarried={false} hobbies={["Codding", "Reading", "Watching Movies"]} />
}
const User = ({name, age, isMarried, hobbies}) => {
  return (<section>
    <h1>Name: {name}</h1>
    <h1>Age: {age}</h1>
    <h1>Martitial Status: {isMarried}</h1>
    <h1>Hobbies: {hobbies}</h1>
  </section>
  )
}

export default App
*/

// Challenge 07: ------------------------------
/*
import React from 'react'
import Person from './Challenges/07.Props/Person'
import Product from './Challenges/07.Props/Product'
import Children from './Challenges/07.Props/Children'

const App = () => {
  return (
  <div>
    <Person name = "Huxn" age = {20}/>
    <Product name = "Mac air m5" price={1200}/>
    <Children>
      <h1>This is data from parent</h1>
    </Children>
    <Children>
      <h1>This is data from parent 2</h1>
    </Children>
    <Children>
      <h1>This is data from parent 3</h1>
    </Children>
  </div>
  )
}

export default App
*/ 
// 09: Conditional rendering+++++++++++++

/*
const ValidPass = () => <h1>Valid Password</h1>;
const InvalidPass = () => <h1>Invalid Password</h1>;

// const Password = ({isValid}) => {
//     if(isValid){
//       return <ValidPass/>
//     }
//     return <InvalidPass/>
// }

//Ternery operator

const Password =({isValid}) => {
  return isValid ? <ValidPass/> : <InvalidPass/>
}

import React from 'react'

const App = () => {
  return (
    <div>
      <Password isValid={false}/>
    </div>
  )
}

export default App
*/ 
//Challenge 08: ------------------------
/*
import React from 'react'
import Weather from './Challenges/08.Conditional Rendering/Weather'
import UserStatus from './Challenges/08.Conditional Rendering/UserStatus'
import Gretting from './Challenges/08.Conditional Rendering/Gretting'

const App = () => {
  return (
    <div>
      <Weather temp={30}/>
      <UserStatus user={true} admin={true}/>
      <Gretting timeOfDay={23}/>
    </div>
  )
}
export default App
*/

// 10. Styling -----------------------

import React from 'react'

const App = () => {
  return (
    <div>App</div>
  )
}

export default App