# Audio Production

## Narration
- Decide whether narration is required; do not add it to a music-only or silent video without reason.
- Use one consistent narrator voice for a single-speaker video.
- Generate narration in scene-sized units when timing needs tight synchronization; otherwise a continuous track may be easier to maintain.
- Measure actual audio duration after generation.
- Listen for pronunciation, pacing, unnatural pauses, clipping, noise, and abrupt cuts.
- Check names, acronyms, numbers, dates, and non-English pronunciation manually.
- Never clone a real person's voice without explicit consent and rights.

## Music and SFX
- Prefer instrumental music under spoken narration.
- Keep voiceover clearly dominant; music and effects should support rather than compete.
- Align SFX to visible actions and story beats.
- Avoid repeated whooshes, impacts, and unnecessary background layers.
- Check for clipping, abrupt starts/stops, and unintended silence.
- Mute native video-clip audio when it conflicts with dedicated narration/music; retain it when it is intentionally part of the scene.

## Free local TTS and audio tools
When Google Vids AI video quota is exhausted and the local fallback is active, generate narration with a free offline engine rather than a paid cloud API. Prefer Kokoro locally when the required language/voice is supported; otherwise consider Piper only after checking the exact voice's MODEL_CARD and training-data license, then a suitable built-in offline OS speech engine. Generate a short test, confirm pronunciation and voice quality, and measure every narration file. Do not assume all voices or language packs are free for every use.

Use FFmpeg for automated audio conversion, fades, mixing, loudness checks, synchronization, and final muxing. Audacity is an optional free manual editor for waveform cleanup and listening checks. Keep narration dominant, duck music under speech, avoid clipping, and retain asset/license notes. Never silently call a paid cloud TTS API or use an unlicensed music/SFX track.

## Synchronization
- Scene duration must cover narration plus a natural visual tail.
- Avoid cutting words at scene boundaries.
- Verify audio track alignment after every timeline rearrangement.
- Listen to the exported file, not only the editor preview, when possible.
