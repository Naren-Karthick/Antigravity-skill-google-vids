# Google Vids Workflow Reference

Google Vids is the primary editor. Treat this document as an operational guide, not a guarantee that every control is available in every account or rollout. Inspect the live UI and follow the controls currently offered.

## Start a project
1. Open Google Vids using the user's authenticated browser session.
2. Confirm the intended account and whether to create a new project or continue an existing one.
3. Choose a blank project for custom multi-scene production unless a template or Docs/Slides conversion better fits.
4. Set the required aspect ratio before creating scenes.
5. Name the project and verify it is saved.

## Choose the production path
- Custom animated story / explainer: establish a visual bible and reference images, then generate or import scene clips.
- Slide/diagram explainer: use shapes, charts, tables, images, and object animation where appropriate.
- Presenter-led content: use a presenter/avatar only when requested or useful.
- Screen tutorial: record the screen and narration, then edit for clarity.
- Existing document or slide deck: consider native conversion if available and inspect the generated result before accepting it.

## Generate assets
1. Pilot one representative scene.
2. Confirm current model controls, available duration, resolution, reference-image support, and insertion behavior.
3. Generate small batches and verify each result.
4. Import external assets only for a specific native capability gap.
5. Keep a manifest mapping each asset to its scene.


## Quota preflight and local fallback

Before creating AI video clips, inspect the live Google Vids UI/account for a quota counter, remaining-use indicator, disabled generation control, plan eligibility notice, or quota error. Record only what the account actually displays. Do not estimate remaining quota from the current project's clip count.

- If Vids quota is available, create and verify a pilot clip, then continue in small batches.
- If Vids quota is exhausted or the generator returns a limit error, stop retrying it and switch to the free local production pipeline in `free-local-production-fallback.md`.
- The local fallback uses Remotion first (only when the user's current license eligibility permits it), then Motion Canvas, Manim, HTML/CSS/SVG/Canvas, or Blender as appropriate.
- Generate narration with a suitable free local TTS engine, checking the exact model/voice license. Use FFmpeg for final rendering/concatenation, audio mixing, captions, muxing, and validation.
- Do not use Google Flow or paid cloud generation/TTS/stock services as an automatic fallback. Ask before any paid action.
- If the local environment cannot support the selected renderer or TTS voice, report the exact blocker and offer a simpler local animation or user-provided assets/voiceover.

Google Vids may still be used for optional finishing only if the required features remain available without extra quota or cost. Otherwise complete the MP4 locally. See the full fallback reference for setup, tool selection, licensing, audio workflow, and QA.

## Edit and preview
- Arrange scenes in storyboard order.
- Match scene durations to measured narration and visual beats.
- Use transitions and animation consistently, not decoratively.
- Check text and captions at the final aspect ratio.
- Preview the entire video before export.

## Export
Use the export format and resolution actually available in the UI. Prefer MP4 for standard video delivery. Wait for explicit completion, then verify the downloaded file and playback independently.

## Live UI rule
Menu names, model names, clip limits, export options, and rollout availability can change. Do not rely on stale screenshots or hard-coded coordinates. Inspect the live interface before each operation and report unavailable controls accurately.
