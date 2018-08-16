<template>
  <transition name="search-popup">
    <div class="search-overlay" v-if="visible">
      <div class="search-bar">
        <span class="cancel-button" @click="close"><i class="fas fa-arrow-left"></i></span>
        <input type="text" placeholder="Search here..." v-model="queryText">
      </div>
      <div class="search-results">
        <ul>
          <div v-for="group in getSortedRouteGroups(queryText)">
            <h4>{{ group.status }}</h4>
            <li v-for="route in group.routes" @click="select" :data-route="route.routeName">{{ route.routeName }}</li>
          </div>
        </ul>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: [
    'routes',
    'visible',
    'action',
    'query',
  ],
  data: function () {
    return {
      'queryText': this.query,
    }
  },
  // TODO: make click on <li> call backend
  methods: {
    close: function () {
      this.$emit('close-search-overlay');
    },
    getSortedRouteGroups: function (query) {
      query = query || '';
      query = query.trim();
      let sortedRouteGroups = [];
      if (this.action == 'assign-bus') {
        sortedRouteGroups = this.getRouteGroups(query, ['o', 'd']);
      } else if (this.action == 'search') {
        sortedRouteGroups = this.getRouteGroups(query, ['a', 'o', 'd']);
      } else if (this.action == 'mark-delayed') {
        sortedRouteGroups = this.getRouteGroups(query, ['o']);
      }
      return sortedRouteGroups;
    },
    getRouteGroups: function (query, order) {
      order = order || [];
      let groups = {};
      for (let routeStatusType of order) {
        groups[routeStatusType] = [];
      }

      let results = this.getQueriedRoutes(query);
      for (let route of results) {
        let routeStatus = route['status'];
        if (routeStatus in groups) {
          groups[routeStatus].push(route);
        }
      }

      // TODO: alphabetically sort routes within each group
      let routeGroups = [];
      for (let routeStatusType of order) {
        routeGroups.push({
          'status': this.translateRouteStatusType(routeStatusType),
          'routes': groups[routeStatusType]
        });
      }
      console.log(routeGroups);
      return routeGroups;
    },
    getQueriedRoutes: function (query) {
      let results = [];
      for (let route of this.routes) {
        if (route['routeName'].toLowerCase().indexOf(query.toLowerCase()) != -1) {
          results.push(route);
        }
      }
      return results;
    },
    translateRouteStatusType: function (routeStatusType) {
      const translations = {
        'o': 'On Time',
        'a': 'Arrived',
        'd': 'Delayed',
      }
      if (routeStatusType in translations) {
        return translations[routeStatusType];
      }
      return '';
    },
    select: function (e) {
      this.$emit('select-search-result', e.target.dataset.route);
      this.close();
    }
  },
}
</script>
