<script>
    import {Link} from 'svelte-routing'

    import Background from '../assets/background1.png'
    import Facebook from '../assets/redes/facebook.svg'
    import Instagram from '../assets/redes/instagram.svg'
    import Gmail from '../assets/redes/gmail.svg'
    import Whatsapp from '../assets/redes/whatsapp.svg'
    import Tiktok from '../assets/redes/tiktok.svg'
</script>

<div class="w-full h-screen z-0  relative">
    <img class="h-screen w-full" src={Background} alt="">

    <div class="flex h-screen items-end top-0 right-0 pr-20 flex-col text-right z-10 absolute pt-8 gap-12 font-montserrat justify-center">
        <div class="text-5xl font-medium text-[#2F2F2F] w-1/2 pl-12 leading-tight">
            Encuentra modelos de alta calidad para tus campañas publicitarias, desfiles de moda y eventos en Bolivia.
        </div>
        <div class="text-5xl font-medium text-[#2F2F2F] w-1/2 pl-12 leading-tight">
            Únete a nosotros hoy para encontrar los modelos perfectos para tu próximo proyecto.
        </div>
        <Link to='/Contacto'>
            <div class="font-medium bg-[#2F2F2F] text-white text-4xl rounded-full py-2 px-5 tracking-widest">
                <button>CONTACTANOS</button>
            </div>
        </Link>
        <div class="flex gap-8">
            <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
                <img src={Facebook} alt="facebook">
            </a>
            <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
                <img src={Instagram} alt="instagram">
            </a>
            <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
                <img src={Gmail} alt="gmail">
            </a>
            <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
                <img src={Tiktok} alt="tiktok">
            </a>
            <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
                <img src={Whatsapp} alt="whatsapp">
            </a>
        </div>
    </div>
</div>
