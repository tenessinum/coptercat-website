<template>
  <div class="open-source">
    <div class="bold">{{ $t("open-source") }}</div>
    <div>
      {{ $t("os.1") }}
      <a href="https://github.com/matveylapin/CopterCat_cm4">{{
        $t("os.2")
      }}</a>
      {{ $t("os.3") }}
    </div>
    <div>
      {{ $t("os.4") }}
      <a
        href="https://github.com/matveylapin/CopterCat_cm4/tree/main/gerbers/"
        >{{ $t("os.5") }}</a
      >
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.open-source {
  padding: 10px;
}
</style>