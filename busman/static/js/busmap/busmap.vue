<template>
  <div @click="busmapClick">
    <top-bar :message="message"></top-bar>
    <map-svg :selected="selected" :highlighted="highlighted" :routes="routes" @select-space="select"/>
    <action-bar :actions="actions" :actionbarOpen="actionbarOpen" @set-actionbar-open="setActionbarOpen"></action-bar>
  </div>
</template>

<script>
import topBar from './components/topBar.vue';
import mapSvg from './components/mapSvg.vue';
import actionBar from './components/actionBar.vue';

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
    }
  },
  components: {
    topBar,
    mapSvg,
    actionBar,
  },
  methods: {
    busmapClick: function (e) {
      if (!this.actionbarOpen && e.target.nodeName !== 'path') {
        console.log('hello');
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
    setActionbarOpen: function (actionbarOpen) {
      this.actionbarOpen = actionbarOpen;
    },
    select: function (selected) {
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
    }
  }
}
</script>
