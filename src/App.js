import Header from './Header/Header'
import Home from './components/Home/Home'
import Table from './components/browse_pfe/Table'
import { BrowserRouter as Router , Route } from 'react-router-dom'
import Add from './components/add_pfe/Add';

function App() {
  return (
    <Router >
        <Header/>
        <Route path="/Home" component={Home}/>
        <Route path='/trouver' component={Table}/>
        <Route path='/add' component={Add}/>
    </Router>
  );
}

export default App;
