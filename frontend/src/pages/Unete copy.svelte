<script>
  import Uploader from "../components/uploader.svelte";
  let selectedFile;
  let imageURL;

  import Image1 from '../assets/modelo_frontal.jpg'

  const handleFileSelected = (event) => {
      selectedFile = event.detail;
      imageURL = URL.createObjectURL(selectedFile);
    };
</script>

<div class="pt-20">

  <Uploader on:demoChange={handleFileSelected} defaultImage={Image1}/>

</div>