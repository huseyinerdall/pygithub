<template>
  <div class="auth">
      <v-container>
          <v-form class="mx-auto mt-16" style="width:50%">
              <v-text-field
                label="Github Acces Token"
                outlined
                v-model="token"
              ></v-text-field>
              <v-btn :loading="loading" @click="authGithub" block color="primary">Gönder</v-btn>
          </v-form>
      </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: 'Auth',
  data : () => ({
      token: '',
      loading: false,
  }),
  components: {
    
  },
  methods: {
      authGithub() {
          this.loading = true
          axios.post(`http://localhost:8000/api/auth/`,{token:this.token})
          .then((res)=> {
              this.loading = false
              console.log(res.data);
              if(res.data.login){
                  let username = res.data.login
                  localStorage.setItem('token',this.token)
                  localStorage.setItem('username',username)
                  this.$router.push({ path: `/search/${username}` })
              } else{
                  alert('Token is invalid')
              }
          })
          .catch((err) => {
              this.loading = false
              console.log(err);
          })
      }
  }
}
</script>