<template>
  <v-textarea :value="url"></v-textarea>
</template>

<script>
export default {
  name: 'CodeField',

  data: () => ({
  }),
  props:{
    url: {
      type: String,
      default: ''
    }
  }
}
</script>
