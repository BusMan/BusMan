<template>
<div class="actionbar" @click=click @touchstart="touchstart" @touchmove="touchmove" @touchend="touchend">
  <div v-for="action in actions" class="action" :data-action="action.id">
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
  methods: {
    touchstart: function(e) {
      console.log('touchstart');
      const actionBar = document.getElementsByClassName("actionbar")[0];

      this.currentY = e.touches[0].clientY;
      this.startY = this.currentY;
      this.actionBarStartY = parseFloat(getComputedStyle(actionBar).transform.replace(/.*, /g, '').replace(')', ''));
      this.lockedOpen = false;
    },
    touchmove: function(e) {
      console.log('touchmove');
      const actionBar = document.getElementsByClassName("actionbar")[0];

      this.moving = true;
      this.currentY = e.touches[0].clientY;

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
    touchend: function(e) {
      console.log('touchend');
      const actionBar = document.getElementsByClassName("actionbar")[0];

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
            .addEventListener('finish', function() {
              actionBar.style.transform = 'translateY(6rem)';
            }
          );
        }
      }
      this.moving = false;
    },
    click: function(e) {
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
    }
  }
}
</script>
