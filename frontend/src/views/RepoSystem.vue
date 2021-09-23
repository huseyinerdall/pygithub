<template>
  <div class="repo-f-s">
    <FileAndDirTree :repo="reponame"/>
  </div>
</template>

<script>
// @ is an alias to /src
import FileAndDirTree from '@/components/FileAndDirTree.vue'

export default {
  name: 'Home',
  data: () => ({
    reponame: ''
  }),
  components: {
    FileAndDirTree
  },
  created(){
    this.reponame = this.$route.params.reponame
  }
}
</script>
