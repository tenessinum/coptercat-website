<template>
  <div class="specs">
    <div class="bold" style="margin-bottom: 20px">{{ $t("specs") }}</div>
    <div class="nav-choose">
      <div v-for="(c, i) in choses" :key="i">
        <div @click="chosen = c" :class="c === chosen ? 'chosen' : ''">
          {{ $t(c) }}
        </div>
      </div>
    </div>
    <div>
      <ul>
        <li v-for="i in samples[choses.indexOf(chosen)]" :key="i">
          {{ $t(chosen + "-lines." + i) }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "specs",
  data() {
    return {
      chosen: "fmu",
      choses: ["fmu", "rpi", "esp", "misc"],
      samples: [5, 6, 4, 7],
    };
  },
};
</script>

<style>
.specs {
  padding: 10px;
}

.chosen {
  background: #aaaaaa;
  color: white;
  transition: 0.5s;
  border-radius: 5px;
}

.nav-choose > div > div {
  cursor: pointer;
  padding: 5px;
}

.nav-choose {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
</style>