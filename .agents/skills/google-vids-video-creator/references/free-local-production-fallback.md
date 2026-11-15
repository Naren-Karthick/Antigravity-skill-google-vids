# Free Local Production Fallback (After Google Vids Quota)

## Goal

When Google Vids AI video-generation quota is exhausted or the feature is unavailable, continue producing the video locally with free tools. **Do not switch to Google Flow or another credit-based/paid AI video generator.** The fallback should create motion graphics, narration, sound, captions, and a final MP4 without depending on a generative-video quota.

Google Vids remains the preferred path while its generation quota is available. Once blocked, use this local pipeline; Google Vids may still be used for optional finishing only if it provides a useful free capability and does not reintroduce the blocked quota dependency.

## 1. Check local prerequisites

Inspect the machine before installing anything:

- Node.js and npm (for Remotion / Motion Canvas)
- Python and pip/uv (for Manim and some local TTS runtimes)
- FFmpeg and ffprobe (rendering, muxing, audio mix, subtitles, validation)
- Available disk space, RAM, GPU/CPU, and target resolution/frame rate

Use already-installed tools first. If a required tool is missing, prefer official installation instructions and free packages. Do not install software, download large model weights, or change system settings without user authorization where the environment requires it. Never install from untrusted mirrors.

Create a local project structure such as:

```text
video-project/
  research/
  script/
  assets/
    images/
    fonts/
    music/
    sfx/
  audio/
    narration/
    music/
    sfx/
  motion/
    remotion/        # or motion-canvas/ or manim/
  renders/
    scenes/
    final/
  captions/
  manifest.json
  qa-report.md
```

## 2. Visual production engine selection

Use this decision order and record the chosen engine in the manifest.

### Primary fallback: Remotion

Use Remotion first for general-purpose YouTube videos, Shorts, explainers, stickman/cartoon stories, title sequences, kinetic typography, data visualizations, diagrams, and multi-scene compositions.

- Build a local React/Remotion project using the current official setup instructions. Do not assume old CLI commands, API names, or version-specific props; inspect the installed version's docs and examples.
- Implement each storyboard beat as a reusable composition/scene component with explicit duration, dimensions, fps, and input props.
- Prefer deterministic programmatic animation: SVG shapes, CSS transforms, keyframes/interpolation, charts, maps, diagrams, text, character rigs, and parallax layers.
- Use supplied or properly licensed images/video as backgrounds or visual ingredients. Add camera moves, masks, depth layers, particles, and transitions to make still assets dynamic.
- Keep reusable character components and a character bible so recurring characters remain consistent.
- Render scenes or the complete composition locally. Verify render exit status and output files before continuing.
- Check Remotion's current license before use. Its official terms currently provide a free license for individuals and qualifying small teams (up to three people), but it is source-available under a proprietary license, not OSI open source. If the user/project does not qualify, do not use it for production; select an open-source alternative instead.

Official references:
- https://www.remotion.dev/docs
- https://www.remotion.dev/docs/license/pricing
- https://www.remotion.dev/docs/terms

### Open-source alternatives

If Remotion is unavailable, incompatible, or not eligible under its current license:

1. **Motion Canvas** — preferred for vector-based explainers and voiceover-synchronized educational animations. It is free and open source. https://motioncanvas.io/docs/
2. **Manim Community Edition** — use for mathematics, algorithms, scientific concepts, graphs, equations, and precise technical animations. MIT-licensed; do not reuse protected 3Blue1Brown character/art assets. https://docs.manim.community/en/stable/
3. **HTML/CSS/SVG/Canvas animation** — use for lightweight kinetic typography, diagrams, UI mockups, charts, stick figures, and simple 2D scenes. Capture frames with a locally available browser automation/runtime and encode with FFmpeg.
4. **Blender** — use only when genuine 3D scenes materially improve the story and the machine can handle rendering. Use its official free/open-source distribution and respect asset licenses.

Do not install every engine. Select the simplest tool that meets the storyboard and the machine's capabilities.

## 3. Turn the storyboard into motion graphics

For every scene, define:

- Scene ID, duration, narration segment, and intended emotion
- Composition size and frame rate matching the final video
- Background, foreground, characters, objects, and layers
- Entrance, emphasis, movement, exit, and transition
- Text/caption safe areas for 16:9 or 9:16
- Asset source and license/attribution
- Whether the scene is vector animation, diagram, kinetic typography, character animation, stock footage with motion, or a hybrid

Prioritize meaningful animation over decorative effects. Use a visual change or camera movement often enough to sustain attention, but do not make every element move at once. Build Shorts vertically from the beginning; never rely on cropping a landscape render.

For a realistic scene that cannot be recreated convincingly with motion graphics, use user-provided footage or properly licensed free stock media with subtle pan/zoom, overlays, labels, and transitions. Do not pretend a motion-graphic approximation is generated live-action footage.

## 4. Generate narration with free local TTS

Prefer offline/local TTS so narration does not require paid API credits or upload the script to an unknown service.

Recommended order:

1. **Kokoro local TTS** if the supported language, voice, hardware, and current license suit the project. Use an official/reputable implementation and verify whether the chosen runtime bundles dependencies with separate licenses. https://github.com/hexgrad/kokoro
2. **Piper TTS** if a suitable voice is available. Inspect the exact voice's MODEL_CARD and training-data license before use. Piper's engine and each voice have separate licensing; do not assume every voice is suitable for commercial publishing. https://github.com/OHF-Voice/piper1-gpl
3. **Built-in offline OS speech** or another already-installed local TTS engine as a fallback. Test pronunciation and audio quality before generating the full narration.
4. If no suitable free voice is available, ask the user to record narration or approve another tool. Do not silently call a paid cloud TTS API or claim that an unavailable language/voice is supported.

Workflow:

- Finalize and proofread narration first.
- Split into scene-sized paragraphs where synchronization matters.
- Generate a short voice sample and ask for approval only if voice choice materially affects the result; otherwise choose a clear default and proceed.
- Generate WAV where possible, use consistent voice/model/speed, and save model/voice/license details.
- Measure every file with ffprobe or the supplied audio-duration script.
- Listen to samples and final narration for pronunciation, pacing, clipping, artifacts, and silence.
- Re-record or regenerate only affected segments. Never speed up speech until it becomes unnatural just to fit a scene.

## 5. Music and sound effects

- Prefer user-provided tracks, public-domain recordings, or music/SFX whose current license explicitly permits the intended YouTube use.
- YouTube Audio Library and reputable free-asset libraries may be used only after checking the specific track's attribution and usage requirements.
- Do not assume that "free download" means royalty-free, commercial-use permitted, or attribution-free.
- Keep a source/license log for every music and SFX file. Avoid copyrighted songs, movie audio, unlicensed samples, and voice imitation.
- If no suitable licensed track is available, use subtle original sound design made from permitted synthesis/noise/tones or leave the scene without music.

## 6. Assemble and mix with FFmpeg

Use FFmpeg/ffprobe as the default free local finishing pipeline:

1. Render all scenes to the same resolution, frame rate, pixel format, and compatible codec settings.
2. Verify scene durations and ordering against the narration and manifest.
3. Concatenate compatible scene files, or render a single complete composition when the chosen engine supports it.
4. Add narration as the primary audio track.
5. Mix background music and SFX at lower levels under narration; use fades and ducking where appropriate. Avoid clipping and check loudness by listening as well as measuring.
6. Add captions as a selectable subtitle track or burn them in when required. Check font availability, spelling, line breaks, safe margins, and reading speed.
7. Mux the final video/audio/subtitles into MP4 using compatible codecs. Preserve a high-quality intermediate if storage allows.
8. Run ffprobe to verify dimensions, frame rate, duration, audio/video streams, and file size. Play the beginning, middle, and end; ideally watch/listen to the complete export.

FFmpeg licensing depends on how the binary was built and which optional components are enabled. Use a trusted build and check its license/build configuration where redistribution or legal compliance matters. https://www.ffmpeg.org/legal.html

Audacity may be used for manual waveform editing, cleanup, fades, and listening checks; it is optional, not required for automated assembly.

## 7. Captions and quality assurance

- Generate SRT/VTT from the final narration transcript, then align it to the measured audio.
- Correct names, numbers, punctuation, and technical terms manually.
- Inspect captions at phone size for Shorts and at normal playback size for long-form.
- Check visual continuity, character consistency, safe areas, contrast, motion smoothness, scene transitions, audio synchronization, and silence/gaps.
- Confirm the output is a playable MP4, not merely a project file or frame sequence.
- Keep source code, project files, assets, narration, captions, render logs, and QA report so the video can be revised.

## 8. Cost and permission rules

- The fallback must remain free to run with locally available/free software and assets. "Free" does not mean unlimited cloud credits.
- Do not use Google Flow, paid generation APIs, paid stock assets, subscriptions, or purchases as an automatic fallback.
- If a proposed tool is paid, requires a trial that will auto-renew, or needs a paid upgrade, stop and ask first.
- Check licenses for software, fonts, stock media, sound effects, voice models, and music separately.
- If hardware is too weak or a free voice/asset cannot meet the quality bar, explain the limitation and ask whether the user prefers a simpler motion-graphics treatment or to supply assets/voiceover. Do not silently downgrade quality or incur charges.

## 9. Manifest fields

Record:

- `video_engine`: google_vids | remotion | motion_canvas | manim | html_canvas | blender
- `fallback_reason`: quota_exhausted | feature_unavailable | account_blocked | tool_failure
- `visual_assets`: scene ID, file path, source, license, render status
- `tts_engine`, `tts_model`, `tts_voice`, `voice_license`
- `audio_assets`: narration/music/SFX paths, source, license, duration
- `ffmpeg_version`, render command/log, output codec and metadata
- `cost_check`: confirm no paid service or purchase was used
- `qa_status`, playback verification, known limitations
