<template>
<div class="actionbar">
  <div v-for="action in actions" class="action">
    <i :class="['fa', action.icon]"></i>
    <span>{{ action.text }}</span>
  </div>
</div>
</template>

<script>
export default {
  props: [
    'actions'
  ],
}
</script>
