<template>
<div class="actionbar"
  @click="actionBarClick"
  @touchstart="actionBarTouchStart" @touchmove="actionBarTouchMove" @touchend="actionBarTouchEnd">
  <div v-for="action in actions" class="action" :data-action="action.id">
    <i :class="['fa', action.icon]"></i>
    <span>{{ action.text }}</span>
  </div>
</div>
</template>

<script>
export default {
  props: [
    'actions',
    'actionbarOpen',
  ],
  watch: {
    'actionbarOpen': function () {
      if (!this.actionbarOpen) {
        this.moving = true;
        this.lockedOpen = false;
        this.actionBarTouchEnd();
        this.$emit('set-actionbar-open', false);
      }
    },
  },
  // TODO: move touch events to busmap.vue
  methods: {
    actionBarTouchStart: function (e) {
      console.log('actionBarTouchStart');
      const actionBar = document.getElementsByClassName("actionbar")[0];

      this.currentY = e.clientY || e.touches[0].clientY;
      this.startY = this.currentY;
      this.actionBarStartY = parseFloat(getComputedStyle(actionBar).transform.replace(/.*, /g, '').replace(')', ''));
      this.lockedOpen = false;
      this.actionBarTouchInProgress = true;
      actionBar.dataset.touchInProgress = true;
    },
    actionBarTouchMove: function (e) {
      console.log('actionBarTouchMove');
      const actionBar = document.getElementsByClassName("actionbar")[0];

      this.actionBarTouchInProgress = this.actionBarTouchInProgress && actionBar.dataset.touchInProgress == 'true';
      if (!this.actionBarTouchInProgress) return;

      this.moving = true;
      this.currentY = e.clientY || e.touches[0].clientY;

      const deltaY = this.currentY - this.startY;
      const pixelsPerRem = parseFloat(getComputedStyle(document.documentElement).fontSize);
      const numberOfActions = 3;
      const initialOffsetInPixels = (2 * numberOfActions) * pixelsPerRem;
      
      let newY = this.actionBarStartY + deltaY;
      if (newY > initialOffsetInPixels) {
        newY = initialOffsetInPixels;
      } else if (newY < 0) {
        newY = 0;
      }

      this.lockedOpen = (newY < initialOffsetInPixels / 2);

      actionBar.style.transform = "translateY(" + newY + "px)";
    },
    actionBarTouchEnd: function (e) {
      console.log('actionBarTouchEnd');
      const actionBar = document.getElementsByClassName("actionbar")[0];
      
      this.actionBarTouchInProgress = false;

      if (this.moving) {
        let endframePosition;
        if (this.lockedOpen) {
          this.$emit('set-actionbar-open', true);
          endframePosition = 0;
        } else { 
          this.$emit('set-actionbar-open', false);
          endframePosition = 6;
        }

        const frames = [
          {
            transform: actionBar.style.transform,
          },
          {
            transform: 'translateY(' + endframePosition + 'rem)',
          }
        ]
        const options = {
          easing: 'cubic-bezier(0, 0, 0.31, 1)',
          duration: 100
        }
        actionBar
          .animate(frames, options)
          .addEventListener('finish', function () {
            actionBar.style.transform = 'translateY(' + endframePosition + 'rem)';
          }
        );
      }
      this.moving = false;
      actionBar.dataset.touchInProgress = false;
    },
    actionBarClick: function (e) {
      e.stopPropagation();
      console.log('action clicked');
      
      const actions = {
        'assign-bus': this.assignBus,
        'search': this.search,
        'mark-delayed': this.markDelayed,
      }
      const actionSelected = e.target.dataset.action;
      const actionFunction = actions[actionSelected];
      actionFunction();
    },
    assignBus: function() {
      console.log('assignBus');
    },
    search: function() {
      console.log('search');
    },
    markDelayed: function() {
      console.log('markDelayed');
    },
  }
}
</script>
