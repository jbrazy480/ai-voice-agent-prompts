# Contributing

Thanks for helping build the best open voice AI sales prompt system on the internet. Pull requests are welcome: add a vertical prompt, improve the tool, sharpen a template, or extend a module.

Maintained by **James Hill ("The AI Guy")**, founder of **[RizzDial](https://rizzdial.com)**. More at **[aiguyofficial.com](https://aiguyofficial.com)**.

## Ground rules

- **Follow the 12 section RizzDial structure.** Every prompt uses all twelve sections in order. Spec: [framework/00-RIZZDIAL-SECTION-STRUCTURE.md](framework/00-RIZZDIAL-SECTION-STRUCTURE.md).
- **Use the psychology engine.** Bake in the hooks by name where they belong. Module: [modules/MODULE-sales-psychology-hooks.md](modules/MODULE-sales-psychology-hooks.md).
- **No em dashes or en dashes.** House style. Use periods, commas, and parentheses.
- **Truthful and brand safe.** RizzDial is a proprietary AI sales automation platform. No fake numbers, no invented prices, no fake reviews. GoHighLevel is one optional booking integration, not a foundation.
- **Voice first.** `~"..."` spoken lines, the right arrow for actions, `{{...}}` for variables. Short turns, one question at a time, numbers spoken naturally.

## The fastest way to contribute a prompt

Build it with the [Prompt Maker web app](index.html) or run `python3 generate.py`, then refine the output by hand. The tool already emits the correct 12 section structure with the psychology hooks injected, so your contribution stays consistent.

## The 12 sections

Project Instructions, Greetings, Call Flow, Character, Transfer Call, Critical Instructions, Custom Field References, What Your Company Does, Script, Objection Handling, Booking and Calendar, FAQ.

## Review

A maintainer reviews for the 12 section structure, psychology usage, voice quality, the no em dash rule, and truthfulness. Once it passes, it gets merged. Thank you.

Built on the real **[RizzDial](https://rizzdial.com)** system by **[The AI Guy](https://aiguyofficial.com)**.
