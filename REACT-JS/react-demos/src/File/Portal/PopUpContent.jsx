import React from 'react'
import {createPortal} from "react-dom";

const PopUpContent = ({copied}) => {
  return createPortal( //createPortal(JSX, DOMNode)
    <div>
        {copied && (
            <div style={{position: "absolute", bottom: "3rem"}}>
                Copied to clicpboard
            </div> 
        )} 
    </div> ,
    document.querySelector("#popup-content")
  )
}

export default PopUpContent 