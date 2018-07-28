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
        this.moveActionBar(true);
        this.$emit('set-actionbar-open', false);
      }
    },
  },
  methods: {
    clamp: function (value, minimum, maximum) {
      return Math.max(Math.min(value, maximum), minimum)
    },
    actionBarTouchStart: function (e) {
      console.log('actionBarTouchStart');

      this.currentY = e.clientY || e.touches[0].clientY;
      this.startY = this.currentY;

      const actionBar = document.getElementsByClassName("actionbar")[0];
      const actionBarTransformMatrixString = getComputedStyle(actionBar).transform;
      this.actionBarStartY = parseFloat(actionBarTransformMatrixString.replace(/.*, /g, '').replace(')', ''));

      this.lockedOpen = false;
      this.actionBarTouchInProgress = true;
    },
    actionBarTouchMove: function (e) {
      console.log('actionBarTouchMove');      
      if (!this.actionBarTouchInProgress) return;

      this.moving = true;

      this.currentY = e.clientY || e.touches[0].clientY;
      const deltaY = this.currentY - this.startY;
      const pixelsPerRem = parseFloat(getComputedStyle(document.documentElement).fontSize);
      const numberOfActions = this.actions.length;
      const initialOffsetInPixels = 3 * (numberOfActions - 1) * pixelsPerRem;
      const newY = this.clamp(this.actionBarStartY + deltaY, 0, initialOffsetInPixels);

      this.lockedOpen = (newY < initialOffsetInPixels / 2);

      const actionBar = document.getElementsByClassName("actionbar")[0];
      actionBar.style.transform = "translateY(" + newY + "px)";
    },
    actionBarTouchEnd: function (e) {
      console.log('actionBarTouchEnd');

      if (!this.moving) return;
      this.moving = false;
      this.actionBarTouchInProgress = false;
      this.$emit('set-actionbar-open', this.lockedOpen);
      this.moveActionBar();
    },
    moveActionBar: function (forceRetract=false) {
      let endframePosition = 0;
      if (!this.lockedOpen || forceRetract) {
        const numberOfActions = this.actions.length;
        const initialOffsetInRem = 3 * (numberOfActions - 1);
        endframePosition = initialOffsetInRem;
      }
      this.moveActionBarToOffset(endframePosition);
    },
    moveActionBarToOffset: function (offset) {
      const actionBar = document.getElementsByClassName("actionbar")[0];
      const frames = [
        { transform: actionBar.style.transform },
        { transform: 'translateY(' + offset + 'rem)' }
      ]
      const options = {
        easing: 'cubic-bezier(0, 0, 0.31, 1)',
        duration: 100
      }
      actionBar
        .animate(frames, options)
        .addEventListener('finish', function () {
          actionBar.style.transform = 'translateY(' + offset + 'rem)';
        }
      );
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
