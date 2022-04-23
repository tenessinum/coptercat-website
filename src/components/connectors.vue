<template>
  <div class="connectors">
    <div class="bold" style="margin-bottom: 20px">{{ $t("connectors") }}</div>
    <div class="img-view" v-if="front">
      <img :src="require('@/assets/board_top_nums.png')" alt="" />
      <div>
        <ol>
          <li v-for="i in 5" :key="i">{{ $t("connectors-front." + i) }}</li>
        </ol>
        <button @click="front = !front">{{ $t("rotate") }}</button>
      </div>
    </div>
    <div class="img-view" v-else>
      <img :src="require('@/assets/board_bottom_nums.png')" alt="" />
      <div>
        <ol start="6">
          <li v-for="i in 14" :key="i">
            {{ $t("connectors-bottom." + (i + 5)) }}
          </li>
        </ol>
        <button @click="front = !front">{{ $t("rotate") }}</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      front: true,
    };
  },
};
</script>

<style>
.connectors {
  padding: 10px;
}

.img-view {
  display: flex;
  flex-direction: row;
}

.mobile .img-view {
  flex-direction: column;
}

.mobile .img-view > img {
  width: 100%;
}

.img-view > img {
  width: 50%;
  height: fit-content;
}

.img-view button {
    border: none;
    font-size: 1.1em;
    margin: 20px;
    margin-top: 10px;
}
</style>