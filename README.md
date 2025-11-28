# Daniel — Floating Sci-Fi Head UI

A lightweight front-end concept for the Daniel autonomous BD agent: a floating holographic head with supporting chrome, ready to swap in a Sora-rendered clip or photoreal still.

## What’s inside
- `index.html` – layout for the head, surrounding rings, and guidance panel.
- `styles.css` – holo-inspired styling, glow rings, floating animation, and scanline sweep.
- `assets/daniel_head_placeholder.svg` – vector placeholder until you drop in the generated render.
- `docs/sora_prompts.md` – Sora/photographic prompts and integration steps.

## Quick start
1. Open `index.html` in a browser to see the concept.
2. Generate Daniel’s face with Sora or your preferred tool using the prompts in `docs/sora_prompts.md`.
3. Replace `assets/daniel_head_placeholder.svg` with your rendered asset (transparent WebM/MP4 or PNG/WebP still).
4. Adjust CSS variables in `styles.css` to drive stateful UI (thinking/speaking/idle) or audio-reactive glows.

## Customization ideas
- Map the floating animation amplitude to microphone input for live presence.
- Tint `--accent`/`--accent-2` based on agent status (processing, speaking, paused).
- Swap the ring pulse timing to mirror speech cadence or heartbeat-like pacing.
