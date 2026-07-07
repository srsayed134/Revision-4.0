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

// 10. Styling +++++++++++++++++

//Option 1 
/*
import React from 'react'

const App = () => {
  return (
    <div>
      <h1 style={{color: "red", backgroundColor: "white", padding: "3rem"}}>
      This is red</h1>
    </div>
  )
}

export default App
*/
// Option 2
/*
import React from 'react'

const styles = {
  color: "Blacke",
  backgroundColor: "crimson",
  padding: "2rem"
}

const App = () => {
  return (
    <div>
      <h1 style={styles}>Inline Style</h1>
    </div>
  )
}

export default App
*/
//Option 3
/*
import "./File/styles.css";
import React from 'react'

const App = () => {
  return (
    <div>
      <h1>This is outline css</h1>
    </div>
  )
}

export default App
*/

// 1.Icons ++++++++
//Get import address from website
//<DiAptana /> also from website
/*
import { DiAptana } from "react-icons/di";

import React from 'react'

const App = () => {
  return (
    <div>
      <h1>This is a react icon <DiAptana /></h1>
    </div>
  )
}

export default App
*/
// Challenge 09: -------------------
/*
import React from 'react'
import StyledCard from './Challenges/09.Style/StyledCard'
import ProfileCard from './Challenges/09.Style/ProfileCard'
import IconComponent from './Challenges/09.Style/IconComponent'

const App = () => {
  return (
    <div>
      <StyledCard/>
      <ProfileCard/>
      <IconComponent/>
    </div>
  )
}

export default App
*/

// 11. Events in React.js +++++++++++++++
/*
import React from 'react'
const handleClick = () => console.log(Math.round(Math.random() * 10))
const Button = () => <button onClick={handleClick}>Click</button>

const App = () => {
  return (
    <div><Button/></div>
  )
}

export default App
*/
/*
import React from 'react'

const Copy = () => {
  const copyHandler = () => {
    console.log("Stop stealing my content")
  }

  return (
    <p onCopy={copyHandler}>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorem quidem doloribus iste obcaecati cum explicabo, temporibus tempore cumque saepe officia!</p>
  )
}
*/
/*
const Move = () => {
  const moveHandler = () => {console.log("Mouse is moved")}
  return(
    <p onMouseMove={moveHandler}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Error odit corporis voluptatem quam accusantium eveniet culpa porro a voluptates odio iure hic consequatur aliquid, maxime debitis blanditiis magni dolor? Ipsam molestias numquam commodi provident possimus. Tenetur voluptatum nobis earum reprehenderit? Expedita omnis, eius libero quod debitis nesciunt explicabo ab ad.</p>
  )
}

const App = () => {
  return (
    <div>
      <Copy/> 
      <Move/>
    </div>
  )
}

export default App
*/

// 12.  State & Hooks Introduction
// When we setCount something it rerender everything
//How to update number ^^^^^^^^^^^^^^^^^^
//Example 
/*
import React, { useState } from 'react'

const App = () => {

  const [count, setCount] = useState(0);
  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={increment}> + </button>
      <button onClick={decrement}> - </button>
    </div>
  )
}

export default App
*/
//Example
//How to update array^^^^^^^^^^^^^^^^^^^
/*
import React, { useState } from 'react'

const App = () => {
  const [friends, setFriend] = useState(["Alex", "John", "Michel"])
  const addOneFriend = () => setFriend([...friends, "Huxn WebDev"])
  const removeFriend = () => setFriend(friends.filter(f => f !== "John"))
  const updateFriend = () => setFriend(friends.map(f => f === "Alex" ? "Alex Smith" : f))
  console.log(friends)
  return (
    <div>
      {friends.map(f => (
        <li key={Math.random()}>{f}</li>
      ))}
      <button onClick={addOneFriend}>Add new friend</button>
      <button onClick={removeFriend}>Remove one friend</button>
      <button onClick={updateFriend}>Update one friend</button>
    </div>
  )
}

export default App
*/
//How to update object^^^^^^^^^^^^^^^^^

/*
import React, { useState } from 'react'

const App = () => {
  const [movie, setMovie] = useState({
    title: "Equilizer 3",
    rating: 3,
  })
  const handleChange = () => {
    // const copyMovie = {
    //   ...movie, rating: 4
    // }

    setMovie({...movie, rating: 7});
  }

  return (
    <div>
      <h1>{movie.title}</h1>
      <h1>{movie.rating}</h1>
      <button onClick={handleChange}>Change movie rating</button>
    </div>
  )
}

export default App
*/
//Change Array of object^^^^^^^^^^^^^^^^^^^
/*
import React, { useState } from 'react'

const App = () => {

  const [movies, setMovies] = useState([
    {id: 1, title: "Spider Man", rating: 3},
    {id: 2, title: "Superman", rating: 5},
    {id: 3, title: "Batman", rating: 7},
  ])

  const handleNameChange = () => {
    setMovies(movies.map(movie => (movie.id === 2 ? {...movies, title: "Jhon Wick"}: movie)))
  }

  return (
    <div>
     {movies.map(movie => <li key={Math.random()}>{movie.title}</li>)}
     <button onClick={handleNameChange}>Movie name change</button>
    </div>
  )
}

export default App
*/
//Share state with other^^^^^^^^^^^^^^^^
//Option -1
/*
import React, { useState } from 'react'
import Comp2 from './File/usestate/Comp2'
import Comp1 from './File/usestate/Comp1'

const App = () => {
  const[count, setCount] = useState(0)
  return (
    <div>
      <Comp1 count={count} onClickHandler={() => setCount(count + 1)} />
      <Comp2 count={count} onClickHandler={() => setCount(count - 1)} />
    </div>
  )
}

export default App
*/
//Option - 2
/*
import React from 'react'
import ExampleOne from './File/usestate/ExampleOne'
import ExampleTwo from './File/usestate/ExampleTwo'
import ExampleThree from './File/usestate/ExampleThree'

const App = () => {
  return (
    <div>
      <ExampleOne/>
      <ExampleTwo/>
      <ExampleThree/>
    </div>
  )
}

export default App 
*/
// Challenge 10:- ++++++++++++++++

import React from 'react'
import Counter from './Challenges/10.UseState/Counter'
import TodoList from './Challenges/10.UseState/TodoList'

const App = () => {
  return (
    <div>
      {/* <Counter/> */}
      <TodoList/>
    </div>
  )
}

export default App