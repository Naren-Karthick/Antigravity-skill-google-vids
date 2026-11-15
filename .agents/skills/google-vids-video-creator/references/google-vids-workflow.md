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


## Quota preflight and Google Flow fallback

Before creating AI video clips, inspect the live Google Vids UI/account for a quota counter, remaining-use indicator, disabled generation control, plan eligibility notice, or quota error. Limits vary by account and can change, so do not rely on a fixed number from this reference. Record only what the account actually displays. Do not estimate remaining quota from the current project's clip count.

If Vids quota is exhausted or the generator returns a limit error, switch clip generation to Google Flow rather than retrying Vids repeatedly:

1. Open the official Google Flow experience in the same authenticated browser profile: https://labs.google/fx/tools/flow.
2. Check the profile menu for remaining Flow/AI credits. Check the prompt/settings panel for the selected model's current credit cost. Both balances and costs are subject to change.
3. Generate a pilot clip, then create the remaining clips in small batches only while credits, account eligibility, and rate limits permit.
4. Download the completed Flow clips and import them into the existing Google Vids project. Finish editing and export in Google Vids.
5. If Flow has insufficient credits or requires a paid plan/upgrade, stop and ask before any purchase. If Flow is unavailable, report the blocker and use suitable non-generative visuals in Vids only if they meet the brief.
6. Check whether the exported Flow clips carry a visible watermark and report it. Do not remove required provenance marks.

Google Flow is a fallback generator, not an unlimited quota bypass. Respect both products' account limits, regional availability, safety rules, and paid-action boundaries.

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
