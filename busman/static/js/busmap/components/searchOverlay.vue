<template>
  <transition name="search-popup">
    <div class="search-overlay" v-if="visible" @click.stop>
      <div class="search-bar">
        <span class="cancel-button" @click="close"><i class="fas fa-arrow-left"></i></span>
        <input type="text" placeholder="Search here..." v-model="queryText">
      </div>
      <div class="search-results">
        <ul>
          <div v-for="group in getSortedRouteGroups(queryText)">
            <h4>{{ group.status }}</h4>
            <li v-for="route in group.routes" @click="select(route)">{{ route.routeName }}</li>
          </div>
        </ul>
      </div>
    </div>
  </transition>
</template>

<script>
import {translateRouteStatusType, actionsEnum} from '../../utils/utils';

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
      if (this.action == actionsEnum.ASSIGN_BUS) {
        sortedRouteGroups = this.getRouteGroups(query, ['o', 'd']);
      } else if (this.action == actionsEnum.SEARCH) {
        sortedRouteGroups = this.getRouteGroups(query, ['a', 'd', 'o']);
      } else if (this.action == actionsEnum.DELAY_BUS) {
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
          'status': translateRouteStatusType(routeStatusType),
          'routes': groups[routeStatusType]
        });
      }
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
    select: function (route) {
      this.$emit('select-search-result', route);
      this.close();
    }
  },
}
</script>
