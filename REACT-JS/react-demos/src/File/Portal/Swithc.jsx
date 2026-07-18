import React, { useState } from 'react'

const Swithc = () => {

    const [sw, setSw] = useState(false)

  return (
    <div>
        {sw ? <span>White</span>:<span>Black</span>}
        <br />
        <input type="text" key={sw ? "dark" : "light"}/>
        <button onClick={() => setSw((s) => !s)}>Switch</button>
    </div>
  )
}

export default Swithc