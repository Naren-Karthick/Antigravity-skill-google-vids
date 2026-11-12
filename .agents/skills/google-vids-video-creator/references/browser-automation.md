# Browser Automation Rules

## Core loop
1. Inspect the current tab/page and identify the current application state.
2. Choose one small action.
3. Execute using the available browser tool.
4. Re-inspect and verify the resulting state.
5. Record the checkpoint before proceeding.

## Reliable interaction
- Prefer accessible roles/names, visible labels, and stable element identifiers.
- Use coordinates only when semantic interaction is unavailable; take a fresh screenshot before coordinate actions.
- Re-locate controls after navigation, modal changes, scrolling, zoom, or responsive layout changes.
- Wait for visible completion indicators rather than arbitrary long sleeps.
- Do not assume a click succeeded. Verify the intended dialog, asset, scene, or state appeared.
- Avoid multiple destructive or expensive actions in one unverified batch.

## Google Vids workflow
- Confirm correct Google account and project before editing.
- Confirm aspect ratio and project title.
- After generation, verify the asset appears in the generation result and is inserted into the intended scene.
- After timeline edits, inspect scene order and track alignment.
- Before export, preview from start to finish.
- During export, wait for explicit completion and verify the downloaded file.

## Safety and blockers
- Let the user complete sign-in, consent, permissions, Workspace policy prompts, and any CAPTCHA.
- Never request passwords, session cookies, recovery codes, or one-time codes.
- Do not bypass account restrictions or security controls.
- Do not delete, overwrite, share, publish, or purchase without authorization.
- If the browser connection is lost, inspect/reconnect to the existing session rather than starting duplicate projects.
- If a feature is unavailable, report the observed limitation and choose a permitted alternative only when it meets the user's goal.

## Tool contract
Use only browser tools actually exposed in the current environment. Do not invent a "browser subagent" API or assume a particular tool name. If no browser-control capability is available, explain the blocker and provide the next action needed.
