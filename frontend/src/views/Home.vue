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
            <v-row class="mt-4">
              <v-subheader inset>{{ userinfos.name }}'s repositories</v-subheader>
            <v-btn
              class="mx-2"
              dark
              color="indigo"
              @click="createdialog=true"
            > Yeni Repo Ekle
              <v-icon dark>
                mdi-plus
              </v-icon>
            </v-btn>
            </v-row>
            <div >
            
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
                  <router-link :to="'/repo/'+repo.name">
                    <v-list-item-title v-text="repo.name"></v-list-item-title>
                  </router-link>
                </v-list-item-content>
                
                <v-list-item-action>
                  <v-btn icon @click="deleteRepo(repo.name)">
                    <v-icon color="red lighten-1">mdi-delete</v-icon>
                  </v-btn>
                </v-list-item-action>


              </v-list-item>
              
              </div>
            
          </v-list>
        </v-col>
      </v-row>
    </v-container>

  <v-dialog
      v-model="createdialog"
      max-width="600px"
    >
      <v-card>
        <v-card-title>
          <span class="text-h5">Repo Oluştur</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              
              <v-col cols="12">
                <v-text-field
                  v-model="reponame"
                  label="Repo ismi*"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="description"
                  label="Açıklama*"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="createdialog = false"
          >
            İPTAL
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="createNewRepo"
          >
            OLUŞTUR
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-item-group>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Home',
  data: () => ({
    overlay: true,
    reponame: '',
    description: '',
    createdialog: false,
    userinfos: null,
    username: localStorage.getItem('username'),
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
    let username = localStorage.getItem('username')
    axios.post(`http://localhost:8000/api/user/`,{
      username
    })
    .then((res)=>{
      this.userinfos = res.data;
      axios.get(res.data.repos_url,{ params: { t: new Date().getTime() }})
          .then((repos)=>{
            this.overlay = false
            this.repos = repos.data
      })
    })
  },
  methods: {
    refresh() {
      let username = localStorage.getItem('username')
      axios.post(`http://localhost:8000/api/user/`,{
        username
      })
      .then((res)=>{
        this.userinfos = res.data;
        axios.get(res.data.repos_url,{ params: { t: new Date().getTime() }})
            .then((repos)=>{
              this.overlay = false
              this.repos = repos.data
        })
      })
    },
    reserve () {
      this.loading = true
      setTimeout(() => (this.loading = false), 2000)
    },
    createNewRepo() {
      if(this.description =='' || this.reponame == ''){
        this.$notify({
            group: 'error',
            title: 'Error',
            text: 'Alanlar boş bırakılamaz!.',
            type: 'error'
          })
        return
      }
      axios.put(`http://localhost:8000/api/actions/`,{
        reponame: this.reponame,
        description : this.description
      })
      .then((res)=>{
        if(res.data.id){
          this.$notify({
            group: 'success',
            title: 'Başarılı',
            text: 'Repository oluşturuldu.',
            type: 'success'
          })
          this.createdialog = false
          this.refresh()
        } else {
          this.$notify({
            group: 'error',
            title: 'Error',
            text: 'Bir hata oluştu.',
            type: 'error'
          })
          this.createdialog = false
        }
        
      })
    },
    deleteRepo(reponame){
      axios.post(`http://localhost:8000/api/actions/`,{
        reponame: reponame,
        _method : 'DELETE'
      })
      .then((res)=>{
        console.log(res)
        if(res.status == 200){
          this.$notify({
            group: 'success',
            title: 'Başarılı',
            text: 'Repository silindi.',
            type: 'success'
          })
          this.refresh()
        } else {
          this.$notify({
            group: 'error',
            title: 'Error',
            text: 'Bir hata oluştu.',
            type: 'error'
          })
        }
        
      })
    }
  }
}
</script>
<style>
</style>