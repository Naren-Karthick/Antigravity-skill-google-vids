# Troubleshooting Guide

## General recovery rule
Before retrying, inspect the current project, asset list, timeline, and job state. A timeout does not prove the operation failed. Prevent duplicate assets and scenes.

## Common blockers

### Sign-in or permission prompt
Pause and ask the user to complete authentication or grant the required permission in their own browser. Never ask for passwords or one-time codes.

### Feature missing from the UI
Check the current account, project type, aspect ratio, and visible menus. Feature availability may depend on account, rollout, region, or Workspace policy. Do not invent a workaround that bypasses policy.

### Generation stalled or failed
Check whether a result was created despite the error. If not, simplify the prompt, reduce conflicting constraints, and retry within the bounded retry policy. Stop if a quota or policy limit is reached.

### Inconsistent characters or visual style
Re-check the approved reference image and character bible. Reuse the same references and reduce unnecessary changes in costume, camera, palette, and environment. Replace only affected scenes.

### Voiceover too long or too short
Measure the generated audio. Revise narration or adjust scene timing based on the measured duration. Do not force the voice track to fit by cutting words.

### Audio conflict
Inspect each clip's native audio and all dedicated tracks. Mute only conflicting source audio. Lower music/SFX relative to narration and listen to the result.

### Captions incorrect
Compare captions with the actual final voice track. Correct names, numbers, punctuation, and line breaks; regenerate only if manual correction is unavailable.

### Timeline gap or duplicate
Compare the timeline to the scene manifest. Remove or repair only clearly identified accidental duplicates/gaps. Do not delete ambiguous user assets.

### Export failure
Confirm the project still opens and previews. Check available storage, export settings, and visible error details. Retry only after determining whether an export file already exists.

### Download not found
Check the browser's actual download state and destination. Do not invent a path or claim completion. Ask the user to choose a location if the browser requires it.

## Escalation report
When blocked, report:
- Phase and last verified checkpoint
- Exact visible error or missing control
- Whether any asset/project change occurred
- Attempts already made
- Minimum user action needed
- Safe next step after the blocker is cleared
