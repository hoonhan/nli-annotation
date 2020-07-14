<template>
  <div class="home">
    <premise msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Premise from '@/components/Premise.vue'

export default {
  name: 'Annotation',
  components: {
    Premise
  }
}
</script>
