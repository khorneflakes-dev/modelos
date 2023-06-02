<script>
    import Uploader from '../components/uploader.svelte';
    import Image1 from '../assets/modelo_frontal.jpg'
    import Image2 from '../assets/demo.jpg'
    let firstImage;
    let secondImage;
    let text_demo;
    let firstImageURL;
    let secondImageURL;

    async function handleSubmit() {
        const formData = new FormData();
        formData.append('file', firstImage);
        formData.append('fileb', secondImage);
        formData.append('token', text_demo);

        try {
        const response = await fetch('http://localhost:8000/files2/', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            alert('Imágenes guardadas exitosamente.');
            // Realiza alguna acción adicional si es necesario
        } else {
            alert('Error al guardar las imágenes.');
        }
        } catch (error) {
        console.error('Error al realizar la solicitud:', error);
        }
    }

    const handleFileSelected1 = (event) => {
        firstImage = event.detail;
        // firstImageURL = URL.createObjectURL(firstImage);
        console.log(firstImage)
        };

    const handleFileSelected2 = (event) => {
        secondImage = event.detail;
        // secondImageURL = URL.createObjectURL(secondImage);
        console.log(secondImage)
        };

</script>

<div class="pt-20">
    <form on:submit|preventDefault={handleSubmit}>
        <!-- <input type="file" on:change={event => firstImage = event.target.files[0]} />
        <input type="file" on:change={event => secondImage = event.target.files[0]} /> -->
        <!-- <Uploader defaultImage={Image1}/> -->
        <Uploader defaultImage={Image1} on:demoChange={handleFileSelected1} />
        <Uploader defaultImage={Image2} on:demoChange={handleFileSelected2} />
        <input type="text" bind:value={text_demo}/>
        <button type="submit">Enviar</button>
      </form>
</div>