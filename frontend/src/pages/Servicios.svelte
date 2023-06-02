<script>
    import InputComponent from "../components/InputComponent.svelte";
    
  
    let selectedFile;
    let imageURL;
  
    const handleFileSelected = (event) => {
      selectedFile = event.detail;
      imageURL = URL.createObjectURL(selectedFile);
    };
  </script>
  
  <div>
    <!-- componente -->
    <InputComponent on:fileSelected={handleFileSelected} />
    {#if !selectedFile}
        <img src='https://i.blogs.es/ceda9c/dalle/1366_2000.jpg' alt="">
    {:else }
        <img src={imageURL} alt="">
    {/if}
    
  </div>
  
  <style>
    img {
      max-width: 100%;
      max-height: 200px;
    }
  </style>