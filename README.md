# 碎碎念 · Murmur

A tap-only daily journal that turns your tags into a poem.

Every day you tap a few things — themes, mood, fragments, objects. Next morning, the day quietly becomes a small imagist poem.
Once a week, a stanza. Once a month, a longer piece.
You can save the poem as an image and share it.

> · · ·  &nbsp;&nbsp; 碎念。 &nbsp;&nbsp;诗。

## What's in here

```
app/        # the working web app (single index.html, no build step)
brand/      # logo & brand reference
wireframes/ # design iterations v1 → v6, kept for the record
```

## Run it

Open `app/index.html` in any modern browser. That's it.

To generate poems you need a Claude API key:
1. Get one at [console.anthropic.com](https://console.anthropic.com/settings/keys)
2. In the app, click ⚙ → paste your key → Done
3. Tap **写下成诗 / Compose** on the Today screen
4. Open the Poem tab and tap **Write the poem**

The key is stored only in your browser's localStorage.

## Design principles

The hard parts of this app aren't the UI, they're the rules that keep the AI from writing bad poetry:

- **Imagist, not narrative.** Show concrete images. Never summarize.
- **No time references.** No "May", "this week", "Wednesday". Use abstract markers — *then, later, afterward* — or none at all.
- **No god-view summary.** No "you spent most of...", no third-person observation. The poem is a glimpse.
- **Use the user's words.** The poem's nouns come primarily from the user's recorded *objects* (物件) and one-line notes.
- **AI titles, from images.** The title is a word or phrase pulled from inside the poem — never the date or the period.
- **Modern minimal only.** Like 韩东 / 王小妮 / Mary Oliver / Jack Gilbert. No classical Chinese (古风). No greeting-card sentiment.
- **Repetition is a rhythm.** `工作。/ 工作。/ 工作。` says it without statistics.
- **First poem is the poem.** No regenerate button.

The full system prompt lives in `buildSystemPrompt()` inside `app/index.html`.

## Stack

- Vanilla HTML / CSS / JS, single file
- localStorage for persistence
- Claude API (Opus 4.7 by default, Sonnet 4.6 also supported) for poem generation, called directly from the browser
- `html2canvas` for image export
- Web Share API for native sharing on mobile

## Status

Personal prototype. Not deployed. The browser-direct API call exposes the key if used as-is in production — for real use, put a small backend in front (Cloudflare Worker, Vercel function) that holds the key server-side.

## Author

[M (@Mlikeason)](https://github.com/Mlikeason) · built with [Claude Code](https://claude.com/claude-code)
