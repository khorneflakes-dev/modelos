<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    export let defaultImage = null;
    let selectedImage = null;
    let selectedImageMain = null;
  
    function handleImageClick() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/*';
      input.onchange = handleFileChange;
      input.click();
    }
  
    function handleFileChange(event) {
      const file = event.target.files[0];
      dispatch('demoChange', file);
      if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = (e) => {
          selectedImage = e.target.result;
        };
        reader.readAsDataURL(file);
      } else {
        selectedImage = null;
      }
    }
</script>
  
  <style>
    .image-container {
      width: 330px;
      height: 500px;
      border: 1px solid #ccc;
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      cursor: pointer;
      overflow: hidden;
    }
    .main-img {
      width: auto;
      height: 100%;
      object-fit: cover;
      display: block;
      position: center top;
    }
  </style>
  
  <!-- <div class="image-container" style="background-image: url({selectedImage || defaultImage})" on:click={handleImageClick}></div> -->

  <div class='image-container' on:click={handleImageClick} on:keypress={handleImageClick}>
    {#if !selectedImage}
      <img class='main-img' src={defaultImage} alt="">
    {:else}
      <img class='main-img' src={selectedImage} alt="">
    {/if}
    
  </div>

