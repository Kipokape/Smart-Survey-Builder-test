import React from 'react';
import Button from '@material-ui/core/Button';

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


function AddQuestionButton() {

  return (
    <div style={styles.center}>    
      <Button sx={{ my: 2,  display: 'block'}} 
      color="secondary" 
      variant="contained" 
      type="submit"  
      >
        Добавить вопрос
      </Button>

    </div>
  );
}
export default AddQuestionButton;