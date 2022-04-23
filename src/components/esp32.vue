<template>
  <div class="esp32">
    <div class="bold">{{ $t("about-esp") }}</div>
    <div>
      {{ $t("more-esp.1") }}
    </div>
    <div>
      {{ $t("more-esp.2") }}
      <a href="https://gitlab.com/painlessMesh/painlessMesh">painlessMesh</a>
      {{ $t("more-esp.3") }}
      <a href="http://wiki.ros.org/rosserial">rosserial</a>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.esp32 {
  padding: 10px;
}
</style>