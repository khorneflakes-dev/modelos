<script>
    let files
    const handleSubmit = async () => {
        
        const formData = new FormData();
        formData.append('filename', files[0].name)
        formData.append('datafile', files[0])
        const response = await fetch('http://localhost:8000/images', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: formData
        });
        if (response.ok) {
        alert('Datos enviados correctamente');
        } else {
        alert('Error al enviar los datos');
        }
    
    

  };
</script>


<form on:submit|preventDefault = {handleSubmit} class="pt-20">

    <input type="file" bind:files={files}>
    <button type="submit">Enviar</button>
</form>