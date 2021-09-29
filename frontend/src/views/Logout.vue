<template>
  <div></div>
</template>
<script>
export default {
  name: 'Logout',
  data: () => ({
  }),
  computed: {
  },
  watch: {
  },
  created() {
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      this.$router.push({path: 'Auth'})
  }
}
</script>
<style>
</style>