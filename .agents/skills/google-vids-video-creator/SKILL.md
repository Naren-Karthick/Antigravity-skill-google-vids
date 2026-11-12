---
name: google-vids-video-creator
description: >-
  End-to-end workflow for creating, editing, narrating, captioning, and exporting
  complete videos in Google Vids (https://vids.google.com/) via browser control.
  Use when the user asks to produce a video, YouTube Short, explainer video, or
  animated clip in Google Vids—even if they only provide a title or topic without
  a script (researches the topic online, writes the full scene-by-scene script and
  voiceover, and builds the complete video).
---

# Google Vids Video Creator

Use this skill to produce complete, edited, narrated, and captioned videos (including YouTube Shorts, explainers, and story-driven animations) in **Google Vids** (`https://vids.google.com/`) through the `browser` subagent.

## Phase 0: Research & Script Generation (When No Full Script Is Provided)

Before opening Google Vids, check what the user supplied:

1. **Topic-only or Title-only request (no script provided):**
   - **Research first:** Use `search_web` to look up accurate, current facts, key mechanisms, real-world examples, and engaging hooks about the title or topic.
   - **Write a complete production script** before launching the browser workflow:
     - **Format & aspect ratio:** Default to `16:9` Landscape for standard explainer/educational videos, or `9:16` Portrait for Shorts/Reels/TikTok (respect any explicit user preference).
     - **Scene breakdown:** Split into clear scenes (each `3s`–`15s` to align cleanly with Omni AI video clip limits; target ~45–60s for Shorts or 60–120s for explainers unless specified).
     - **For each scene, define:** Visual prompt (consistent character/style), Voiceover narration line (concise, natural spoken phrasing), Music mood, and SFX cues.
2. **Explainer video request:**
   - Follow an **Explainer Story Arc**: *Hook / Question -> Clear Core Explanation (How It Works) -> Concrete Example or Visual Analogy -> Twist / Nuance -> Summary & Call-to-Action*.
   - If the user provided a script, use it faithfully; if they provided only a topic or title, research via `search_web` and generate the full explainer script first.
   - Choose a clear, engaging voice (`Neo`, `Explainer`, `Educator`, or `Narrator` in `Generate a voiceover`) and keep that same voice across all scenes.

## Prerequisites & Browser Delegation

1. **Delegate UI work to the `browser` subagent**: Use `invoke_subagent` (`TypeName: "browser"`) for all Google Vids interactions. Keep the same browser subagent alive across phases using `send_message` rather than spawning duplicates.
2. **Handle setup blockers immediately**:
   - If Chrome DevTools fails to attach (`DevToolsActivePort` missing), pause and ask the user to open Chrome and enable `chrome://inspect/#remote-debugging`.
   - If Google Sign-In or Workspace access is required, stop and let the user authenticate manually, then resume via `send_message`.

## Phase 1: Project Initialization

1. Navigate to `https://vids.google.com/`.
2. Choose the optimal starting flow (see [Creation Mode Decision Matrix](./references/ui-and-prompt-patterns.md#creation-mode-decision-matrix)):
   - Default to **`Blank vid`** for custom multi-scene animated/narrated videos so you control every scene's timing, voiceover, and assets.
   - Use **`Docs to video`** or **`Slides to video`** only when converting an existing Google Doc/Slides deck in `16:9` (hidden in startup modal when `9:16` or `1:1` is selected; `File -> Storyboard` is also disabled in `9:16`).
3. Set the aspect ratio immediately via the startup modal, toolbar `Video size`, or `File -> Video size` (`Portrait 9:16`, `Landscape 16:9`, or `Square 1:1`).
4. Rename the project title in the top-left header.

## Phase 2: Character & Style Consistency

Google Vids does not have a native character-rigging tool. Establish visual consistency before generating scenes:

1. Open **Generate an image** in the right sidebar.
2. Choose an aspect ratio (`Square 1:1` or project ratio) and a clean style (`Vector art`, `Sketch`, `Watercolour`, `Cyberpunk`, `Photography`, or `No style`).
3. Generate a clean character reference sheet on a plain solid background with no text or watermarks. Inspect it visually and regenerate if cluttered.
4. **Do not leave the raw reference sheet on any final scene canvas.** Instead, keep it in `Generate an image` history and hover it -> **`Convert to video`** (or attach it under `Generate an AI video clip -> Create -> Ingredients`, up to 3 images) so Omni binds it as `@Image1` across every scene.

## Phase 3: Voiceover-First Scene Production

Always generate each scene's voiceover **before** generating its AI video clip so clip duration matches speech duration without clipping or gaps.

1. Create all planned scenes in the timeline (`New scene` / `Ctrl+M`).
2. **Pick one consistent narrator** in **Generate a voiceover** (Gemini 3.8 Flash Lite TTS, 37 voices; supports `[` expression tags). Use the exact same voice across every scene.
3. For each scene in sequence:
   - Select the scene in the timeline and generate its **Current scene** voiceover. Record its exact duration (e.g., `6.6s`).
   - Open **Generate an AI video clip -> Create** (with `@Image1` attached from `Convert to video` or `Ingredients`).
   - Set **Resolution** to `1080p`, **Aspect Ratio** to match the project, and **Duration** (`3s`–`15s` slider) to `>= ceil(voiceover_duration)` (split or use `Extend` if a scene exceeds 15s).
   - **Speed-Match Efficiency Trick:** If a generated clip comes out slightly shorter than its voiceover (e.g., `9.02s` clip vs `9.4s` voiceover), adjust the clip's playback speed slightly (e.g., `0.95x`) rather than regenerating the clip.
   - Write prompts referencing `@Image1`, camera movement, lighting, and explicit exclusions: `no text overlays, no watermarks, no speech`.
   - Insert the clip edge-to-edge filling the frame, **mute the clip's own audio track** (`Format -> Sound -> Mute`) so it does not clash with narration, and match the scene duration to the clip.

## Phase 4: Music, Sound Effects, Captions & Transitions

1. **Background Music (`Generate music`, Lyria 3.5)**:
   - Choose `30-second clip` or `Full song` and toggle **Instrumental** on when narration is present.
   - Lower music volume below the voiceover track so narration stays crisp.
2. **Sound Effects (`Stock and web -> Sound effects`)**:
   - Search Shutterstock SFX and place cues aligned with scene beats using the timeline `Show timing` toggle. Keep SFX balanced under narration.
3. **Captions (`Captions` sidebar)**:
   - Apply to `All scenes` (or per scene) using `Word emphasis` (for Shorts-style highlighted words), `Line by line`, or `Word by word`.
   - Position captions in the lower-middle safe zone so they never cover characters' faces or UI edges.
4. **Transitions & Polish**:
   - Add smooth scene **Transitions** (`Ctrl+Alt+R`, enabled once 2+ scenes exist) and optional **Animations** (`Ctrl+Shift+M`).

## Phase 5: Quality Check & Export

1. Play the full video from `00:00.0` (`Preview` / `Ctrl+F5`) and check the [pre-export checklist](./references/ui-and-prompt-patterns.md#pre-export-validation-checklist).
2. Export via **`File -> Download -> MP4 video (.mp4)`** (or `Export to Drive` / `Export to YouTube`).
3. Wait for rendering and browser download to finish, then confirm the `.mp4` file exists in the user's Downloads folder and is playable.

## References

- [Google Vids UI Capabilities, Voices & Prompt Patterns](./references/ui-and-prompt-patterns.md)

