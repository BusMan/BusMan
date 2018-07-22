<template>
  <div>
    <top-bar :message="message"></top-bar>
    <map-svg :selected="selected" :highlighted="highlighted"/>
  </div>
</template>

<script>
import topBar from './components/topBar.vue';
import mapSvg from './components/mapSvg.vue';

export default {
  props: [
    'topbar',
    'routeList'
  ],
  data: function () {
    return {
      'message': this.topbar.message,
      'selected': null,
      'highlighted': null
    }
  },
  components: {
    topBar,
    mapSvg,
  }
}
</script>
