<template>
  <div @click="busmapClick">
    <search-overlay
      :routes="routes"
      :visible="searchVisible"
      :action="searchAction"
      @close-search-overlay="handleCloseSearchOverlay"
      @select-search-result="handleSelectSearchResult">
    </search-overlay>

    <top-bar :message="message"></top-bar>

    <map-svg
      :selected="selected"
      :highlighted="highlighted"
      :routes="routes"
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

export default {
  props: [
    'user',
    'routes',
  ],
  data: function () {
    return {
      'message': `Hi ${this.user.name}, you are cool.`,
      'selected': null,
      'highlighted': null,
      'actionbarOpen': false,
      'actions': [
        {
          'text': 'Search',
          'id': 'search',
          'icon': 'fa-search',
        },
        {
          'text': 'Mark Delayed',
          'id': 'mark-delayed',
          'icon': 'fa-clock',
        },
      ],
      'routes': this.routes,
      'searchVisible': false,
      'searchAction': '',
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
            'id': 'mark-delayed',
            'icon': 'fa-clock',
          },
        ]
      }
      this.actionbarOpen = false;
    },
    handleSetActionbarOpen: function (actionbarOpen) {
      this.actionbarOpen = actionbarOpen;
    },
    handleSelectAction: function (action) {
      this.searchVisible = true;
      this.searchAction = action;
    },
    handleSelectSpace: function (selected) {
      this.selected = selected;
      this.actions = [
        {
          'text': 'Assign Bus',
          'id': 'assign-bus',
          'icon': 'fa-plus',
        },
        {
          'text': 'Search',
          'id': 'search',
          'icon': 'fa-search',
        },
        {
          'text': 'Mark Delayed',
          'id': 'mark-delayed',
          'icon': 'fa-clock',
        },
      ]
    },
    handleCloseSearchOverlay: function () {
      this.searchVisible = false;
    },
    handleSelectSearchResult: function (e) {
      console.log(e.route);
      console.log(e.context);
    },
    handleWsMessage: function (e) {
      const data = e.data;
      this.routes = data.routes;
    }
  }
}
</script>
