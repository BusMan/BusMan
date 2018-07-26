<template>
  <div @click="click" @mouseup="mouseup">
    <top-bar :message="message"></top-bar>
    <map-svg :selected="selected" :highlighted="highlighted"/>
    <action-bar :actions="actions"></action-bar>
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
      'actions': [
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
      ],
    }
  },
  components: {
    topBar,
    mapSvg,
    actionBar,
  },
  methods: {
    click: function (e) {
      console.log('main page click');
      const actionBar = document.getElementsByClassName('actionbar')[0];
      if (!actionBar) return;
      const numberOfActions = this.actions.length;
      const initialOffsetInRem = numberOfActions * 2;
      const frames = [
        {
          transform: actionBar.style.transform,
        },
        {
          transform: 'translateY(6rem)',
        }
      ]
      const options = {
        easing: 'cubic-bezier(0, 0, 0.31, 1)',
        duration: 100
      }
      actionBar
        .animate(frames, options)
        .addEventListener('finish', function() {
          actionBar.style.transform = 'translateY(6rem)';
        }
      );
    },
    mouseup: function (e) {
      const actionBar = document.getElementsByClassName('actionbar')[0];
      actionBar.dataset.touchInProgress = false;
    }
  }
}
</script>
