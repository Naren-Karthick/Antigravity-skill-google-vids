# Antigravity Skill: Google Vids Video Creator

An Antigravity agent skill that teaches AI agents to plan, research, script, animate, narrate, caption, and export complete videos in **Google Vids** (`https://vids.google.com/`) through browser control.

## Contents

- `.agents/skills/google-vids-video-creator/SKILL.md` — Core end-to-end production workflow (research & script generation for title/topic-only prompts, explainer story arc, `9:16` / `16:9` / `1:1` setup, consistent character creation via `Generate an image` + Omni `Ingredients` / `Convert to video`, voiceover-first timing, Lyria 3.5 music, Shutterstock SFX, `Word emphasis` captions, transitions, QA, and MP4 export).
- `.agents/skills/google-vids-video-creator/references/ui-and-prompt-patterns.md` — Verified Google Vids tooling inventory, creation mode decision matrix, Omni `Create` / `Animate` / `Extend` / `Edit` guide, audio mixing rules, keyboard shortcuts, and pre-export checklist.

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

