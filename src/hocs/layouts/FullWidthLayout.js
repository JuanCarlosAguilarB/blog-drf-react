import Navbar from 'components/navbar/Navbar'
import Footer from 'components/navigation/Footer'
import React from 'react'
import { connect } from 'react-redux'


const FullWidthLayout = ({ children }) => {
  return (
    <>
      <Navbar />
         {children}
      <Footer />
    </>
  )
}

// para  ahcer uso correctamente de redux 
const mapStateToProps = state => ({

})

export default connect(mapStateToProps, {

})(FullWidthLayout)
