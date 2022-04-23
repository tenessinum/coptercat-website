<template>
  <div class="firmware">
    <div class="bold" style="margin-bottom: 20px">{{ $t("firmware") }}</div>
    <div class="nav-choose">
      <div v-for="(c, i) in choses" :key="i">
        <div @click="chosen = c" :class="c === chosen ? 'chosen' : ''">
          {{ $t(c) }}
        </div>
      </div>
    </div>
    <div v-if="chosen === 'fmu'">
      <div>
        {{ $t("fmu-firmware.1") }}
        <a
          href="https://docs.px4.io/master/en/software_update/stm32_bootloader.html#stm32-bootloader"
          >{{ $t("fmu-firmware.10") }}</a
        >
      </div>
      <div>{{ $t("fmu-firmware.2") }}</div>
      <ol>
        <li>{{ $t("fmu-firmware.3") }}</li>
        <li>{{ $t("fmu-firmware.4") }}</li>
        <li>{{ $t("fmu-firmware.5") }}</li>
      </ol>
      <div>{{ $t("fmu-firmware.6") }}</div>
      <ol>
        <li>{{ $t("fmu-firmware.7") }}</li>
        <li>{{ $t("fmu-firmware.8") }}</li>
        <li>{{ $t("fmu-firmware.9") }}</li>
      </ol>
    </div>
    <div v-else-if="chosen === 'esp'">
      <div>{{ $t("esp-firmware.1") }}</div>
      <div>{{ $t("esp-firmware.2") }}</div>
      <ol>
        <li>{{ $t("esp-firmware.3") }}</li>
        <li>{{ $t("esp-firmware.4") }}</li>
        <li>{{ $t("esp-firmware.5") }}</li>
      </ol>
      <div>{{ $t("esp-firmware.6") }}</div>
      <ol>
        <li>{{ $t("esp-firmware.7") }}</li>
        <li>{{ $t("esp-firmware.8") }}</li>
        <li>{{ $t("esp-firmware.9") }}</li>
        <li>{{ $t("esp-firmware.10") }}</li>
        <li>{{ $t("esp-firmware.11") }}</li>
      </ol>
    </div>
    <div v-else-if="chosen === 'rpi'">
      <div>{{ $t("rpi-firmware.1") }} (<a
          href="https://www.jeffgeerling.com/blog/2020/how-flash-raspberry-pi-os-compute-module-4-emmc-usbboot"
          >{{ $t("rpi-firmware.2") }}</a
        >)</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      chosen: "fmu",
      choses: ["fmu", "rpi", "esp"],
    };
  },
};
</script>

<style>
.firmware {
  padding: 10px;
}
</style>