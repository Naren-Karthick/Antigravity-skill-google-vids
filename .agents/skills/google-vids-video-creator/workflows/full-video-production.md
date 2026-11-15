# Full Video Production Workflow

Use this workflow for a complete video from topic to exported MP4.

## 1. Brief
Read the request and attachments. First confirm whether the deliverable is a long-form YouTube video or a YouTube Short. If the user has not specified, ask exactly one direct question — "Do you want a long-form YouTube video or a YouTube Short?" — and wait for the answer before research/script production. If already specified, do not ask again. Then define audience, language, platform, runtime, aspect ratio, tone, narration, visual style, and export target.


## 1A. Discover a topic and prepare YouTube packaging (when requested or no title is supplied)
Research current audience-interest signals and the channel niche before recommending topics. Build a 5–10 idea shortlist, score demand signals, curiosity, novelty, channel fit, visual potential, competition/differentiation, and feasibility, then recommend one with evidence and caveats. Do not promise virality or invent analytics/search-volume data.

For the chosen topic, create 3–5 accurate title options and recommend one. Generate a dedicated 16:9 thumbnail image with a single clear focal subject, high contrast, short readable text if useful, and safe margins. Use image generation for the image itself; add exact typography in a design tool if needed. Inspect it at mobile size. Prepare a description, relevant tags, a few hashtags, CTA, pinned comment, optional community teaser, and upload checklist. Add chapters only after final runtime/timestamps are known. Save everything using the YouTube publishing package template. If the user asked only for topic ideas, stop here; otherwise continue production.

## 2. Title-led research (required when only a title is supplied)
Treat the title as enough to start. Do not ask the user to supply a script or research notes. Do not infer long-form versus Shorts from the title. If the format is not already known, ask the required format question in Step 1 and wait. Once answered, tailor runtime, aspect ratio, pacing, scene count, narration density, hook, and ending to that format. Record the choice in the production plan.

- Break the title into the central question, concepts, audience, and promised outcome.
- Research the topic before scripting. Prefer primary sources such as official documentation, original research, government/university publications, standards bodies, and direct datasets; use reputable secondary sources for context.
- Cross-check important factual claims against at least two independent credible sources where practical. Check dates for current or changing topics.
- Save a research brief containing key findings, verified facts, examples, caveats, uncertainties, source titles/organizations, URLs, and research date.
- Distinguish established facts from interpretation, prediction, and hypothetical storytelling. In "what if" videos, explain the real-world baseline and label imagined outcomes as speculation.
- Verify names, dates, figures, units, definitions, quotations, and code examples. Omit or qualify unsupported claims; never fabricate evidence or citations.

## 2A. Format-specific content design
- Long-form YouTube: default landscape 16:9. Build a deeper narrative with a strong opening hook, clear sections, examples/context, natural transitions, and a satisfying conclusion. Set runtime based on topic depth and user direction; add chapters after final timestamps are verified.
- YouTube Shorts: default vertical 9:16. Deliver one focused idea quickly, hook viewers in the opening seconds, use tighter sentences and faster visual changes, large mobile-safe captions, and a concise payoff/CTA. Remove lengthy introductions and unnecessary exposition. Fit the script to a concise short-form runtime supported by current platform rules and user preference.
- Never create a long-form script and merely crop it into a Short. Write and storyboard specifically for the selected format. If the user requests both, create separate scripts, edits, titles, and thumbnails/packages for each.

## 3. Script
Turn the research brief into a complete, runtime-appropriate script: hook, narrative arc, clear explanations, transitions, narration, scene-by-scene visual intent, concise on-screen text, music/SFX cues, conclusion, and CTA where appropriate. Include source notes for the description or references slide when useful. Keep sentences speakable and check factual claims and pronunciation. For educational/code topics, verify the code and explanations.

**Continue automatically:** unless the user explicitly requests only research, an outline, or a script, continue from the title through storyboard, asset creation, Google Vids editing, quality checks, and export. Do not stop after presenting the research or script.

## 3A. Select visual style and design characters
Choose a fitting style per video: 2D vector/hand-drawn/cut-out, 3D stylized/realistic, stickman, anime-inspired original designs, cinematic/realistic, or a deliberate hybrid. Create a character bible and reusable reference sheet for recurring characters. For gods and sacred figures, research the exact tradition, region, period, scripture/iconographic sources, and attributes; distinguish textual descriptions from regional devotional art; do not mix iconography or invent unsupported details. Depict respectfully, and ask one concise question if a meaningful tradition choice or depiction sensitivity is unresolved.

## 4. Storyboard
For every scene define: ID, purpose, narration, measured/estimated duration, visual prompt, character references, on-screen text, SFX/music cue, transition, and continuity notes. Use measured narration audio to set scene length.

## 5. Prepare and pilot
Create a manifest and asset folders. Open Google Vids, create/name project, set aspect ratio. Establish visual style and reference assets. Generate one pilot scene and verify style, timing, audio, and insertion before batch work.


## 6. Check Vids quota and select the production path

Inspect the live Google Vids UI/account for a quota counter, remaining-use indicator, disabled generation control, or limit error. Record only observed evidence; do not hard-code allowances or estimate quota from this project's clip count.

- If Vids generation is available, make one pilot clip and continue in small batches after verifying it.
- If Vids reports quota exhaustion or the feature is unavailable, stop retrying and switch to the free local production fallback in `references/free-local-production-fallback.md`.
- Use Remotion first for general motion graphics, subject to current license eligibility. If unavailable or ineligible, use Motion Canvas, Manim, HTML/CSS/SVG/Canvas, or Blender according to the content.
- Generate narration with a suitable free local TTS engine (Kokoro first where supported; Piper only after checking the exact voice's model card/license; then an available offline OS voice).
- Render scenes locally and use FFmpeg for concatenation, narration/music/SFX mixing, captions, MP4 muxing, and validation.
- Do not switch to Google Flow, paid APIs, paid stock, paid TTS, or purchases as an automatic fallback. Ask before any paid action.
- If the machine lacks the required tools or cannot render the requested quality, report the blocker and offer a simpler local motion-graphics version or ask the user to provide assets/voiceover.

Google Vids may still be used for optional finishing if its remaining free features are sufficient; otherwise complete the final MP4 locally. Log the fallback reason, renderer, TTS engine/voice/license, asset licenses, FFmpeg version, and verification results.

## 7. Produce
Generate narration first for narration-led videos, then create visuals using the selected engine. With the local fallback, render and verify each scene, then assemble and mix with FFmpeg. Update the manifest after each verified scene. Never retry before checking whether the previous job succeeded.

## 8. Edit
Trim/extend clips, align narration, add subtle transitions, captions, music and SFX. Check text safe areas and mobile legibility. Preview the full sequence.

## 9. QA
Run the checklist. Fix failures and re-check. Mark untestable items as not verified.

## 10. Export
Export MP4 if offered. Wait for completion. Verify exact file path, non-zero size, metadata, dimensions, duration, and playback. Preserve the editable project and source assets.

## 11. Deliver
Report verified specs, project link, export location, QA status, tools used, and remaining limitations. Never say "finished" if the file or playback is unverified.
