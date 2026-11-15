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


## Phase 0A — Topic discovery and YouTube packaging

When the user asks for a topic, asks what to upload next, or gives a broad channel niche without a specific title, do not randomly invent a topic. Research current audience interest and recommend a topic with a clear viewer promise.

1. Identify the channel niche, intended audience, language, geography, channel format, and recent topics if visible or supplied. Do not assume access to private YouTube Analytics; inspect it only when the user has connected/signed in and the relevant page is available.
2. Research current search interest, recent news/events where relevant, YouTube autocomplete/search results, competing videos, and audience questions from credible public sources. Use current evidence and note the research date. Do not claim access to exact search volume or private trend metrics unless the interface explicitly shows them.
3. Build a shortlist of 5–10 topic ideas. Score each consistently (for example 1–5) for audience demand signals, curiosity/hook strength, novelty, relevance to the channel, visual storytelling potential, competition/differentiation, and production feasibility.
4. Recommend the strongest topic and explain the evidence and trade-offs briefly. Never promise that a topic, title, thumbnail, or upload time will go viral. Avoid misleading clickbait and unsupported trend claims.
5. For the chosen topic, create 3–5 title options with distinct angles (curiosity, benefit/explainer, emotional/story, search-friendly). Select one recommended title. Keep it accurate to the video's actual content and within the platform's current title constraints.
6. Build a thumbnail concept and generate a dedicated thumbnail image using an available image-generation tool. Default to 16:9 YouTube thumbnail framing (commonly 1280×720 output when supported). Use one dominant subject, strong readable contrast, a clear focal point, and very short text only when it adds value. Keep important elements inside safe margins; avoid tiny text, clutter, fake UI, misleading imagery, and unnecessary logos. Do not rely on text rendered inside image generation for exact spelling: generate clean composition and add/edit text in a design tool when needed. Inspect the final thumbnail at small/mobile size.
7. Prepare a complete publishing package:
   - Recommended title plus alternate titles
   - Thumbnail image and a short explanation of its visual hook
   - Search-friendly description with an opening hook, concise summary, useful keywords naturally integrated, source credits/references where needed, and CTA
   - Relevant YouTube tags (not keyword stuffing) and a small set of relevant hashtags
   - Chapters with timestamps only after the final edit/export duration is known
   - Pinned comment idea and optional community-post teaser
   - Category, audience/age suitability, language, and upload checklist when these can be determined
8. Check spelling, factual accuracy, source attribution, copyright and platform policy. Do not copy another creator's title/thumbnail/script. Do not add unrelated trending tags. Do not claim sponsorship, affiliation, or official endorsement.
9. Save the package in the project folder and include it in the final delivery. If the user only asked for ideas, stop before video production; otherwise continue automatically into the full production workflow.

If the user supplies a specific title, respect it as the working title. You may suggest stronger alternatives, but do not silently replace the user's chosen title.

## Phase 1 — Title-to-video research and script

**Title-only mode is a first-class workflow.** If the user gives only a video title (for example, "What If Humans Never Slept?" or "How Does an Array Work in C?"), treat that as sufficient authorization to begin the complete production pipeline. Do not ask the user to write a script, provide research, or fill in a long brief. Infer a sensible audience, format, tone, runtime, and visual approach from the title and the user's stated preferences; state those defaults in the production plan and proceed.

### Research workflow
1. Parse the title into the central question, key concepts, likely audience, and the promise the video must fulfil.
2. Search the web for trustworthy, relevant information before scripting. Use primary sources first: official documentation, research papers, government or university publications, standards bodies, and direct datasets. Use reputable secondary sources to add context and explain concepts.
3. For factual topics, verify important claims against at least two independent credible sources where practical; prioritize original/primary evidence when sources disagree. For current topics, check publication dates and whether the information is still current.
4. Build a compact research brief with: key findings, verified facts, useful examples, important caveats, disputed/uncertain points, source title/organization, URL, and research date. Keep source notes in the project folder and retain them for the final description or references slide when appropriate.
5. Separate fact, interpretation, prediction, and fiction. Never turn an estimate, correlation, hypothesis, or hypothetical scenario into a confirmed fact. For "what if" videos, establish the real-world baseline, then clearly frame imagined consequences as speculation.
6. Check all names, dates, numbers, units, definitions, code examples, and quotations. Do not invent citations, statistics, quotations, expert opinions, or scientific certainty. Quote sparingly and paraphrase in original language.
7. If reliable sources cannot confirm a claim, omit it, qualify it, or explicitly mark it as uncertain rather than guessing.

### Script package
Use the research brief to create:
- A compelling opening hook that quickly pays off the title's promise
- A logical narrative arc with clear explanations and smooth transitions
- Complete spoken narration, with pronunciation notes where needed
- Scene-by-scene script and visual intent
- Short, legible, correctly spelled on-screen text
- Music mood and timed SFX cues
- A meaningful conclusion and CTA where appropriate
- A source list for production notes and, where useful, the video description or end references

Adapt the script to the target runtime. Prefer clear, natural, speakable language over dense paragraphs. For educational/code videos, verify that explanations and code are correct and runnable where applicable.

Do not stop after delivering research or a script: continue into storyboard, asset generation, Google Vids editing, QA, and export unless the user explicitly asks for planning or a script only.

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


## Phase 4A — Check Google Vids generation quota and choose the video-generation engine

**Before generating any AI video clips, inspect the user's live Google Vids account and current UI for quota/limit status.** Do not assume a fixed monthly or daily allowance: limits, counters, eligible features, and reset rules vary by account type, subscription, Workspace policy, and product rollout.

1. Open the AI video generation panel and inspect any remaining-use counter, quota message, disabled control, plan notice, or usage-limit dialog. If the account exposes a usage/availability page, inspect it too.
2. Record what is actually visible in the production manifest: quota status (available, exhausted, unavailable, or unknown), any displayed remaining amount, reset date/time if shown, and the evidence observed.
3. Do not infer remaining quota from the number of clips created in this project. Usage may be shared across projects or other Google products, and the account may not expose a precise counter.
4. If Google Vids has usable quota, generate one pilot clip and verify it succeeds before continuing in small batches.
5. If Google Vids explicitly reports that its AI video-generation limit is exhausted, generation is blocked by quota, or the feature is unavailable for this account, switch the video-clip generation work to Google Flow. Do not repeatedly retry the exhausted Vids generator.
6. If the Vids quota cannot be determined from the UI, try one low-cost pilot only when the UI allows it. If the attempt returns a limit/quota error, switch to Flow. If there is no reliable way to check and no error is shown, mark the status unknown and proceed cautiously rather than claiming the quota is available.

### Google Flow fallback

- Open Google Flow in the same authenticated browser profile at https://labs.google/fx/tools/flow (or use the official Flow entry point shown in Google products). Confirm the correct Google account.
- Before generating, inspect the Flow profile area for remaining Flow/AI credits and inspect the current model/settings panel for the cost of the selected generation. Flow credits and model costs can change; never hard-code a credit allowance or assume Flow is unlimited.
- If Flow has enough available credits and the generation is permitted, generate the required scene clips there. Prefer the model/settings that best meet the storyboard and remaining-credit budget; create a pilot first, then proceed in small batches.
- If Flow also has insufficient credits, is rate-limited, unavailable in the user's region/account, or requires a paid upgrade/purchase, stop before spending money. Ask the user before any purchase, subscription change, or other paid action. Otherwise use non-generative Vids assets (images, diagrams, stock media, motion graphics) where they can meet the brief, or report the blocker.
- Verify each Flow generation completed and download/export the resulting clip. Keep scene IDs and filenames aligned with the storyboard and manifest.
- Import the downloaded Flow clips into the original Google Vids project. Google Vids remains the primary editor: arrange clips, add narration, captions, music, SFX, transitions, and titles there, then perform the normal QA and MP4 export.
- Check the output for any visible watermark, especially when the account or location may apply one. Do not attempt to remove or conceal required provenance marks; report them if present.
- Record which scenes were generated in Vids versus Flow, the selected model/settings, any displayed credit usage, import status, and any watermark or limitation in the manifest and final report.

**Important:** A Google Vids quota exhaustion is a trigger to use Flow for video-clip generation, not permission to bypass account restrictions. Respect Flow's own credits, rate limits, eligibility, regional availability, and safety controls.


## Visual style and character library

Choose the visual language that best serves the subject, audience, platform, and available generation tools. Do not force every video into one default look. Offer or infer a suitable style and record it in the visual bible.

Supported styles include:
- **2D animation:** flat/vector, hand-drawn, cut-out, motion-graphics, educational cartoon, comic-book, silhouette.
- **3D animation:** stylized 3D, family-friendly/cartoon 3D, realistic 3D, game-cinematic, clay/stop-motion look.
- **Stickman:** minimalist line characters, expressive poses, simple backgrounds and readable visual metaphors.
- **Anime/manga-inspired:** expressive stylized characters and cinematic compositions; use original designs rather than copying a living artist's distinctive style or a protected franchise character.
- **Realistic/cinematic:** live-action-like scenes, documentary reenactment, historical reconstruction, nature/science visualization.
- **Hybrid:** combine styles only with a clear reason and consistent art direction.

For each recurring character, create a character bible and (when supported) a clean reference sheet. Specify character ID, age range where relevant, silhouette, proportions, face, hair, skin/fur/material appearance, clothing, accessories, palette, expressions, movement, and immutable continuity traits. Reuse approved reference assets across scenes. Avoid accidental character drift, extra limbs, changing costumes, or inconsistent scale.

### Deities, sacred figures, and culturally specific depictions

When a video includes a god, goddess, deity, avatar, prophet, saint, sacred being, or figure from a living or historical religious tradition:

1. Identify the exact tradition, denomination/school, region, period, and source tradition relevant to the user's topic. Do not assume that depictions are universal across communities.
2. Research authoritative primary or community-respected sources, such as the relevant scripture/translation, temple or cultural institution material, museum collections, academic publications, and reputable tradition-specific sources. Cross-check visual attributes where possible.
3. Verify iconography individually: names and forms, skin/hair description where textually or traditionally specified, number and placement of arms/faces, weapons or sacred objects, vehicle/mount, hand gestures (mudras), clothing, ornaments, tilak/marks, colors, companions, and symbolic objects. Include only attributes supported by the selected tradition/source; do not fill gaps with guesses.
4. Distinguish scriptural description from regional artistic convention, later devotional art, and modern popular imagery. If sources differ, choose one clearly identified tradition/style and state that choice in the production notes.
5. Never combine attributes from different deities, traditions, avatars, or regions just because they look visually dramatic. Do not treat a modern poster depiction as proof of canonical details.
6. Depict sacred figures respectfully. Avoid parody, sexualization, degrading poses, careless combat/gore, or using sacred symbols as decoration. Consider that some communities discourage visual depiction; if the user's intent or tradition makes this sensitive, ask one concise clarification before generating.
7. Create and approve a deity/figure reference sheet before generating multiple scenes. Keep the same face, iconography, clothing, ornaments, attributes, and proportions throughout the video. If the source material does not specify a detail, keep it neutral or omit it rather than inventing certainty.
8. Add a short source note to the research brief and, where appropriate, the video description. Never claim that an AI-generated depiction is an authentic historical artifact or definitive representation.


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
