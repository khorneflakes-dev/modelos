<script>
  import Image1 from '../assets/modelo_frontal.jpg'
  import Uploader from '../components/uploader.svelte';
  
  let selectedFile1;
  let selectedFile2;
  let selectedFile3;
  let selectedFile4;
  let selectedFile5;
  let selectedFile6;

  const handleFileSelected1 = (event) => {selectedFile1 = event.detail;};

  const handleFileSelected2 = (event) => {selectedFile2 = event.detail;};

  const handleFileSelected3 = (event) => {selectedFile3 = event.detail;};

  const handleFileSelected4 = (event) => {selectedFile4 = event.detail;};

  const handleFileSelected5 = (event) => {selectedFile5 = event.detail;};

  const handleFileSelected6 = (event) => {selectedFile6 = event.detail;};


  let pais;
  let lugar_residencia;
  let dispo_viajes;
  let nombre;
  let edad;
  let sexo;
  let ocupacion;
  let nivel_academico;
  let estatura;
  let peso;
  let busto;
  let cintura;
  let cadera;
  let calzado;
  let color_pelo;
  let color_ojos;
  let tono_piel;
  let email;
  let telefono;
  let instagram;
  let facebook;
  let tiktok;

  async function handleSubmit() {
    const formData = new FormData();
    formData.append('pais', pais);
    formData.append('lugar_residencia', lugar_residencia);
    formData.append('dispo_viajes', dispo_viajes);
    formData.append('nombre', nombre);
    formData.append('edad', edad);
    formData.append('sexo', sexo);
    formData.append('ocupacion', ocupacion);
    formData.append('nivel_academico', nivel_academico);
    formData.append('estatura', estatura);
    formData.append('peso', peso);
    formData.append('busto', busto);
    formData.append('cintura', cintura);
    formData.append('cadera', cadera);
    formData.append('calzado', calzado);
    formData.append('color_pelo', color_pelo);
    formData.append('color_ojos', color_ojos);
    formData.append('tono_piel', tono_piel);
    formData.append('email', email);
    formData.append('telefono', telefono);
    formData.append('instagram', instagram);
    formData.append('facebook', facebook);
    formData.append('tiktok', tiktok);

    formData.append('foto1', selectedFile1);
    formData.append('foto2', selectedFile2);
    formData.append('foto3', selectedFile3);
    formData.append('foto4', selectedFile4);
    formData.append('foto5', selectedFile5);
    formData.append('foto6', selectedFile6);

    try {
      const response = await fetch('http://localhost:8000/files/', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        alert('Formulario guardado exitosamente.');
        // Realiza alguna acción adicional si es necesario
      } else {
        alert('Error al guardar el formulario.');
      }
    } catch (error) {
      console.error('Error al realizar la solicitud:', error);
    }
  }

</script>

<!-- <div class="pt-20">
  <Uploader defaultImage={Image1} on:demoChange={handleFileSelected1} />
</div> -->

<form on:submit|preventDefault={handleSubmit} class="pt-20">
  <Uploader defaultImage={Image1} on:demoChange={handleFileSelected1} />
  <Uploader defaultImage={Image1} on:demoChange={handleFileSelected2} />
  <Uploader defaultImage={Image1} on:demoChange={handleFileSelected3} />
  <Uploader defaultImage={Image1} on:demoChange={handleFileSelected4} />
  <Uploader defaultImage={Image1} on:demoChange={handleFileSelected5} />
  <Uploader defaultImage={Image1} on:demoChange={handleFileSelected6} />
  
  <input type="text" bind:value={pais} placeholder="pais" />
  <input type="text" bind:value={lugar_residencia} placeholder="lugar_residencia" />
  <input type="text" bind:value={dispo_viajes} placeholder="dispo_viajes" />
  <input type="text" bind:value={nombre} placeholder="nombre" />
  <input type="text" bind:value={edad} placeholder="edad" />
  <input type="text" bind:value={sexo} placeholder="sexo" />
  <input type="text" bind:value={ocupacion} placeholder="ocupacion" />
  <input type="text" bind:value={nivel_academico} placeholder="nivel_academico" />
  <input type="text" bind:value={estatura} placeholder="estatura" />
  <input type="text" bind:value={peso} placeholder="peso" />
  <input type="text" bind:value={busto} placeholder="busto" />
  <input type="text" bind:value={cintura} placeholder="cintura" />
  <input type="text" bind:value={cadera} placeholder="cadera" />
  <input type="text" bind:value={calzado} placeholder="calzado" />
  <input type="text" bind:value={color_pelo} placeholder="color_pelo" />
  <input type="text" bind:value={color_ojos} placeholder="color_ojos" />
  <input type="text" bind:value={tono_piel} placeholder="tono_piel" />
  <input type="text" bind:value={email} placeholder="email" />
  <input type="text" bind:value={telefono} placeholder="telefono" />
  <input type="text" bind:value={instagram} placeholder="instagram" />
  <input type="text" bind:value={facebook} placeholder="facebook" />
  <input type="text" bind:value={tiktok} placeholder="tiktok" />

  <button type="submit">Enviar</button>

</form>