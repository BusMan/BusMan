<template>
<div class="search-overlay">
    <div class="search-bar">
        <input type="text" placeholder="Search here...">
        <span class="cancel-button">Cancel</span>
    </div>
    <div class="search-results">
        <ul>
            <li v-for="route in routes">{{ route.routeName }}</li>
        </ul>
    </div>
</div>
</template>

<script>
export default {
  props: [
    'routes',
  ],
  watch: {},
  methods: {},
}
</script>
