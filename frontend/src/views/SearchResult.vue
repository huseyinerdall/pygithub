<template>
  <v-item-group>
    <v-overlay v-model="overlay"></v-overlay>
    <v-container>
      <v-row>
        <v-col>
          <v-card
              v-if="userinfos"
              :loading="loading"
              class="mx-auto my-12"
              max-width="374"
          >
            <template slot="progress">
              <v-progress-linear
                  color="deep-purple"
                  height="10"
                  indeterminate
              ></v-progress-linear>
            </template>

            <v-img
                height="250"
                :src="userinfos.avatar_url"
            ></v-img>

            <v-card-title>{{ userinfos ? userinfos.name : '' }}</v-card-title>

            <v-card-text class="text-justify">
              <div class="my-4 text-subtitle-1">
                <v-icon>mdi-map-marker-radius</v-icon>
                {{ userinfos.location || 'No location information' }}
              </div>

              <div class="my-4 text-subtitle-1">
                <v-icon>mdi-post</v-icon>
                <a class="ml-2" :href="userinfos.blog" target="_blank">{{ userinfos.blog }}</a>
              </div>

              <div class="my-4 text-subtitle-1">
                <v-icon>mdi-text-account</v-icon>
                {{ userinfos.bio || 'No bio text' }}
              </div>

              <div>
                <span>{{userinfos.followers}} Takipçi</span>
                <span class="ml-3">{{userinfos.following}} Takip</span>
              </div>

              <div>
                <span>{{userinfos.public_repos}} Repositories</span>
                <span class="ml-3">{{userinfos.public_gists}} Gists</span>
              </div>

            </v-card-text>

          </v-card>
        </v-col>
        <v-col>
          <v-list
              subheader
              two-line
          >
            <v-subheader inset>{{ userinfos.name }}'s repositories</v-subheader>

            <v-list-item
            style="border:1px solid #eee"
                v-for="repo in repos"
                :key="repo.id"
            >
              <v-list-item-avatar>
                <v-icon
                    class="grey lighten-1"
                    dark
                >
                  mdi-source-repository
                </v-icon>
              </v-list-item-avatar>

              <v-list-item-content>
                  <v-list-item-title v-text="repo.name"></v-list-item-title>
<!--                <v-list-item-subtitle v-text="folder.subtitle"></v-list-item-subtitle>-->
              </v-list-item-content>

            </v-list-item>
          </v-list>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Home',
  data: () => ({
    overlay: true,
    userinfos: null,
    repos: [],
    files: [
      {
        color: 'blue',
        icon: 'mdi-clipboard-text',
        subtitle: 'Jan 20, 2014',
        title: 'Vacation itinerary',
      },
      {
        color: 'amber',
        icon: 'mdi-gesture-tap-button',
        subtitle: 'Jan 10, 2014',
        title: 'Kitchen remodel',
      },
    ],
    folders: [],
    loading: false,
    selection: 1,
  }),
  computed: {
  },
  watch: {
  },
  created() {
    let username = this.$route.params.username
    axios.post(`http://localhost:8000/api/user/`,{
      username
    })
    .then((res)=>{
      this.userinfos = res.data;
      axios.get(res.data.repos_url)
          .then((repos)=>{
            this.overlay = false
            this.repos = repos.data
      })
    })
  },
  methods: {
    reserve () {
      this.loading = true
      setTimeout(() => (this.loading = false), 2000)
    },
  }
}
</script>
<style>
</style>