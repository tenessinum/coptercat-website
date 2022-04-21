<template>
  <viewer3d></viewer3d>
</template>

<script>
import viewer3d from "@/components/3dviewer";

export default {
  name: "App",
  components: {
    viewer3d,
  },
};
</script>

<style>
html,
body, #app {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", sans-serif;
}
</style>
