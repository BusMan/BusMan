<template>
<div class="actionbar"
  @click="actionBarClick"
  @touchstart="actionBarTouchStart" @touchmove="actionBarTouchMove" @touchend="actionBarTouchEnd"
  @mousedown="actionBarTouchStart" @mousemove="actionBarTouchMove" @mouseup="actionBarTouchEnd">
  <div v-for="action in actions" class="action" :data-action="action.id"
    @touchstart="actionTouchStart" @touchend="actionTouchEnd"
    @mousedown="actionTouchStart" @mouseup="actionTouchEnd">
    <i :class="['fa', action.icon]"></i>
    <span>{{ action.text }}</span>
  </div>
</div>
</template>

<script>
export default {
  props: [
    'actions'
  ],
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
        this.lockedOpen = true;
      }

      actionBar.style.transform = "translateY(" + newY + "px)";
    },
    actionBarTouchEnd: function (e) {
      console.log('actionBarTouchEnd');
      const actionBar = document.getElementsByClassName("actionbar")[0];
      
      this.actionBarTouchInProgress = false;

      if (this.moving) {
        if (!this.lockedOpen) {
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
            .addEventListener('finish', function () {
              actionBar.style.transform = 'translateY(6rem)';
            }
          );
        }
      }
      this.moving = false;
      actionBar.dataset.touchInProgress = false;
    },
    actionBarClick: function (e) {
      e.stopPropagation();
      console.log('action clicked');
      
      const actionSelected = e.target.dataset.action;
      switch (actionSelected) {
        case 'assign-bus':
          console.log('assign-bus');
          break;
        case 'search':
          console.log('search');
          break;
        case 'mark-delayed':
          console.log('mark-delayed');
          break;
        default:
          console.log('unrecognized action');
          break;
      }
    },
    actionTouchStart: function (e) {
      this.actionSelectedHtml = e.target;
      this.actionSelectedHtml.style.backgroundColor = '#f9f9f9';
    },
    actionTouchEnd: function (e) {
      if (!this.actionSelectedHtml) return;
      this.actionSelectedHtml.style.backgroundColor = '$fff';
    }
  }
}
</script>
