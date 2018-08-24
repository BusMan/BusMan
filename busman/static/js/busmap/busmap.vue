<template>
  <div @click="handleClickBusmap">
    <search-overlay
      :routes="routeList"
      :visible="searchVisible"
      :action="selectedAction"
      @close-search-overlay="handleCloseSearchOverlay"
      @select-search-result="handleSelectSearchResult">
    </search-overlay>

    <top-bar :user="user" :routes="routeList"></top-bar>

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
import { actionsEnum, viewModeToActionMap } from '../utils/utils';

export default {
  props: [
    'user',
    'routes',
  ],
  data: function () {
    return {
      'selected': null,
      'selectedRoute': null,
      'selectedAction': '',
      'highlighted': [],
      'actionbarOpen': false,
      'actions': this.getActionList(viewModeToActionMap.NONE_SELECTED),
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
    handleClickBusmap: function (e) {
      if (!this.actionbarOpen && e.target.nodeName !== 'path') {
        this.selected = null;
        this.actions = this.getActionList(viewModeToActionMap.NONE_SELECTED);
      }
      this.actionbarOpen = false;
      this.searchVisible = false;
    },
    getActionList: function (viewMode) {
      const viewType = this.user.is_admin ? 'admin' : 'normal';
      return viewMode[viewType];
    },
    sendAction: function (action=this.selectedAction,
                          space_id=this.selected,
                          route_id=this.selectedRoute.id) {
      if (!this.user.is_admin) {
        console.warn('User is not an admin. Not sending: ', {action, space_id, route_id});
        return;
      }
      console.info('Sending Action:', {action, space_id, route_id});
      this.ws.send(JSON.stringify({
        action,
        space_id,
        route_id
      }));
      this.selected = null;
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
      this.selected = space.id();
      if (space.data('route')) {
        this.actions = this.getActionList(viewModeToActionMap.FILLED_SPACE_SELECTED)
        this.selectedRoute = space.data('route');
      } else {
        this.actions = this.getActionList(viewModeToActionMap.BLANK_SPACE_SELECTED);
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
