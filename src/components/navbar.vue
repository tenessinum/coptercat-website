<template>
  <div class="navbar">
    <img :src="require('@/assets/icons/logo.svg')" alt="" />
    <div style="display: flex; flex-direction: row; gap: 10px">
      <div>{{ $t("lang") }}</div>
      <select v-model="$i18n.locale">
        <option
          v-for="(lang, i) in ['ru', 'en']"
          :key="`Lang${i}`"
          :value="lang"
        >
          {{ lang }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  name: "navbar",
};
</script>

<style>
.navbar {
  width: calc(100% - 40px);
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 40px;
}

.navbar > img {
  height: 100%;
}
</style>