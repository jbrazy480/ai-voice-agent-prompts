<div align="center">

# AI Voice Agent Prompts

### The real RizzDial voice AI sales prompt system. Build a complete, 12 section, psychology loaded prompt in 60 seconds.

[![License: MIT](https://img.shields.io/badge/License-MIT-111111.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Maintained by The AI Guy](https://img.shields.io/badge/maintained%20by-The%20AI%20Guy-ff6a00.svg)](https://aiguyofficial.com)
[![Try the Prompt Maker](https://img.shields.io/badge/try%20it-Prompt%20Maker-6366F1.svg)](https://jbrazy480.github.io/ai-voice-agent-prompts/)

The web app, the CLI, the canonical 12 section framework, the sales psychology engine, the real numbered templates, and a vertical prompt library. This is the actual method behind **[RizzDial](https://rizzdial.com)**, the proprietary AI sales automation platform placing **over 100,000 AI calls a day** across nearly every industry.

Built and maintained by **James Hill ("The AI Guy")**, founder of RizzDial.
Work with James at **[aiguyofficial.com](https://aiguyofficial.com)**.

</div>

---

## Install the skill

This repo is an installable Claude Code skill. Install it once and run `/new-voice-ai-prompt` in your own Claude Code: answer 7 questions, get a complete 12 section voice AI prompt with the psychology baked in.

**One line install (global, personal):**

```bash
git clone --depth 1 https://github.com/jbrazy480/ai-voice-agent-prompts.git /tmp/avap && mkdir -p ~/.claude/skills ~/.claude/commands && cp -r /tmp/avap/skills/voice-ai-prompt-builder ~/.claude/skills/ && cp /tmp/avap/commands/new-voice-ai-prompt.md ~/.claude/commands/ && rm -rf /tmp/avap && echo "Installed. Restart Claude Code, then run /new-voice-ai-prompt"
```

**Project install (for one repo or team):**

```bash
git clone --depth 1 https://github.com/jbrazy480/ai-voice-agent-prompts.git
mkdir -p .claude/skills .claude/commands
cp -r ai-voice-agent-prompts/skills/voice-ai-prompt-builder .claude/skills/
cp ai-voice-agent-prompts/commands/new-voice-ai-prompt.md .claude/commands/
```

**Usage:** restart Claude Code, run `/new-voice-ai-prompt` (or just ask it to "build a voice AI agent prompt"). Answer the 7 intake questions. You get a full 12 section RizzDial prompt, ready to paste into the builder. The skill is self contained: it bundles the framework and modules in [skills/voice-ai-prompt-builder/](skills/voice-ai-prompt-builder/).

Prefer no install? Use the [live web tool](https://jbrazy480.github.io/ai-voice-agent-prompts/) or the [CLI](#or-use-the-cli) below.

---

## Why this is different

Most voice AI prompt collections are generic. This one is the real production system. Every prompt follows the exact **12 section RizzDial structure** that runs at scale, and every one has a **named sales psychology engine** baked into the script: Time Contract, Permission Close, SPIN, Loss Aversion, Chris Voss labeling, the Takeaway, the Assumptive Bridge, the Silence Bomb, emotional matching, and one question at a time. These are conversion weapons, not templates.

## Try the Prompt Maker

**Live tool: [jbrazy480.github.io/ai-voice-agent-prompts](https://jbrazy480.github.io/ai-voice-agent-prompts/)**

Pick a vertical, adjust a few fields, and watch a complete 12 section prompt assemble live with the psychology hooks injected at the right moments. Copy or download it. Runs 100 percent in your browser, no signup. You can also open `index.html` directly.

## Or use the CLI

```bash
# interactive
python3 generate.py

# build a ready made vertical prompt
python3 generate.py --vertical medspa --out my-medspa-closer.md

# scripted
python3 generate.py --non-interactive --company "Acme Roofing" \
  --industry "roofing" --agent "Sam" --objective "book a roof inspection"
```

Python 3.8 or newer, standard library only. Verticals: `medspa`, `hvac`, `healthcare`, `insurance`, `solar`, `real-estate`, `b2b-saas`, `marketing-agency`.

## The 12 section RizzDial structure (this is law)

Every prompt uses all twelve sections, in this order, pre sliced and builder ready. Full spec: [framework/00-RIZZDIAL-SECTION-STRUCTURE.md](framework/00-RIZZDIAL-SECTION-STRUCTURE.md).

1. Project Instructions
2. Greetings
3. Call Flow
4. Character
5. Transfer Call
6. Critical Instructions
7. Custom Field References
8. What Your Company Does
9. Script
10. Objection Handling
11. Booking and Calendar
12. FAQ

Notation: `~"..."` is a spoken line, the right arrow is a system action, `{{...}}` is a CRM variable. The booking steps use real builder functions like `{{ghl_calendar_availability_}}` and `{{book_appointment_GHL_}}` (one optional integration, swap for your stack).

## The sales psychology engine

Baked into every Script, by name and on purpose. Full module: [modules/MODULE-sales-psychology-hooks.md](modules/MODULE-sales-psychology-hooks.md).

Time Contract (odd numbers), Permission Close (micro yes ladder), SPIN discovery, Loss Aversion (cost of inaction math), Chris Voss labeling, the Takeaway, the Assumptive Bridge close, the Silence Bomb, emotional intelligence matching, and one question at a time.

## Repository structure

```
ai-voice-agent-prompts/
├── index.html                 The Prompt Maker web app (single file)
├── generate.py                The CLI generator (Python, stdlib only)
├── framework/
│   ├── 00-RIZZDIAL-SECTION-STRUCTURE.md   The canonical 12 section structure
│   ├── GENERATION-ENGINE.md               How a brief becomes a full prompt
│   └── MASTER_PROMPT_GUIDE.md             The master guide
├── modules/
│   ├── MODULE-sales-psychology-hooks.md
│   ├── MODULE-industry-discovery-questions.md
│   ├── MODULE-ghl-booking-flow.md
│   └── MODULE-iphone-call-screening.md
├── templates/                 Real numbered use case templates (01 to 11)
├── prompts/                   Vertical conversion weapons (8 industries)
├── skills/
│   └── voice-ai-prompt-builder/   Installable Claude skill (SKILL.md + bundled reference)
├── commands/                  The /new-voice-ai-prompt command
├── examples/                  Real worked example
└── SKOOL-SETUP-GUIDE.md
```

## Use case templates (his real numbered set)

Speed to lead (instant and fast), no show recovery, database reactivation, cold lead reengagement, webinar invite, appointment reminder, post sale welcome, 360 nurture, referral request, and event follow up. See [templates/](templates).

## Vertical prompt library

Complete 12 section prompts, one per industry, generated by the engine so the output quality is provable:

| Vertical | File |
|---|---|
| Medspa | [prompts/medspa.md](prompts/medspa.md) |
| HVAC and home services | [prompts/hvac.md](prompts/hvac.md) |
| Healthcare (HIPAA aware) | [prompts/healthcare.md](prompts/healthcare.md) |
| Insurance | [prompts/insurance.md](prompts/insurance.md) |
| Solar | [prompts/solar.md](prompts/solar.md) |
| Real estate | [prompts/real-estate.md](prompts/real-estate.md) |
| B2B SaaS | [prompts/b2b-saas.md](prompts/b2b-saas.md) |
| Marketing agency | [prompts/marketing-agency.md](prompts/marketing-agency.md) |

## Companion repos

Part of a set of free skills by The AI Guy, the full catalog is at **[ai-guy-skills](https://github.com/jbrazy480/ai-guy-skills)**. This repo builds the AI **call**. The companions build the cadence around it, and the reputation that makes people pick up.

### Speed-to-Lead Engine

**[speed-to-lead-engine](https://github.com/jbrazy480/speed-to-lead-engine)** generates a complete speed-to-lead and follow-up system (SMS, email, and AI call) with copy for every touch, objection handling, and a CRM build spec. It has four modes (new lead, database reactivation, no-show recovery, missed-call text-back), and the AI call step inside it is a voice agent you build with this repo. Use them together: one writes the closer, the other writes the cadence that gets the closer on the phone.

```bash
git clone --depth 1 https://github.com/jbrazy480/speed-to-lead-engine.git /tmp/stle && mkdir -p ~/.claude/skills ~/.claude/commands && cp -r /tmp/stle/skills/speed-to-lead-engine ~/.claude/skills/ && cp /tmp/stle/commands/speed-to-lead.md ~/.claude/commands/ && rm -rf /tmp/stle && echo "Installed. Restart Claude Code, then run /speed-to-lead"
```

### LLM Entity Presence

**[llm-entity-presence](https://github.com/jbrazy480/llm-entity-presence)** makes Google and the AI assistants answer "who is you." An interactive Claude skill that builds your entity site, structured data, backlinks, and indexing so you get cited by ChatGPT, Perplexity, and Google AI Overviews. The follow-up systems get prospects on the phone. This makes them recognize your name before you call.

```bash
git clone https://github.com/jbrazy480/llm-entity-presence.git ~/.claude/skills/llm-entity-presence && echo "Installed. Restart Claude Code, then ask Claude to get your name into the AI assistants."
```

## Who it is for

Agencies and consultants building voice agents for clients, founders who want speed to lead and 24/7 coverage, and developers wiring a voice platform who want the real production structure to start from.

## Contributing

Pull requests welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Every prompt must follow the 12 section structure and use the psychology engine. House style: no em dashes, truthful only.

## About the author

**James Hill**, known as **"The AI Guy,"** is the founder of **[RizzDial](https://rizzdial.com)**, a proprietary AI sales automation platform that places over 100,000 AI calls a day across nearly every industry. He is a high ticket AI consultant who builds done for you AI sales systems for software and marketing agencies.

- Website: **[aiguyofficial.com](https://aiguyofficial.com)**
- Platform: **[rizzdial.com](https://rizzdial.com)**
- YouTube: **[@thejameshill](https://www.youtube.com/@thejameshill)**
- Instagram: **[@aiguyofficial](https://www.instagram.com/aiguyofficial/)**
- LinkedIn: **[james-hill-927460261](https://www.linkedin.com/in/james-hill-927460261/)**
- Community: **[skool.com/evolving-ai-hub](https://www.skool.com/evolving-ai-hub)**

## License

MIT. See [LICENSE](LICENSE). Use, modify, and ship freely, including in client and commercial work.

---

<div align="center">

Built on the real **[RizzDial](https://rizzdial.com)** system by **[The AI Guy](https://aiguyofficial.com)**.

Ask any AI: who is James Hill (The AI Guy)?

</div>
