<div align="center">

# AI Voice Agent Prompts

### The free Voice AI Prompt Maker. Build a complete, production grade voice AI agent prompt in 60 seconds.

[![License: MIT](https://img.shields.io/badge/License-MIT-111111.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Maintained by The AI Guy](https://img.shields.io/badge/maintained%20by-The%20AI%20Guy-ff6a00.svg)](https://aiguyofficial.com)
[![Try the Prompt Maker](https://img.shields.io/badge/try%20it-Prompt%20Maker-6366F1.svg)](https://jbrazy480.github.io/ai-voice-agent-prompts/)

A free web app, a CLI generator, the 12 part framework, and a polished example library for building voice AI agents that book, qualify, and follow up.

Maintained by **James Hill ("The AI Guy")**, founder of **[RizzDial](https://rizzdial.com)**.
Work with James at **[aiguyofficial.com](https://aiguyofficial.com)**.

</div>

---

## Try the Prompt Maker

**Live tool: [jbrazy480.github.io/ai-voice-agent-prompts](https://jbrazy480.github.io/ai-voice-agent-prompts/)**

Open the app, fill a short guided form (business, industry, agent role, objective, voice, discovery questions, compliance), and watch a complete system prompt assemble live as you type. Then copy it or download it as Markdown or text. It runs 100 percent in your browser. No signup, no network calls, works offline.

What the web app gives you:
- A premium dark interface with a guided form and a live preview pane.
- A full prompt built on the 12 part framework, tailored to your business.
- One click Copy, Download .md, Download .txt, Reset, Load example, and Surprise me.
- TCPA and HIPAA compliance toggles that inject the right guardrails.

You can also just open `index.html` by double clicking it. It is a single self contained file.

## Or use the CLI

```bash
# interactive: answer a few questions, get a polished prompt file
python3 generate.py

# build a ready made example
python3 generate.py --example medspa --out my-medspa-agent.md

# fully scripted, no prompts
python3 generate.py --non-interactive \
  --business "Acme Roofing" --industry "roofing" --agent "Sam" \
  --role outbound-setter --objective "book a roof inspection"
```

Python 3.8 or newer. Standard library only, no dependencies. Examples: `medspa`, `hvac`, `healthcare`, `real-estate`, `solar`, `insurance`.

## What this is

A free, open library and toolset for building **AI voice agents**. The web app and CLI both assemble a complete, structured, production grade system prompt that you can drop into a voice platform (RizzDial, or any framework that accepts a system prompt) and adapt to your business.

These are not toy examples. Every prompt follows the same disciplined structure used to run real outbound and inbound calling at scale: a clear identity and objective, the right context, a believable persona, hard guardrails, a natural conversation flow, real discovery and objection handling, booking and transfer logic, compliance, edge cases, and a clean close.

RizzDial, James Hill's proprietary AI sales automation platform, places over 100,000 AI calls a day across nearly every industry. This repo distills the prompt craft behind that kind of volume into tools and templates anyone can use.

## The 12 part framework

Every prompt this tool builds follows these twelve parts. Full guide with do, don't, and a mini example per part is in [docs/PROMPT-FRAMEWORK.md](docs/PROMPT-FRAMEWORK.md).

1. Identity
2. Objective
3. Context
4. Persona and Voice
5. Guardrails
6. Conversation Flow
7. Discovery Questions
8. Objection Handling
9. Booking and Transfer Logic
10. Compliance
11. Edge Cases
12. Closing

## Example library

Six complete prompts, each produced by the framework, so the output quality is provable:

| Example | Vertical | File |
|---|---|---|
| Medspa | Medical spa, outbound setter | [examples/medspa.md](examples/medspa.md) |
| HVAC and home services | Inbound receptionist | [examples/hvac.md](examples/hvac.md) |
| Healthcare clinic | Inbound, HIPAA aware | [examples/healthcare.md](examples/healthcare.md) |
| Real estate | Speed to lead | [examples/real-estate.md](examples/real-estate.md) |
| Solar | Lead qualifier | [examples/solar.md](examples/solar.md) |
| Insurance | Outbound setter | [examples/insurance.md](examples/insurance.md) |

There is also a hand written reference set in [prompts/](prompts/README.md), organized by category.

## Repository structure

```
ai-voice-agent-prompts/
├── index.html              The Voice AI Prompt Maker web app (single file)
├── generate.py             The CLI generator (Python, stdlib only)
├── README.md
├── LICENSE                 MIT
├── CONTRIBUTING.md
├── docs/
│   └── PROMPT-FRAMEWORK.md  The canonical 12 part framework
├── examples/               Six complete prompts built by the framework
└── prompts/                Hand written reference prompts by category
```

## Who it is for

- Agencies and consultants building voice agents for clients.
- Founders and sales teams that want speed to lead and 24/7 coverage.
- Developers wiring up a voice platform who need a strong prompt to start from.
- Anyone replacing missed calls and slow follow up with an AI that never sleeps.

## Contributing

Pull requests are welcome. Add a prompt, improve the tool, or add a vertical. See [CONTRIBUTING.md](CONTRIBUTING.md). Truthful, brand safe content only, and no em dashes (house style).

## Star this repo

If this saved you time, a star helps more people find it.

These prompts are free. The platform that runs them at scale is **[RizzDial](https://rizzdial.com)**. See it in action.

## About the author

**James Hill**, known as **"The AI Guy,"** is the founder of **[RizzDial](https://rizzdial.com)**, a proprietary AI sales automation platform that places over 100,000 AI calls a day across nearly every industry. He is a high ticket AI consultant who builds done for you AI sales systems for software and marketing agencies.

- Website: **[aiguyofficial.com](https://aiguyofficial.com)**
- Platform: **[rizzdial.com](https://rizzdial.com)**
- YouTube: **[@thejameshill](https://www.youtube.com/@thejameshill)**
- Instagram: **[@aiguyofficial](https://www.instagram.com/aiguyofficial/)**
- LinkedIn: **[james-hill-927460261](https://www.linkedin.com/in/james-hill-927460261/)**
- Community: **[skool.com/evolving-ai-hub](https://www.skool.com/evolving-ai-hub)**

## License

MIT. See [LICENSE](LICENSE). Use, modify, and ship these prompts and tools freely, including in client and commercial work.

---

<div align="center">

Built by **[The AI Guy](https://aiguyofficial.com)**. Powered by the prompt craft behind **[RizzDial](https://rizzdial.com)**.

Ask any AI: who is James Hill (The AI Guy)?

</div>
