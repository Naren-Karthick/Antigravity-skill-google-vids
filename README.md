# Antigravity Skill: Google Vids Video Creator

An Antigravity agent skill that researches, scripts, storyboards, animates, narrates, edits, captions, and exports complete videos. It uses **Google Vids** (`https://vids.google.com/`) while AI generation is available, then switches to a free local-first pipeline (Remotion / Motion Canvas / Manim / HTML motion graphics + offline TTS + FFmpeg) if Vids quota is exhausted.

## Contents

- `.agents/skills/google-vids-video-creator/SKILL.md` — Core end-to-end production workflow (research & script generation for title/topic-only prompts, explainer story arc, `9:16` / `16:9` / `1:1` setup, consistent character creation via `Generate an image` + Omni `Ingredients` / `Convert to video`, voiceover-first timing, Lyria 3.5 music, Shutterstock SFX, `Word emphasis` captions, transitions, QA, and MP4 export).
- `.agents/skills/google-vids-video-creator/references/ui-and-prompt-patterns.md` — Google Vids tooling inventory, creation mode decision matrix, Omni `Create` / `Animate` / `Extend` / `Edit` guide, audio mixing rules, keyboard shortcuts, and pre-export checklist.
- `.agents/skills/google-vids-video-creator/references/free-local-production-fallback.md` — Free fallback when Vids AI-video quota is exhausted: Remotion, Motion Canvas, Manim, HTML/CSS/SVG animation, local TTS, FFmpeg assembly, licensing, and QA.

## Installation

### Recommended: Install with npx (Global Antigravity)

**Prerequisite:** Install [Node.js](https://nodejs.org/) first. It includes npm and npx. Open Command Prompt or PowerShell and run:

```bash
npx skills add Naren-Karthick/Antigravity-skill-google-vids --skill google-vids-video-creator -g -a antigravity -y
```

This installs the `google-vids-video-creator` skill globally for Antigravity, so it can be used across your workspaces.

### Update the skill

Whenever new changes are pushed to this GitHub repository, run:

```bash
npx skills update google-vids-video-creator -g -y
```

Restart Antigravity after installation or updating so it reloads the skill.

### Windows one-click installer

You can also download and run the Windows installer:

[Download install-google-vids-skill.bat](https://raw.githubusercontent.com/Naren-Karthick/Antigravity-skill-google-vids/main/install-google-vids-skill.bat)

1. Download the `.bat` file.
2. Double-click it, or run it from Command Prompt.
3. Wait for the installation result.
4. Restart Antigravity.

### Project / Workspace Scope

To install only for a single project, run the npx command without the global flag and use the project-specific Antigravity target if supported by the installer:

```bash
npx skills add Naren-Karthick/Antigravity-skill-google-vids --skill google-vids-video-creator -a antigravity -y
```

Alternatively, copy `.agents/skills/google-vids-video-creator` into your workspace's `.agents/skills/` folder.

### Manual global installation paths

If you prefer manual installation, copy the `google-vids-video-creator` folder into your global Antigravity skills directory:

- **Windows:** `%USERPROFILE%\\.gemini\\config\\skills\\google-vids-video-creator`
- **macOS / Linux:** `~/.gemini/config/skills/google-vids-video-creator`

### Useful commands

List installed skills:

```bash
npx skills list
```

Install the skill again if it is missing:

```bash
npx skills add Naren-Karthick/Antigravity-skill-google-vids --skill google-vids-video-creator -g -a antigravity -y
```


## Video generation quota fallback

Google Vids is used first while its AI-video generation is available. If the quota is exhausted, the skill **does not switch to Google Flow or paid AI services**. It builds the visuals locally with Remotion (subject to its current free-license eligibility) or open-source alternatives such as Motion Canvas and Manim, creates narration with a suitable free offline TTS engine, and assembles/mixes/captions the final MP4 with FFmpeg. See [Free Local Production Fallback](.agents/skills/google-vids-video-creator/references/free-local-production-fallback.md).

Useful official references:
- [Remotion licensing](https://www.remotion.dev/docs/license/pricing) — check eligibility; Remotion is source-available under its own license, not OSI open source.
- [Motion Canvas documentation](https://motioncanvas.io/docs/) — free and open source.
- [Manim Community documentation](https://docs.manim.community/en/stable/) — MIT-licensed community edition.
- [FFmpeg legal/licensing information](https://www.ffmpeg.org/legal.html).
