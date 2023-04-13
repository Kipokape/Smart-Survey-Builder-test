import React from 'react';
import Button from '@material-ui/core/Button';
import { Link as RouterLink } from 'react-router-dom';

const styles = {
  center: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '5vh',
    marginTop: '6%',
    marginBottom:'6%',
  }
};


function CreatePollButton() {

  return (
    <div style={styles.center}>    
      <Button sx={{ my: 2,  display: 'block'}} 
      color="secondary" 
      variant="contained" 
      type="submit"  
      component={RouterLink} to="/constructorPoll"
      >
        Создать опрос
      </Button>

    </div>
  );
}
export default CreatePollButton;