<template>
  <div id="canvas_container"></div>
</template>

<script>
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
import { ThreeMFLoader } from "three/examples/jsm/loaders/3MFLoader";
import { SVGLoader } from "three/examples/jsm/loaders/SVGLoader";

export default {
  name: "3dviewer",
  data() {
    return {
      width: 500,
      height: 500,
    };
  },
  mounted() {
    let scene = new THREE.Scene();

    let camera = new THREE.PerspectiveCamera(
      45,
      this.width / this.height,
      1,
      10000
    );
    scene.add(camera);

    let renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.setSize(this.width, this.height);
    document.getElementById("canvas_container").innerHTML = "";

    new ResizeObserver((e) => {
      renderer.setSize(e[0].target.clientWidth, e[0].target.clientHeight);
      this.width = e[0].target.clientWidth;
      this.height = e[0].target.clientHeight;
      camera.aspect = this.width / this.height;
      camera.updateProjectionMatrix();
      camera.updateMatrixWorld();
    }).observe(document.getElementById("canvas_container"));
    renderer.setClearColor(0xbbbbbb, 1);
    let controls = new OrbitControls(camera, renderer.domElement);
    camera.position.set(0, 0, 100);
    camera.lookAt(0, 0, 0);
    controls.update();

    const _fronts = [
      { file: "faces/Front.svg", color: 0x666666 },
    ];

    function loadFronts(fronts, offset) {
      if (fronts.length === 0) return;

      let floader = new SVGLoader();
      floader.load(
        fronts[0].file,
        function (data) {
          let paths = data.paths;
          let group = new THREE.Group();

          for (let i = 0; i < paths.length; i++) {
            let path = paths[i];
            let material = new THREE.MeshPhysicalMaterial({
              color: fronts[0].color,
              side: THREE.DoubleSide,
            });

            let shapes = SVGLoader.createShapes(path);

            for (let j = 0; j < shapes.length; j++) {
              let shape = shapes[j];
              let geometry = new THREE.ShapeGeometry(shape);
              let mesh = new THREE.Mesh(geometry, material);
              group.add(mesh);
            }
          }
          group.scale.multiplyScalar(0.000001);
          group.position.x -= 19.25 + 2.45;
          group.position.y += 25.2 + 3.17;
          group.position.z += 4.7 + offset;
          group.rotation.z = Math.PI;
          group.rotation.y = Math.PI;

          scene.add(group);
          loadFronts(fronts.slice(1), offset + 0.1);
        }
      );
    }

    let loader = new ThreeMFLoader().setPath("models/");
    loader.load("model.3mf", function (object) {
      object.position.x -= 227;
      object.position.y += 107;

      scene.add(object);
      loadFronts(_fronts, 0);
    });

    document
      .getElementById("canvas_container")
      .appendChild(renderer.domElement);

    let lights = [];
    for (let i = 0; i < 6; i++) {
      lights.push(new THREE.DirectionalLight(0xffffff, 1));
    }

    lights[0].position.set(10, 0, 0);
    lights[1].position.set(-10, 0, 0);
    lights[2].position.set(0, 10, 0);
    lights[3].position.set(0, -10, 0);
    lights[4].position.set(0, 0, 10);
    lights[5].position.set(0, 0, -10);

    for (let i = 0; i < 6; i++) {
      scene.add(lights[i]);
    }
    renderer.setAnimationLoop(() => {
      controls.update();
      renderer.render(scene, camera);
    });
  },
};
</script>

<style>
#canvas_container {
  height: 100%;
  color: #0b200b;
}
</style>