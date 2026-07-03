import React from 'react'

const MorningGretting = () => <h1>Good Morning</h1>
const AfternoonGretting = () => <h1>Good Afternoon</h1>

const Gretting = ({timeOfDay}) => {
    if(timeOfDay < 12){
        return <MorningGretting/>
    }else if(12 < timeOfDay){
        return <AfternoonGretting/>
    }
}

export default Gretting