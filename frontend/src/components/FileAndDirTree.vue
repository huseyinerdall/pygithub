<template>
  <v-row>
    <v-col cols="3">
      <v-navigation-drawer
          class="deep-purple accent-4"
          dark
          fixed
          permanent
          width="300"
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
    </v-col>
    <v-col cols="9" class="pa-2 pt-10">
      <v-textarea
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
export default {
  data: () => ({
    initiallyOpen: ['public'],
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
    code: ''
  }),
  props: {
    repo: {
      type: String
    }
  },
  computed: {
    selected () {
      if (!this.active.length) return undefined
      if (this.active[0] == selectedFile) return undefined
      const selectedFile = this.active[0]
      return selectedFile
    },
  },
  watch: {
    selected() {
      if (!this.active[0]) return undefined
      this.codeLoading = true
      axios.get(this.active[0])
          .then(res => {
            this.codeLoading = false
            this.code = typeof res.data == 'object' ? JSON.stringify(res.data) : res.data
          })
    },
  },
  components: {
  },
  created() {
    axios.get(`https://api.github.com/repos/huseyinerdall/${this.repo}/contents`)
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
  methods: {
    fetchFiles(item) {
      return fetch(item.url)
          .then(res => res.json())
          //.then(json => (item.children.push(...json)))
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
    editorInit: function(editor) {
      console.log(editor);
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
</style>