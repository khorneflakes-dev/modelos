<script>
  import './lib/Tailwind.css';
  import Navbar from './navbar.svelte';
  import { Router, Link, Route } from 'svelte-routing'
  import Home from './pages/Home.svelte';
  import Nosotros from './pages/Nosotros.svelte'
  import Servicios from './pages/Servicios.svelte';
  import Portafolio from './pages/Portafolio.svelte';
  import Modelos from './pages/Modelos.svelte';
  import Unete from './pages/Unete.svelte';
  import Contacto from './pages/Contacto.svelte';
</script>

<Router>

  <Navbar/>
  <Route path='/'>
    <Home/>
  </Route>
  <Route path='/Nosotros'>
    <Nosotros/>
  </Route>
  <Route path='/Servicios'>
    <Servicios/>
  </Route>
  <Route path='/Portafolio'>
    <Portafolio/>
  </Route>
  <Route path='/Modelos'>
    <Modelos/>
  </Route>
  <Route path='/Unete'>
    <Unete/>
  </Route>
  <Route path='/Contacto'>
    <Contacto/>
  </Route>
</Router>