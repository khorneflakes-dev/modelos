<script>
    import { createEventDispatcher } from 'svelte';
  
    const dispatch = createEventDispatcher();
  
    let selectedFile;
  
    const handleFileChange = (event) => {
      selectedFile = event.target.files[0];
      // el metodo fileSelected expone la variable selectedFile
      dispatch('fileSelected', selectedFile);
    };
</script>
  
<div class="pt-20">
    <input type="file" on:change={handleFileChange}>
</div>