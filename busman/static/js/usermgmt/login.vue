<template>
  <div>
    <login-header :school="school"></login-header>
    <tooltip/>
  </div>
</template>

<script>
import loginHeader from './components/header.vue';

export default {
  props: [
    'school'
  ],
  components: {
    loginHeader
  }
}
</script>
