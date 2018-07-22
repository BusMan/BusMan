<template>
  <div>
    <top-bar :message="message"></top-bar>
    <mapsvg/>
  </div>
</template>

<script>
import topBar from './components/topBar.vue';
import mapsvg from './components/mapSvg.vue';

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
    topBar,
    mapsvg,
  }
}
</script>
