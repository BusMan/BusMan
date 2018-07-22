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
    'user',
    'routes'
  ],
  data: function () {
    return {
      'message': `Hi ${this.user.name}, you are cool.`,
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
