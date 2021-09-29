<template>
  <v-app id="app">
    <v-app-bar class="align-center" fixed>
      
      <div id="nav">
        <router-link to="/">Home</router-link>
      </div>
      <v-spacer></v-spacer>
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
      <v-btn :href="'/search/'+username">ARA</v-btn>
      <v-spacer></v-spacer>
      <v-btn @click="logout">Logout</v-btn>
    </v-app-bar>
    <v-container class="mt-8">
      <router-view/>
    </v-container>
    <notifications group="error" position='top center' width=400 />
    <notifications group="success" position='top center' width=400 />
  </v-app>
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
    },
    logout() {
      this.$router.push({name:'Logout'})
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
