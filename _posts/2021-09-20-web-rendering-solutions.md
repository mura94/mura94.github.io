---
layout: post
title: Web Rendering Solutions
subtitle: Tools for rendering 3D objects and environments on common web browsers.
tags: [AR, Web, Rendering, WebXR, WebAR, GLTF, USDZ, 3D]
thumbnail-img: assets/img/damaged-helmet.png
---

I've recently been looking into web-based, (somewhat) lightweight 3D rendering tools, and I've been pleasantly surprised by what is out there!

Here are some neat ones to check out:

- [`<model-viewer>`](https://modelviewer.dev/)
  - Great for cross-platform AR and generic GLTF model rendering
  - Alternative to Apple Quick Look, which is Safari-only. Also includes an option to open Quick Look (.usdz/.reality) files for iOS users
  - Neat web-based editor
  - See a quick example [here](https://blakejarvis.design/modelViewer)
    - Not supported by some browsers it seems (I've found that msft edge only works here on some PC's)
- [filament](https://github.com/google/filament)
  - Takes a bit of setup, but following a few tutorials can get you something like [this](https://blakejarvis.design/suzanne) which is surprisingly high res with good performance even on mobile.
- [LGL Tracer Renderer](https://lgltracer.com/)
  - I *just* saw this one and am amazed by the results. It's way less performant than the others, but just try it and see the quality of path tracing on the web!
- [Apple Quick Look](https://developer.apple.com/augmented-reality/quick-look/)
  - Only for Safari on compatible iOS devices
  - Reality Composer is a neat tool for really quick AR experience setup, but is a bit buggy and missing key functionality for extensive use
  - Convert basic GLTF models to USDZ with [this handy web tool](https://spase.io/playground)
- [SketchFab 3D Viewer](https://sketchfab.com/3d-viewer)
  - Haven't tried this yet but will do soon
- [GLTF Sample Viewer](https://github.khronos.org/glTF-Sample-Viewer-Release/)
  - Made by the folks who design the GLTF format
  - Mostly for dev purposes it seems
- [Three.js](https://threejs.org/)
  - Requires some know-how and custom setup for your own purposes
  - Incredibly deep rendering potential
  - [Web editor](https://threejs.org/editor/)
  - Quick example [here](https://blakejarvis.design/threejs)
  - Tonnnns of cool examples found [here](https://threejs.org/examples/#webgl_animation_cloth)
