<template>
<div class="search-overlay" v-if="visible">
    <div class="search-bar">
        <input type="text" placeholder="Search here...">
        <span class="cancel-button" @click="close">Cancel</span>
    </div>
    <div class="search-results">
        <ul>
            <li v-for="route in routes">{{ route.routeName }} - {{ route.status }}</li>
        </ul>
    </div>
</div>
</template>

<script>
export default {
  props: [
    'routes',
    'visible',
  ],
  watch: {},
  methods: {
      close: function () {
          this.$emit('close-search-overlay');
      }
  },
}
</script>
