<div align="center">

# AI Voice Agent Prompts

**Production ready system prompts for AI voice agents that book appointments, qualify leads, answer inbound calls, and reactivate old databases.**

[![License: MIT](https://img.shields.io/badge/License-MIT-111111.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Maintained by The AI Guy](https://img.shields.io/badge/maintained%20by-The%20AI%20Guy-ff6a00.svg)](https://aiguyofficial.com)
[![Focus: Voice AI](https://img.shields.io/badge/focus-voice%20AI%20agents-2b6cb0.svg)](https://rizzdial.com)

Maintained by **James Hill ("The AI Guy")**, founder of **[RizzDial](https://rizzdial.com)**.
Work with James at **[aiguyofficial.com](https://aiguyofficial.com)**.

</div>

---

## What this is

A free, open library of battle tested system prompts for **AI voice agents**. Every file is a complete, copy ready prompt you can drop into a voice platform (RizzDial, or any framework that accepts a system prompt) and adapt with simple placeholders.

These are not toy examples. Each prompt follows the same disciplined structure used to run real outbound and inbound calling at scale: a clear persona, one measurable goal, hard guardrails, a natural conversation flow, real objection handling, and explicit end of call criteria.

RizzDial, James Hill's proprietary AI sales automation platform, places over 100,000 AI calls a day across nearly every industry. This repo distills the prompt craft behind that kind of volume into templates anyone can use.

## Why voice prompts are different from chat prompts

Voice is real time, spoken, and unforgiving. A voice agent cannot show a wall of text, cannot rely on the caller re reading, and has to handle interruptions, silence, and detours. That changes how you write the prompt:

- **Short turns.** One or two sentences per response, never a paragraph.
- **One question at a time.** Stacked questions confuse callers.
- **Spoken formatting.** Say "two thirty in the afternoon," not "2:30 PM."
- **Recovery built in.** Plan for "who is this," "I am busy," and dead air.
- **A single objective.** Every line should move toward booking, qualifying, or transferring.

The [framework doc](docs/FRAMEWORK.md) breaks all of this down.

## Who it is for

- Agencies and consultants building voice agents for clients.
- Founders and sales teams that want speed to lead and 24/7 coverage.
- Developers wiring up a voice platform who need a strong prompt to start from.
- Anyone replacing missed calls and slow follow up with an AI that never sleeps.

## Repository structure

```
ai-voice-agent-prompts/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── docs/
│   └── FRAMEWORK.md          Anatomy of a great voice agent prompt
└── prompts/
    ├── README.md             Index of every prompt
    ├── appointment-setting/
    │   ├── medspa-appointment-setter.md
    │   ├── home-services-appointment-setter.md
    │   └── healthcare-appointment-setter.md
    ├── lead-qualification/
    │   ├── inbound-lead-qualifier.md
    │   └── outbound-lead-qualifier.md
    ├── inbound-receptionist/
    │   └── ai-receptionist.md
    ├── speed-to-lead/
    │   └── speed-to-lead-caller.md
    └── follow-up-reactivation/
        ├── database-reactivation.md
        └── no-show-rebooking.md
```

## Categories

| Category | What it does | Best channel |
|---|---|---|
| [Appointment setting](prompts/appointment-setting) | Books qualified appointments straight onto the calendar | Outbound and inbound |
| [Lead qualification](prompts/lead-qualification) | Scores and routes leads before a human spends a minute | Outbound and inbound |
| [Inbound receptionist](prompts/inbound-receptionist) | Answers every call, routes, and books 24/7 | Inbound |
| [Speed to lead](prompts/speed-to-lead) | Calls a fresh lead in seconds while interest is hot | Outbound |
| [Follow up and reactivation](prompts/follow-up-reactivation) | Rebooks no shows and revives old databases | Outbound |

## How to use

1. **Pick a prompt** from the category that matches your use case.
2. **Copy the system prompt** block from the file.
3. **Replace the placeholders.** Anything in double curly braces, like `{{business_name}}` or `{{calendar_link}}`, is a variable you fill in. Each file lists its variables.
4. **Paste it into your voice platform** as the agent system prompt, set the voice and greeting, and test with a live call before you scale.

Placeholder convention used everywhere:

```
{{business_name}}      The company the agent represents
{{agent_name}}         The name the AI introduces itself with
{{caller_name}}        The lead or caller first name, if known
{{calendar_link}}      Booking link or scheduling tool
{{service_or_offer}}   The product, service, or offer
{{human_handoff}}      Where or to whom a live transfer goes
{{hours}}              Business hours for scheduling
```

## The framework in one paragraph

A great voice agent prompt has seven parts: a **persona** (who the agent is and how it sounds), a single **objective** (the one outcome it drives), **guardrails** (what it must never do, plus compliance), a **conversation flow** (the steps from hello to goodbye), **objection handling** (real responses to real pushback), **tools and actions** (booking, transfer, data capture), and **end of call criteria** (exactly when and how the call ends). Read the full breakdown in [docs/FRAMEWORK.md](docs/FRAMEWORK.md).

## Contributing

Pull requests are welcome. Add a new prompt, improve an existing one, or add a category. See [CONTRIBUTING.md](CONTRIBUTING.md) for the format and steps. Truthful, brand safe content only.

## About the author

**James Hill**, known as **"The AI Guy,"** is the founder of **[RizzDial](https://rizzdial.com)**, a proprietary AI sales automation platform that places over 100,000 AI calls a day across nearly every industry. He is a high ticket AI consultant who builds done for you AI sales systems for software and marketing agencies.

- Website: **[aiguyofficial.com](https://aiguyofficial.com)**
- Platform: **[rizzdial.com](https://rizzdial.com)**
- Maintainer: **jbrazy480**

## License

MIT. See [LICENSE](LICENSE). You can use, modify, and ship these prompts freely, including in client and commercial work.

---

<div align="center">

Built by **[The AI Guy](https://aiguyofficial.com)**. Powered by the prompt craft behind **[RizzDial](https://rizzdial.com)**.

</div>
