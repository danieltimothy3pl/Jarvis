# Sora + Photographic Generation Brief for Daniel's Floating Head

Use these prompts verbatim or adapt them inside your chosen video / photo generator (Sora, Runway, Pika, Midjourney, Stable Diffusion). The goal is a photoreal, sci‑fi holographic head that matches the front-end shell in `index.html`.

## Video prompt (Sora)
```
A photoreal, gender-neutral holographic human head named Daniel, floating in mid air above a dark navy background. Camera performs a slow dolly-in with a subtle orbit, macro lens bokeh, eye focus rack. Lighting is cool teal and violet rim light with a soft neutral fill. Thin scanlines and volumetric particles drift around the face. The head gently rotates and nods as if listening, with mouth barely moving. Surface has translucent skin, micro circuits and iridescent highlights. Frame 3/4 view, chest-up, no torso below the clavicle. Ultra HD, cinematic, 12 seconds.
```

**Variants to try**
- Swap "gender-neutral" with "androgynous masculine" for a firmer jawline.
- Add "African American" or "Latino" descriptors to guide skin tone while keeping the holographic sheen.
- Add "slow blinking bioluminescent eyes" for extra readability.

## Still image prompt (photo/SDXL/MJ)
```
Hyper-detailed portrait of a floating holographic human head named Daniel, 3/4 view, teal and violet rim light, dark navy void background, faint scanline glow, translucent skin with subtle circuitry, volumetric particles, cinematic macro depth of field, calm attentive expression, sci-fi interface reflections.
```

**Negative prompt**: disfigured, distorted, extra limbs, extra eyes, text, watermark, lowres, fogged lens, heavy makeup, helmet, body beyond shoulders.

## Output guidance
- Render at 16:9 or square; the CSS frame will crop to a circle automatically.
- Export a transparent WebM/MP4 (alpha) if possible; otherwise use a PNG/WebP keyframe for the placeholder.
- Keep the head centered with headroom so the rings in `index.html` remain visible.

## Integration steps
1. Generate the clip or still using the prompts above.
2. Export a transparent WebM (preferred) or PNG.
3. Replace `assets/daniel_head_placeholder.svg` in `index.html` with your render path.
4. Optionally map animation amplitude to audio/microphone level by adjusting the `@keyframes float` scaling.
5. For state changes ("thinking", "speaking", "error"), tint the CSS variables `--accent` and `--accent-2` dynamically.

## Audio-reactive idea (optional)
- Tie the glow strength to speech volume by updating `--glow` via JavaScript on `requestAnimationFrame`.
- Pulse the inner ring when the agent is "processing" and pause it when idle.
