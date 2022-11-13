import React from 'react'
import FullWidthLayout from 'hocs/layauots/FullWidthLayout'
import { connect } from 'react-redux'

const Home = () => {
  return (
    <FullWidthLayout>
      Home
    </FullWidthLayout>
  )
}

const mapStateToProps = state =>(
    {})
    

export default connect(mapStateToProps,{

})(Home)
