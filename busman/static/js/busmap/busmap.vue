<template>
  <div @click="busmapClick">
    <search-overlay
      :routes="routeList"
      :visible="searchVisible"
      :action="selectedAction"
      @close-search-overlay="handleCloseSearchOverlay"
      @select-search-result="handleSelectSearchResult">
    </search-overlay>

    <top-bar :message="message"></top-bar>

    <map-svg
      :selected="selected"
      :highlighted="highlighted"
      :routes="routeList"
      @select-space="handleSelectSpace"/>

    <action-bar
      :actions="actions"
      :actionbarOpen="actionbarOpen"
      @set-actionbar-open="handleSetActionbarOpen"
      @select-action="handleSelectAction">
    </action-bar>
  </div>
</template>

<script>
import topBar from './components/topBar.vue';
import mapSvg from './components/mapSvg.vue';
import actionBar from './components/actionBar.vue';
import searchOverlay from './components/searchOverlay.vue';
import {actionsEnum} from '../utils/utils';

export default {
  props: [
    'user',
    'routes',
  ],
  data: function () {
    return {
      'message': `Hi ${this.user.name}, you are cool.`,
      'selected': [],
      'selectedRoute': null,
      'selectedAction': '',
      'highlighted': [],
      'actionbarOpen': false,
      'actions': [
        {
          'text': 'Search',
          'id': actionsEnum.SEARCH,
          'icon': 'fa-search',
        },
        {
          'text': 'Mark Delayed',
          'id': actionsEnum.DELAY_BUS,
          'icon': 'fa-clock',
        },
      ],
      'routeList': this.routes,
      'searchVisible': false,
      'ws': null,
    }
  },
  created: function () {
    const protocol = window.location.protocol.includes('s') ? 'wss' : 'ws';
    const host = window.location.host;
    this.ws = new WebSocket(`${protocol}://${host}/ws/`);
    this.ws.onmessage = this.handleWsMessage;
  },
  components: {
    topBar,
    mapSvg,
    actionBar,
    searchOverlay,
  },
  methods: {
    busmapClick: function (e) {
      if (!this.actionbarOpen && e.target.nodeName !== 'path') {
        this.selected = [];
        this.actions = [
          {
            'text': 'Search',
            'id': 'search',
            'icon': 'fa-search',
          },
          {
            'text': 'Mark Delayed',
            'id': actionsEnum.DELAY_BUS,
            'icon': 'fa-clock',
          },
        ]
      }
      this.actionbarOpen = false;
    },
    sendAction: function (action=this.selectedAction,
                          space_id=this.selected[0],
                          route_id=this.selectedRoute.id) {
      console.info('Sending Action:', {action, space_id, route_id});
      this.ws.send(JSON.stringify({
        action,
        space_id,
        route_id
      }));
      this.selected = [];
      this.selectedAction = '';
      this.selectedRoute = null;
    },
    handleSetActionbarOpen: function (actionbarOpen) {
      this.actionbarOpen = actionbarOpen;
    },
    handleSelectAction: function (action) {
      this.selectedAction = action;
      if (action == actionsEnum.UNASSIGN_BUS) {
        this.sendAction(actionsEnum.UNASSIGN_BUS);
      } else {
        this.searchVisible = true;
      }
    },
    handleSelectSpace: function (space) {
      this.selected = [space.id()];
      if (space.data('route')) {
        this.actions = [
          {
            'text': 'Unassign Bus',
            'id': actionsEnum.UNASSIGN_BUS,
            'icon': 'fa-minus',
          },
          {
            'text': 'Search',
            'id': actionsEnum.SEARCH,
            'icon': 'fa-search',
          },
          {
            'text': 'Mark Delayed',
            'id': actionsEnum.DELAY_BUS,
            'icon': 'fa-clock',
          },
        ]
        this.selectedRoute = space.data('route');
      } else {
        this.actions = [
          {
            'text': 'Assign Bus',
            'id': actionsEnum.ASSIGN_BUS,
            'icon': 'fa-plus',
          },
          {
            'text': 'Search',
            'id': actionsEnum.SEARCH,
            'icon': 'fa-search',
          },
          {
            'text': 'Mark Delayed',
            'id': actionsEnum.DELAY_BUS,
            'icon': 'fa-clock',
          },
        ]
      }
    },
    handleCloseSearchOverlay: function () {
      this.searchVisible = false;
    },
    handleSelectSearchResult: function (route) {
      this.selectedRoute = route;
      if (this.selectedAction == actionsEnum.SEARCH) {
        this.highlighted = [route.space];
      } else {
        this.sendAction();
      }
    },
    handleWsMessage: function (e) {
      const data = JSON.parse(e.data);
      this.routeList = data.routes;
    }
  }
}
</script>
