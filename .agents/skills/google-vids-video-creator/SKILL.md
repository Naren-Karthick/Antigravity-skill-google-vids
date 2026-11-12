---
name: google-vids-video-creator
description: >-
  End-to-end, resumable video production from a topic or brief to a verified
  exported MP4. Researches, scripts, storyboards, generates visuals and audio,
  edits in Google Vids, uses external tools only when needed, performs quality
  checks, and reports verified completion. Use for complete videos, explainers,
  animated stories, YouTube videos, Shorts, and social videos.
---

# Google Vids Video Creator

## Mission

Turn a topic, title, brief, or supplied script into a complete, polished, exported video. Google Vids is the primary editor. Use external tools only for a specific capability gap, a failed operation, or a measurable quality improvement.

**Never equate a planned action with a completed action.** Verify each important state change in the UI or with a file/media inspection. Never claim an export exists or plays unless verified.

## Operating principles

1. **Plan before operating.** Research, define audience, platform, aspect ratio, runtime, narration, scenes, assets, and acceptance criteria before opening the editor.
2. **Voiceover-first when narration-led.** Finalize narration and measure its duration before setting scene durations or generating clips. For non-narrated montage/music videos, plan to the soundtrack instead.
3. **Build in small batches.** Create and verify a few scenes at a time; avoid launching many expensive generations before confirming the workflow works.
4. **Persist progress.** Maintain a production manifest outside the transient chat/browser context. Update it after each completed milestone and scene.
5. **Use observed UI, not remembered coordinates.** Inspect the current page before acting. Prefer labels, accessible names, DOM/UI semantics, and stable selectors over coordinates. If only visual control is available, take a fresh screenshot after navigation or layout changes.
6. **Verify actions.** After every meaningful click, upload, generation, insertion, timeline edit, or export, inspect the resulting state before continuing.
7. **Recover safely.** Retry only after checking whether the previous operation succeeded. Avoid duplicate scenes, uploads, tracks, and exports.
8. **Respect user assets and account boundaries.** Do not delete or overwrite user media/projects without explicit permission. Never request passwords or bypass authentication, access controls, paywalls, or safety restrictions.
9. **Be cost-aware.** Prefer reuse, image-to-video/animate, trim, extend, and modest speed adjustments over regenerating a satisfactory asset. Confirm before paid services, purchases, or actions with material cost.
10. **Report honestly.** Distinguish completed, partially completed, blocked, and unverified steps.

## Phase 0 — Intake and production brief

Read the user's request and supplied files. Do not ask for details that can be safely defaulted. Ask only when a missing choice materially changes the deliverable (for example, language, audience, or a required identity/brand asset).

Create a brief containing:

- Working title and one-sentence promise
- Audience, language, tone, and content format
- Platform and aspect ratio: default 16:9 for standard YouTube/explainers; 9:16 for Shorts/Reels/TikTok; use explicit user preference
- Target runtime and resolution; never promise a resolution unavailable in the account
- Narration: yes/no, voice/language/accent if known
- Visual style, recurring characters, reference assets, and continuity rules
- Music/SFX/caption requirements
- Export destination and filename
- Acceptance criteria and any user approval gates

For an unspecified full video, use sensible defaults and state them in the plan before production. Do not pause for approval unless the brief involves sensitive claims, personal likeness/voice cloning, paid actions, or another consequential choice.

## Phase 1 — Research and script

When the user provides only a topic/title, research before writing. Prefer primary sources for factual, scientific, medical, legal, financial, or current claims. Cross-check important claims; distinguish established facts from speculation and hypothetical storytelling. Record source URLs and research date in the production notes.

Write:
- Hook and narrative arc
- Complete spoken narration, with pronunciation notes where needed
- Scene-by-scene script and visual intent
- On-screen text (short, legible, correctly spelled)
- Music mood and timed SFX cues
- Closing takeaway/CTA where appropriate

Do not fabricate citations, statistics, quotations, or scientific certainty. For "what if" content, label speculative consequences clearly and avoid presenting imagined events as established fact.

## Phase 2 — Storyboard and timing

Create a scene table with:
- Scene ID and purpose
- Narration text
- Estimated narration duration
- Visual prompt (subject, action, environment, composition, camera, lighting, style)
- Character/reference assets
- On-screen text
- Music/SFX cue
- Transition and continuity notes
- Target scene duration and generation method

Estimate narration duration from measured audio whenever possible. If only text is available, use a configurable estimate (roughly 130–160 spoken words/minute for conversational English) and revise after audio generation.

Keep each generated clip within the duration controls actually visible in Google Vids. Do not hardcode model limits: inspect current controls and the selected model. Split long beats into coherent shots; use Extend only when continuity matters and the feature is available.

## Phase 3 — Production manifest and resume state

Create a project folder where supported, otherwise use a dedicated working directory. Keep:
- `production-plan.md`
- `scene-breakdown.csv` or `scene-breakdown.md`
- `manifest.json`
- generated voiceover, images, clips, music, SFX, captions, and export files
- `qa-report.md`

Manifest requirements:
- Project title, created/updated timestamps, target specs
- Google Vids project URL/name if available
- Current phase and last verified checkpoint
- Scene IDs with statuses: planned, narration_ready, visual_ready, inserted, reviewed
- Asset filenames/locations, durations, aspect ratios, and generation notes
- Retry count and last error
- Export path, file size, duration, codec/metadata, and playback-check status

Before resuming, read the manifest and inspect the actual Google Vids project. Reconcile the manifest against reality; the UI is authoritative for editor state and filesystem inspection is authoritative for local files. Never repeat a completed expensive generation unless the asset is missing, unusable, or the user requests it.

## Prerequisites and browser delegation

1. Delegate Google Vids UI work to the available browser subagent/tool. Keep the same browser session alive across phases when possible.
2. Use the actual browser-control interface available in the environment; do not invent tool names or assume a browser subagent exists.
3. Navigate to https://vids.google.com/ and inspect the current page.
4. If authentication, permission, Workspace policy, or a user-controlled consent step is required, pause and ask the user to complete it. Resume from the last verified checkpoint.
5. If browser attachment fails, report the exact blocker and provide the minimum user action needed. Do not repeatedly restart the browser or silently switch to an unrelated profile.

## Phase 4 — Google Vids project setup

1. Start a new project or use an existing project only when the user asked to continue it.
2. Choose Blank vid for custom multi-scene work unless Docs/Slides conversion or a suitable template is clearly faster.
3. Set aspect ratio at the start and verify it.
4. Name the project clearly.
5. Create the planned scenes in a small batch.
6. Save/confirm project state before expensive generation.

UI labels and feature availability can change. Follow the current visible UI; use the reference guide as a hint, not an authority over the live interface.

## Phase 5 — Visual consistency and generation

1. Establish a visual bible: style, palette, character design, environment, camera language, lighting, and exclusions.
2. Generate a clean reference image/sheet when recurring characters or a repeated visual identity are required. Inspect it; do not place a contact sheet/reference sheet on the final canvas unless intended.
3. Reuse the same reference/ingredient images where supported. Confirm the selected reference is attached to each relevant generation.
4. Prompt each shot with a concrete action and beginning/middle/end state, plus camera movement, composition, environment, lighting, aspect ratio, and style.
5. Include exclusions only where useful (e.g. no unwanted text, logos, watermarks, malformed hands). Avoid overloading prompts with contradictory constraints.
6. Generate a pilot scene first. Verify visual quality, duration, aspect ratio, character consistency, and insertion behavior before batch production.
7. Generate in small batches; after each batch verify clip creation, insertion, ordering, and manifest update.
8. If generation fails, inspect job status and project state before retrying. Use bounded retries (normally up to 2 attempts per asset), vary the prompt or method only when diagnosing a specific failure.
9. If Google Vids cannot produce a required asset, use an external generator only for that asset, then import it into Google Vids. Record the tool and asset provenance.

## Phase 6 — Narration and audio

For narration-led videos:
1. Select a suitable voice and keep it consistent unless multiple speakers are intentional.
2. Generate narration per scene or as one continuous track, depending on available controls and synchronization needs.
3. Measure actual audio duration; do not rely only on word-count estimates.
4. Check pronunciation, pacing, pauses, clipping, and language.
5. If native voiceover is inadequate, consider an external TTS tool (for example, ElevenLabs) only if available and authorized. Do not clone a real person's voice without explicit consent and appropriate rights.
6. Keep narration intelligible above music and SFX. Use instrumental music under speech unless vocals are intentional.
7. Mute generated clip audio when it conflicts with dedicated narration/music. Preserve native audio only when it is intentionally part of the mix.
8. Align SFX to visible actions; avoid unnecessary sound effects.

Do not upload private scripts, voice samples, or media to external services without user authorization and a clear need.

## Phase 7 — Timeline editing and polish

1. Place scenes in the storyboard order and verify no missing or duplicate scenes.
2. Fit each clip to the narration/action beat. Prefer trim, extend, or a small speed adjustment when it preserves quality; do not make motion unnaturally fast/slow.
3. Ensure voiceover does not get cut at scene boundaries. Use intentional overlaps only when supported and appropriate.
4. Add transitions sparingly; avoid transitions that slow the story or introduce gaps.
5. Add captions/subtitles when requested or clearly useful. Review transcription against the actual narration; correct names, numbers, punctuation, and line breaks.
6. Keep text within platform-safe areas and readable on mobile.
7. Balance music and SFX below narration; inspect loudness by listening, not just track placement.
8. Use consistent typography, color, framing, and pacing.
9. Preview the complete video from beginning to end, not only individual scenes.

## Phase 8 — External-tool decision policy

Google Vids remains the primary editor. Use external tools only when all of these are true:
- A concrete capability gap or quality issue has been identified.
- The external tool is available and authorized.
- The benefit outweighs extra upload, cost, privacy, and workflow complexity.
- The resulting asset can be brought back into Google Vids or used for a clearly stated post-export task.

Examples:
- FFmpeg: inspect media metadata/duration, normalize or trim audio, create proxies, validate playback, or perform a requested post-export conversion. Never use it to bypass a Google Vids restriction.
- External TTS: voice quality/language control when native narration is inadequate.
- External image/video generation: a specific visual the native generator cannot achieve.
- Descript or another editor: only when the requested editing operation is unavailable in Google Vids and the user has authorized the external workflow.

Do not assume a tool is installed. Check availability before invoking it. Do not send account credentials, private assets, or copyrighted source media to a third party without permission.

## Phase 9 — Quality assurance

Use the checklist in `templates/quality-checklist.md`. At minimum verify:
- Correct runtime, aspect ratio, orientation, and resolution
- All scenes present, in order, and visually coherent
- No black/blank frames, placeholders, accidental duplicate clips, or abrupt gaps
- Narration complete, intelligible, correctly pronounced, and synchronized
- Music/SFX balanced and not clipping
- Captions accurate, readable, and safe-positioned
- Titles, spelling, names, and factual statements checked
- Start and ending feel intentional
- Export file exists, is non-zero, and can be opened/played
- Playback spot-check includes opening, middle, scene transitions, and ending; full playback when practical

If a check cannot be performed, mark it **not verified** rather than passing it.

## Phase 10 — Export and delivery

1. Export using a format and quality actually offered by the current UI. Prefer MP4 for standard video delivery.
2. Wait for rendering and download completion; do not infer completion from a closed dialog.
3. Confirm the exact output file path exists and has non-zero size.
4. Inspect metadata with an available media tool (FFprobe/FFmpeg if installed); verify duration and dimensions against target.
5. Play the file or perform a supported playback check. If unavailable, disclose that limitation.
6. Preserve the editable Google Vids project and source assets when possible.
7. Deliver the exact file path/link only when verified. Include the Google Vids project link if available.

## Final report

Provide:
- Video title, format, aspect ratio, resolution, and verified duration
- Google Vids project link (if available)
- Export file and verification results
- Number of scenes and assets generated
- External tools used and why
- QA results, limitations, and anything requiring user action

Use clear status labels: **Verified**, **Partially verified**, **Blocked**, **Not verified**.

## References

Load only the relevant reference for the current phase:
- [Google Vids UI capabilities and prompt patterns](./references/ui-and-prompt-patterns.md)
- [Full production workflow](./workflows/full-video-production.md)
- [Browser automation rules](./references/browser-automation.md)
- [Audio production](./references/audio-production.md)
- [Recovery and resume](./workflows/recovery-workflow.md)
- [Quality checklist](./templates/quality-checklist.md)
