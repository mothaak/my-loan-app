import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoanApplicationForm from './components/LoanApplicationForm';

const App: React.FC = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<LoanApplicationForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
