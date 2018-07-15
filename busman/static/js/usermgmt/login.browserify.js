const Vue = require('vue');
const VTooltip = require('v-tooltip');
const App = require('./login.vue');

Vue.use(VTooltip);
new Vue({
  el: '#app',
  render: function (createElement) {
    return createElement(App, {
      props: window.data
    });
  }
});
