const Vue = require('vue');
const App = require('./busmap.vue');

new Vue({
  el: '#app',
  render: function (createElement) {
    return createElement(App, {
      props: window.data
    });
  }
});
