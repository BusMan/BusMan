<template>
<div class="topbar">
  {{ message }}
</div>
</template>

<script>
import { translateRouteStatusType } from '../../utils/utils';
export default {
  props: [
    'user',
    'routes'
  ],
  data: function () {
    return {
      'message': ''
    };
  },
  created: function () {
    this.updateMessage();
  },
  methods: {
    findUserRoute: function () {
      if (!this.user.route_id) {
        return null;
      }
      for (let route of this.routes) {
        if (route.id == this.user.route_id) {
          return route;
        }
      }
      return null;
    },
    updateMessage: function () {
      const route = this.findUserRoute();
      if (!route) {
        this.message = `Hi ${this.user.name}, have a nice day!`;
      } else {
        this.message = `Hi ${this.user.name}, your bus is ${translateRouteStatusType(route.status).toLowerCase()}.`;
      }
    }
  },
  watch: {
    user: function () {
      this.updateMessage();
    },
    routes: function () {
      this.updateMessage();
    }
  }
}
</script>
