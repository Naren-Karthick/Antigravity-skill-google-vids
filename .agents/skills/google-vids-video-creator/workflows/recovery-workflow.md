# Recovery and Resume Workflow

## Before resuming
1. Read `manifest.json`, production plan, scene breakdown, and QA notes.
2. Open the existing Google Vids project link from the manifest.
3. Inspect current project state and compare it with recorded statuses.
4. Treat the editor and actual files as authoritative; reconcile stale manifest entries.

## Status model
- `planned`: no asset exists.
- `narration_ready`: narration asset generated and verified.
- `visual_ready`: visual asset generated and verified.
- `inserted`: assets placed in the intended scene and timeline.
- `reviewed`: scene preview checked for timing, visuals, and audio.
- `blocked`: cannot proceed without user action or missing capability.

## Failure handling
- First inspect whether the operation completed despite a timeout or lost response.
- If complete, update manifest; do not repeat.
- If incomplete, identify the failure class: authentication, network, quota, generation, upload, timeline, export, or local file.
- Retry at most twice for a transient asset-generation failure. Change one prompt parameter at a time to isolate the cause. For local rendering, inspect logs and output files before retrying; reuse completed scene renders.
- For Google Vids quota exhaustion, stop retrying Vids and switch to the free local fallback in `references/free-local-production-fallback.md`. Do not use Google Flow or paid generators automatically.
- For local-tool installation, license, hardware, or policy blockers, stop and explain the minimum user action; do not loop or incur costs.
- For a failed export, verify project integrity before exporting again.
- Never delete partial assets until the user authorizes cleanup.

## Resume
Continue from the first incomplete scene/checkpoint. Reuse completed assets. After recovery, update the manifest with the error, resolution, and new verified checkpoint.
