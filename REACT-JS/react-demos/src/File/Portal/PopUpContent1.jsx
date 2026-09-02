import React from 'react'
import {createPortal} from "react-dom";
 

const PopUpContent1 = ({copied}) => {
  return createPortal (
   <section>
    {copied && (
        <div style={{position: "absolute", bottom:"3rem"}}>Copied To Clipboard </div>
    )}
   </section>,
   document.querySelector("#popup-content1")
  )
}

export default PopUpContent1