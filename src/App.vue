<template>
  <div :class="isMobile ? 'mobile' : 'tablet'">
    <div class="app-container">
      <navbar />
      <annotation />
      <specs />
      <connectors />
      <firmware />
      <opensource/>
      <div class="viewer-container">
        <dviewer />
      </div>
    </div>
  </div>
</template>

<script>
import { isMobileOnly } from "mobile-device-detect";
import dviewer from "./components/3dviewer";
import navbar from "./components/navbar";
import annotation from "./components/annotation";
import specs from "./components/specs";
import connectors from "./components/connectors";
import firmware from "./components/firmware";
import opensource from "./components/open-source";

export default {
  components: { navbar, dviewer, annotation, specs, connectors, firmware, opensource },
  data() {
    return {
      isMobile: isMobileOnly,
    };
  },
  name: "App",
  beforeCreate() {},
};
</script>

<style>
html,
body,
#app {
  margin: 0;
  padding: 0;
  width: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", sans-serif;
  font-size: 1.1em;
}

.viewer-container {
  width: 100%;
  height: 50vw;
}

.mobile .viewer-container {
  width: 100%;
  height: 100vw;
}

.app-container {
  background: white;
}

.tablet .app-container {
  width: 70%;
  margin: 20px auto;
  border-radius: 20px;
  box-shadow: 0px 0px 10px 7px rgba(34, 60, 80, 0.15);
}

.mobile .app-container {
  width: 100%;
}

html {
  background-image: url("/wallpapers.svg");
  background-position: center;
  background-size: 200px;
  animation: wallpaper_move 10s linear infinite;
}

@keyframes wallpaper_move {
  from {
    background-position-x: 0px;
    background-position-y: 0px;
  }

  to {
    background-position-x: 200px;
    background-position-y: -200px;
  }
}
</style>
