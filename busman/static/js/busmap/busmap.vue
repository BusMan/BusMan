<template>
  <top-bar :message="message"></top-bar>
</template>

<script>
import topBar from './components/topBar.vue';

export default {
  props: [
    'topbar'
  ],
  data: function () {
    return {
      'message': this.topbar.message
    }
  },
  components: {
    topBar
  }
}
</script>
