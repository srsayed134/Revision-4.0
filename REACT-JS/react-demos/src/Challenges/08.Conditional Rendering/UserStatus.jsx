import React from 'react'

const User = () => <h1>Welcome User</h1>
const Admin = () => <h1>Welcome Admin</h1>

const UserStatus = ({user, admin}) => {
    if(user && admin){
      return <Admin/>
    }else if(user){
      return <User/>
    }
}

export default UserStatus