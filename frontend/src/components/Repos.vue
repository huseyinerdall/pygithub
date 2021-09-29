<template>
  <v-item-group>
    <v-container>
      <v-row>

        <v-col
            v-for="repo in repos"
            :key="repo.id"
            cols="12"
            md="4"
        >
          <v-item v-slot="{ active, toggle }">
            <v-card
                :color="active ? 'primary' : ''"
                class="d-flex align-center"
                dark
                height="200"
                @click="toggle"
            >
              <v-scroll-y-transition>
                <div
                    v-if="active"
                    class="text-h2 flex-grow-1 text-center"
                >
                  Active
                </div>
              </v-scroll-y-transition>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
  <!--  <v-container>
      <v-item-group mandatory>
        <v-container>
          <v-row>
            <v-col
                v-for="repo in repos"
                :key="repo.id"
                cols="12"
                md="4"
            >
              <v-item v-slot="{ active, toggle }">
                {{repo.name}}
                <v-card
                    :color="active ? 'primary' : ''"
                    class="d-flex align-center"
                    dark
                    height="200"
                    @click="toggle"
                >
                  <v-scroll-y-transition>
                    <div
                        v-if="active"
                        class="text-h2 flex-grow-1 text-center"
                    >
                      Active
                    </div>
                  </v-scroll-y-transition>
                </v-card>
              </v-item>
            </v-col>
          </v-row>
        </v-container>
      </v-item-group>
    </v-container>-->
</template>
<script>
import axios from 'axios'
export default {
  name: 'Home',
  data: () => ({
    userinfo: null,
    repos: []
  }),
  computed: {
  },
  watch: {
  },
  created() {
    let username = this.$route.params.username
    console.log(username)
    axios.get(`https://api.github.com/users/${username}`)
        .then((res)=>{
          this.userinfos = res.data;
          axios.get(res.data.repos_url)
              .then((repos)=>{
                this.repos = repos.data
              })
        })
  },
  methods: {
  }
}
</script>
<style>
</style>