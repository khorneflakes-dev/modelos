<script>
    import { Router, Link, Route } from 'svelte-routing'
    import './lib/Tailwind.css'
    import Logo from'./assets/logo.svg'
</script>

<div class="flex h-16 w-screen font-montserrat fixed z-50 bg-[#f6f6f6] border-b border-gray-400 text-gray-600" id="navbar">
    <div class="w-full flex items-center justify-center border-r border-gray-400">
        <Link to='/'>
            <img class="w-3/4 h-3/4" src={Logo} alt="logo">
        </Link>
    </div>
    <div class="w-full flex items-center justify-center border-r border-gray-400">
        <Link to='/Nosotros'>
            SOBRE NOSOTROS
        </Link>
    </div>
    <div class="w-full flex items-center justify-center border-r border-gray-400">
        <Link to='Servicios'>
            SERVICIOS
        </Link>
    </div>
    <div class="w-full flex items-center justify-center border-r border-gray-400">
        <Link to='Portafolio'>
            PORTAFOLIO
        </Link>
    </div>
    <div class="w-full flex items-center justify-center border-r border-gray-400">
        <Link to='/Modelos'>
            MODELOS
        </Link>
    </div>
    <div class="w-full flex items-center justify-center border-r border-gray-400">
        <Link to='/Unete'>
            UNETE AL EQUIPO
        </Link>
    </div>
    <div class="w-full flex items-center justify-center">
        <Link to='/Contacto'>
            CONTACTO
        </Link>
    </div>
  </div>