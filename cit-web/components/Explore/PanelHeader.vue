<template>
  <v-expansion-panel-header class="pa-5 ma-0 panel-header">
    <span class="mr-4 text-subtitle-1">{{ title }}</span>
    <v-spacer></v-spacer>
    <v-sheet
      color="#2176d2"
      class="white--text mr-2 length-button elevation-0 font-weight-bold d-flex justify-center align-center rounded-circle"
      width="40"
      height="40"
      >{{ length }}</v-sheet
    >
  </v-expansion-panel-header>
</template>

<script>
import { Component, Vue, Prop } from 'nuxt-property-decorator'
import BaseList from '~/components/Explore/BaseList.vue'
@Component({
  BaseList,
})
export default class Explore extends Vue {
  @Prop({ default: null, type: String }) title
  @Prop({ default: null, type: Number }) length
}
</script>
<style lang="scss" scoped>
.length-button {
  flex: none !important;
}
</style>
