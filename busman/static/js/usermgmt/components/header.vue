<template>
  <header>
    <h1>busman</h1>
    <span>
      <b>{{ school }} </b>
    </span>
  </header>
</template>

<script>
export default {
  props: [
    'school'
  ]
}
</script>
