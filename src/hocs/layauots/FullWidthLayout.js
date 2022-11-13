import React from 'react'
import { connect } from 'react-redux'


const FullWidthLayout = ({children}) => {
  return (
    <>
    {children}
    </>
  )
}

// para  ahcer uso correctamente de redux 
const mapStateToProps = state => ({

})

export default connect(mapStateToProps,{

})(FullWidthLayout)
