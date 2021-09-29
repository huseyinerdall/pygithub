<template>
  <v-row>
    <v-col cols="3">
      <v-card>
        <v-navigation-drawer
            class="deep-purple accent-4 ml-2"
            style="margin-top:76px;"
            dark
            permanent
            width="300"
            height="540"
            fixed
        >
          <v-treeview
              v-model="tree"
              :open="initiallyOpen"
              :items="items"
              activatable
              item-key="download_url"
              open-on-click
              :load-children="fetchFiles"
              dense
              :active.sync="active"
              return-object
          >
            <template v-slot:prepend="{ item, open }">
              <v-icon v-if="item.type=='dir'">
                {{ open ? 'mdi-folder-open' : 'mdi-folder' }}
              </v-icon>
              <v-icon v-else>
                {{ files[item.file] || 'mdi-code-tags'}}
              </v-icon>
            </template>
          </v-treeview>
        </v-navigation-drawer>
      </v-card>
    </v-col>
    <v-col cols="9" class="pa-2 pt-10 text-left">
      <v-btn @click="editFile">Update File</v-btn>
      <v-btn @click="deleteFile">Delete File</v-btn>
      <v-textarea
          v-model="code"
          :value="code"
          background-color="grey lighten-2"
          auto-grow
          dense
          outlined
          :row-height="rowHeight"
          spellcheck="false"
          id="code-field"
          :loading="codeLoading"
      >
      </v-textarea>
    </v-col>
  </v-row>
</template>
<script>
import axios from 'axios'
import postData from '../functions/post'
import base64toutf8 from  '../functions/base64toutf8'

export default {
  data: () => ({
    initiallyOpen: ['public'],
    options: {
      selectOnLineNumbers: false
    },
    rowHeight: 20,
    codeLoading: false,
    files: {
      html: 'mdi-language-html5',
      js: 'mdi-nodejs',
      json: 'mdi-code-json',
      py: 'mdi-language-python',
      pdf: 'mdi-file-pdf',
      png: 'mdi-file-image',
      jpeg: 'mdi-file-image',
      jpg: 'mdi-file-image',
      txt: 'mdi-file-document-outline',
      xls: 'mdi-file-excel',
      vue: 'mdi-vuejs',
      c: 'mdi-language-c',
      css: 'mdi-language-css3',
      rs: 'mdi-language-rust',
      go: 'mdi-language-go',
      ts: 'mdi-language-typescript',
      md: 'language-markdown'
    },
    tree: [],
    items: [],
    active: [],
    code: '',
    currentIndex: 0
  }),
  props: {
    repo: {
      type: String
    }
  },
  computed: {
    selected: {
      // getter
      get: function () {
        if (!this.active.length) return undefined
        if (this.active[0] == selectedFile) return undefined
        const selectedFile = this.active[0]
        return selectedFile
      },
      // setter
      set: function (newValue) {
        return newValue
      }

    },
  },
  watch: {
    selected() {
      if (!this.active[0]) return undefined
      this.codeLoading = true
      this.currentIndex = this.items.indexOf(this.active[0])
      axios.get(this.active[0].url,{ params: { t: new Date().getTime() }})
          .then(res => {
            this.codeLoading = false
            this.code = typeof res.data.content == 'object' ? JSON.stringify(base64toutf8(res.data.content),4) : base64toutf8(res.data.content)
          })
    },
  },
  components: {
  },
  created() {
    this.getRepo()
  },
  methods: {
    fetchFiles(item) {
      return fetch(item.url)
          .then(res => res.json())
          .then(json => {
            for (let el of json) {
              if(el.type == 'dir'){
                el.children = [];
              }
              el.file = el.name.split('.').pop()
            }
            item.children.push(...json)
          })
          .catch(err => console.warn(err))
    },
    getRepo() {
      axios.get(`https://api.github.com/repos/huseyinerdall/${this.repo}/contents`,{ params: { t: new Date().getTime() }})
          .then((res)=>{
            for (let el of res.data) {
              if(el.type == 'dir'){
                el.children = []
              }
              el.file = el.name.split('.').pop()
            }
            this.items = res.data;
          })
    },
    editFile(){
      let post_parameters = {
        path: this.selected.path,
        sha: this.items[this.currentIndex].sha,
        content: this.code,
        message: 'message',
        repo_name: this.$route.params.reponame,
        _method: 'POST'
      }
      postData(`http://localhost:8000/api/actions/`,post_parameters)
      .then((res)=>{
        this.getRepo()
        this.selected = res.content
        if(res.content){
          this.$notify({
            group: 'success',
            title: 'Başarılı',
            text: 'Dosyanız kaydedildi',
            type: 'success'
          });
        }
        console.log(res);
        /*delete this.items[this.currentIndex]
        this.items[this.currentIndex] = res.content*/
      })
    },
    deleteFile(){
      let post_parameters = {
        path: this.selected.path,
        sha: this.items[this.currentIndex].sha,
        message: 'message',
        repo_name: this.$router.params.reponame
      }
      postData(`http://localhost:8000/api/actions/`,post_parameters)
      .then((res)=>{
        this.getRepo()
        this.selected = res.content
        /*delete this.items[this.currentIndex]
        this.items[this.currentIndex] = res.content*/
      })
    },
    onMounted(editor) {
      this.editor = editor
    },
    onCodeChange(editor) {
      console.log(editor.getValue())
    }
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@200;400&display=swap');
#code-field{
  font-family: 'Source Code Pro', monospace;
  font-size: 14px;
  line-height: 1;
}
.v-treeview-node__label{
  text-align: left;
  text-indent: 24px;
}
</style>