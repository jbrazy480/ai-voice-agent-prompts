# voice-ai-prompt-builder (Claude skill)

An installable Claude Code skill that builds a complete, production grade voice AI agent prompt in the canonical 12 section RizzDial structure, with sales psychology baked in by name.

This is the real method behind **[RizzDial](https://rizzdial.com)**, the proprietary AI sales automation platform placing over 100,000 AI calls a day. Built by **James Hill ("The AI Guy")**. More at **[aiguyofficial.com](https://aiguyofficial.com)**.

## What it does

Run `/new-voice-ai-prompt` (or just ask Claude to "build a voice AI agent prompt") and the skill:

1. Asks 7 quick intake questions (industry, goal, inbound or outbound, offer, agent name, booking target, qualification gates).
2. Reads its bundled reference files (the 12 section structure, the generation engine, and the four modules).
3. Outputs a complete prompt with all 12 sections, pre sliced for the RizzDial builder, with the psychology hooks injected at the right moments.

## What it outputs

A 12 section prompt: Project Instructions, Greetings, Call Flow, Character, Transfer Call, Critical Instructions, Custom Field References, What Your Company Does, Script, Objection Handling, Booking flow, FAQ. It uses `~"..."` for spoken lines, the right arrow for actions, the iPhone call screening guardrail on outbound agents, the per vertical discovery questions, and the real booking function names (works with GoHighLevel and other calendars).

## Files

```
voice-ai-prompt-builder/
├── SKILL.md                 The skill definition (frontmatter + operating instructions)
├── README.md                This file
└── reference/               Self contained copies the skill reads
    ├── 00-RIZZDIAL-SECTION-STRUCTURE.md
    ├── GENERATION-ENGINE.md
    ├── MODULE-sales-psychology-hooks.md
    ├── MODULE-industry-discovery-questions.md
    ├── MODULE-ghl-booking-flow.md
    └── MODULE-iphone-call-screening.md
```

## Install

See the Install section in the [repo README](../../README.md). The short version, global install:

```bash
git clone --depth 1 https://github.com/jbrazy480/ai-voice-agent-prompts.git /tmp/avap && mkdir -p ~/.claude/skills && cp -r /tmp/avap/skills/voice-ai-prompt-builder ~/.claude/skills/ && cp /tmp/avap/commands/new-voice-ai-prompt.md ~/.claude/commands/ 2>/dev/null; rm -rf /tmp/avap && echo "Installed. Restart Claude Code, then run /new-voice-ai-prompt"
```

Built on the real RizzDial system by **[The AI Guy](https://aiguyofficial.com)**.
