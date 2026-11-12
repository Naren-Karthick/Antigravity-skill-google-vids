# Video Prompt Engineering

## Prompt structure
Write each shot prompt in this order:

1. **Format:** aspect ratio, intended shot length, animation or live-action style.
2. **Subject:** the exact character/object and distinguishing visual traits.
3. **Action:** one clear action with beginning, middle, and end.
4. **Environment:** location, background, props, time of day.
5. **Composition:** subject placement, shot size, foreground/background.
6. **Camera:** locked, pan, tilt, tracking, dolly, orbit, or handheld; choose one purposeful move.
7. **Lighting and mood:** direction, softness, contrast, color temperature, emotional tone.
8. **Continuity:** reference image/ingredient, costume, proportions, palette, environment.
9. **Constraints:** no unwanted text, logos, watermarks, extra characters, or unintended dialogue when relevant.

## Character consistency
Create a character bible before generating multiple scenes:
- Character name/ID
- Shape and proportions
- Face, hair, clothing, accessories
- Main colors and line/texture style
- Typical expressions and movement
- Features that must never change

Use the same approved reference asset for every shot when the editor supports reference images. Restate the key traits in prompts; references help but do not guarantee perfect continuity. Review generated results and regenerate only when a mismatch materially harms the story.

## One shot, one dominant action
Avoid combining unrelated actions, camera moves, locations, and emotional changes in one prompt. Split complex sequences into separate shots. Make the action physically clear and visually observable.

## Stickman / 2D animation prompt pattern
"Vertical 9:16, clean minimalist 2D stickman animation, consistent [character description] with [distinctive clothing/accessory], [single action sequence], simple uncluttered [environment], expressive readable body language, smooth natural motion, fixed line weight and color palette, [camera direction], [lighting/mood], no dialogue, no captions, no text, no watermark."

## Cinematic prompt pattern
"[Aspect ratio], cinematic [genre/style] shot of [subject], [specific action with start-to-end progression] in [environment]. [Shot size and composition]. Camera [single movement]. [Lighting], [color palette], [atmosphere]. Maintain [continuity traits]. No unintended text, logos, or watermarks."

## Negative constraints
Use concise exclusions for likely failure modes. Do not pile on long contradictory lists. Avoid requesting readable text inside generated video; add titles and captions in the editor for spelling and layout control.

## Prompt iteration
When a generation fails:
1. Identify the visible defect.
2. Change only the prompt element related to that defect.
3. Keep the successful subject/style/continuity details.
4. Retry within the workflow's retry budget.
5. Record the revised prompt and result in the manifest.
