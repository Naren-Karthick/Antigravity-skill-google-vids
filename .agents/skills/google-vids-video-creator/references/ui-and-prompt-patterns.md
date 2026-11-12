# Google Vids UI Capabilities, Voices & Prompt Patterns

Reference details verified against Google Vids (`https://docs.google.com/videos/`).

## Verified Tooling Inventory

| Feature | Location | Key Options & Limits |
| :--- | :--- | :--- |
| **Aspect Ratio** | Startup modal / Toolbar `Video size` / `File -> Video size` | `Portrait 9:16`, `Landscape 16:9`, `Square 1:1` (`File -> Storyboard` disabled in `9:16`) |
| **AI Video Clip (`Omni`)** | Right sidebar: `Generate an AI video clip` | Modes: `Create` (up to 3 `Ingredients` images + `Avatar`), `Edit`, `Animate`, `Extend`; `720p` or `1080p`; `3s`–`15s` per clip |
| **Image Generation** | Right sidebar: `Generate an image` | `Square 1:1`, `Landscape 16:9`, `Portrait 9:16`; Styles: `Photography`, `Background`, `Vector art`, `Sketch`, `Watercolour`, `Cyberpunk`, `No style` |
| **AI Voiceover** | Right sidebar: `Generate a voiceover` | Powered by Gemini 3.8 Flash Lite TTS; 37 voices; `Current scene` or `All scenes`; type `[` for inline audio/expression tags |
| **AI Avatar** | Right sidebar: `Generate an avatar` | Script-driven talking avatar (`Current scene` / `All scenes`), supports `[` audio tags, preset voices/avatars (e.g., *Finley*) |
| **AI Music** | Right sidebar: `Generate music` | Powered by Lyria 3.5; `30-second clip` or `Full song`; `Instrumental` toggle vs. `Full` |
| **Recording** | Right sidebar: `Record` / `Insert` | Teleprompter (`Current scene` / `All scenes`), modes: `Camera`, `Camera and screen`, `Screen`, `Voiceover` |
| **Stock & Web** | Right sidebar: `Stock and web` | Getty Images (stock video/images), YouTube (music), Shutterstock (sound effects), Tenor (stickers/GIFs), Web/Google Images |
| **Drive, Photos & Upload** | Right sidebar / `Insert -> Upload` | Import local/Drive/Photos images, video, and audio (`MP4`, `WebM`, `MOV`) |
| **Captions** | Right sidebar: `Captions` | `All scenes` or `Current scene`; categories: `Word emphasis` (highlighted Shorts-style), `Line by line` (10 presets), `Word by word` (6 presets) |
| **Motion & Visuals** | Toolbar & `Insert` menu | `Animation` (`Ctrl+Shift+M`: Scene moods `None`, `Classic`, `Playful`, `Soft`, `Rhythmic`, `Bold`, `Festive`; Simple `Fade`, `Slide`, `Rise`, `Scale`, `Elastic slide`, `Toaster`, `Pop`, `Stomp`; per-Object animations), `Transition` (`Ctrl+Alt+R`), `Shapes and lines`, `Insert from templates`, `Table`, `Chart`, `Special characters`, `Customise styles`, `Background` |
| **Timeline & Shortcuts** | Bottom timeline & top toolbar | `Show timing` per-object tracks, `New scene` (`Ctrl+M`), `Duplicate scenes`, `Delete scenes`, `Split scene at playhead` (`Ctrl+Shift+S`), `Move scenes`, zoom slider `5`–`800`, `Preview` (`Ctrl+F5`), `Audio trimming`, `Transcript`, `Voice typing` |
| **Export** | `File -> Download` / `File` menu | `MP4 video (.mp4)`, `GIF animation (.gif)`, `Export to Drive`, `Export to YouTube (New)` |

## Creation Mode Decision Matrix

Pick the fastest Google Vids workflow for the user's goal:

- **Animated stories, Shorts, custom visual explainers:** Start with `Blank vid` + `Generate an image` (character/style reference) + `Omni` (`Create` with `Convert to video` / `Ingredients`) + `Generate a voiceover` + `Captions` (`Word emphasis`).
- **Diagram / slide-style explainers or product demos:** Start with `Blank vid` or `Insert from templates` (filterable by Function, Design style, Colour, Industry), combine `Shapes and lines`, `Chart`, `Table`, `Generate an image`, and per-`Object` `Animation` (`Ctrl+Shift+M`).
- **Presenter-led explainer:** Use `Generate an avatar` (`Current scene` or `All scenes` with `[` tags) over custom backgrounds/templates.
- **Converting existing Docs or Slides (`16:9`):** Use `Docs to video` or `Slides to video` (`File` menu or `16:9` startup modal).
- **Screen walkthrough + voice:** Use `Record` (`Camera and screen` / `Screen` with built-in teleprompter).

## Omni (`Generate an AI video clip`) Mode Efficiency Guide

- **`Create`:** Text-to-video (`3s`–`15s`, `1080p`). Attach up to 3 `Ingredients` images (or hover a `Generate an image` card -> `Convert to video`) to keep characters/environments consistent as `@Image1`.
- **`Animate`:** Turns a single static image (generated diagram, scene art, or photo) into smooth motion (`3s`–`15s`). Ideal for explainer diagrams or title visuals.
- **`Extend`:** Continues seamlessly from an existing `MP4`/`WebM`/`MOV` clip when an unbroken scene exceeds `15s`.
- **`Edit`:** Applies prompt-driven visual changes to an existing clip (`MP4`/`WebM`/`MOV`) instead of regenerating from scratch.
- **Speed Adjustment Trick:** When a generated clip is slightly shorter than its voiceover (e.g., `9.02s` vs `9.4s`), adjust clip speed (e.g., `0.95x`) to stretch it cleanly without regenerating.

## Audio Mixing & Sync Rules

1. **Mute AI Video Clips:** Always set `Format -> Sound -> Mute` on `Omni` clips when using dedicated voiceover + music + SFX.
2. **Track Hierarchy:** Keep **Voiceover** loudest and clearest, **SFX** (`Stock and web -> Sound effects`, trimmed to exact action beats via `Show timing`) medium-low, and **Background Music** (`Generate music` with `Instrumental` ON) subtle underneath.
3. **Zero Overlap / Zero Gaps:** Verify per-scene `Show timing` tracks so narration finishes before the scene ends and music trims cleanly at the final scene boundary.

## Script & Explainer Planning Blueprint (When Only Title/Topic Is Given)

When the user supplies only a title or topic (or requests an explainer without a script):

1. **Web Research (`search_web`):** Gather 3–5 verified facts, definitions, numbers, or surprising angles so the narration is accurate and informative rather than generic filler.
2. **Scene-by-Scene Script Table:**
   - Keep each scene between **5s and 14s** (within Omni's `3s`–`15s` limit; ~2.5 spoken words per second).
   - **Explainer Structure:**
     1. **Hook (5–8s):** Curiosity gap, bold question, or surprising fact.
     2. **Core Concept (10–14s):** Simple visual metaphor explaining what it is or how it works.
     3. **Mechanism / Steps (10–14s):** Cause-and-effect breakdown with clear visual action.
     4. **Real-World Impact / Twist (10–14s):** Why it matters, edge case, or counterintuitive detail.
     5. **Takeaway / Outro (6–10s):** Memorable wrap-up and viewer question/CTA.

## Character Reference & Omni Prompt Template

1. **Character Reference Prompt (`Generate an image` -> `Vector art`):**
   > Clean 2D [character type] reference sheet on a plain solid white background: [exact visual traits], centered full-body standing pose, clean flat 2D animation art style, no text, no watermarks.

2. **Per-Scene Omni Prompt (`Generate an AI video clip -> Create` with `@Image1`):**
   > [Art style], [aspect ratio e.g. vertical 9:16]. Using the exact character from @Image1 ([restate key traits briefly]), [clear action sequence with beginning, middle, end]. [Camera motion + lighting + environment]. Smooth animation, no text overlays, no watermarks, no speech.

## Voice Selection Tips (`Generate a voiceover`)

- **Energetic young adult male (YouTube Shorts storytelling):** `Neo` (`en/Puck.wav`, *"Upbeat, medium pitch"*).
- **Other inspected conversational/classic voices:** `Kero` (`en/Fenrir.wav`, *"Excitable, lower middle pitch"*), `Elio` (*"Friendly, lower middle pitch"*), `Nyla`, `Holt`, `Knox`, `Narrator`, `Educator`, `Teacher`, `Persuader`, `Explainer`, `Coach`, `Motivator`.

## Pre-Export Validation Checklist

- [ ] All planned scenes are present with zero black gaps or empty placeholder frames.
- [ ] Character appearance and art style match across every scene.
- [ ] All AI video clips' native audio tracks are muted (unless intentionally kept) so they do not clash with voiceover.
- [ ] Narration plays completely without clipping at scene boundaries or overlapping the next scene.
- [ ] Background music and sound effects sit cleanly underneath narration without sudden volume spikes.
- [ ] Captions match the spoken script, have no typos, and avoid covering faces or key visuals.
- [ ] Project aspect ratio (`9:16` / `16:9` / `1:1`) and total runtime match the target spec.
- [ ] Downloaded `.mp4` exists on disk, has non-zero size, and plays cleanly.

