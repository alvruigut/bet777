import logo from './logo-alc.png';
import './App.css';
import React from 'react';

function App() {
  const loginFormRef = React.createRef();

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
       
      </header>
    </div>
  );
}

export default App;
