<template>
  <div class="annotation">
    <div class="bold">{{ $t("project_description_title") }}</div>
    <div>{{ $t("project_description") }}</div>
    <hr />
    <div class="bold">{{ $t("idea_title") }}</div>
    <div>{{ $t("idea") }}</div>
    <hr />
    <div class="bold">{{ $t("perspective_title") }}</div>
    <div>{{ $t("perspective") }}</div>
  </div>
</template>

<script>
export default {
  name: "annotation",
};
</script>

<style>
.annotation {
  padding: 10px;
}

.bold {
  font-weight: bold;
}
</style>