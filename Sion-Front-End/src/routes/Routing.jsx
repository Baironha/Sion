import React from 'react';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';


import HomePage from '../page/HomaPage';


function Routing() {


    return (
        <div>
            <Router>
                <Routes>

                        {/* Paginas de usuarios */}
                        <Route path="/" element={<HomePage/>}/>
                        

                        
                </Routes>
            </Router>
        </div>
    );
}

export default Routing