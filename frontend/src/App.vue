<template>
  <div id="app">
    <v-app-bar class="d-flex align-center">
      <div id="nav">
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link>
      </div>
      <div>
        <v-text-field solo dense hide-details v-model="username">
          <template v-slot:label>
            Kullanıcı Adı
            <v-icon>
            mdi-file-find
          </v-icon>
          </template>
        </v-text-field>
      </div>
      <router-link :to="'/search/'+username" tag="button">ARA</router-link>
    </v-app-bar>
    <router-view/>
  </div>
</template>
<script>
export default {
  data: () => ({
    username: ''
  }),
  computed: {
  },
  watch: {
  },
  created() {

  },
  methods: {
    searchUser() {
      if (this.username == '') return undefined
      this.$router.push({ name: 'SearchResult', params: { username: this.username } })
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
