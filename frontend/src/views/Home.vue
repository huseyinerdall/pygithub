<template>
  <div class="home">
    <Repos/>
  </div>
</template>

<script>
// @ is an alias to /src
import Repos from '@/components/Repos.vue'

export default {
  name: 'Home',
  components: {
    Repos
  }
}
</script>
