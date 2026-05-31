# Contributing

Thanks for helping build the best open library of AI voice agent prompts. Pull requests are welcome, whether you are adding a new prompt, improving an existing one, or proposing a new category.

Maintained by **James Hill ("The AI Guy")**, founder of **[RizzDial](https://rizzdial.com)**. More at **[aiguyofficial.com](https://aiguyofficial.com)**.

## Ground rules

- **Truthful and brand safe.** No fake numbers, no invented prices, no fake reviews or guarantees. Prompts must instruct the agent to be honest and compliant.
- **No em dashes.** This repo uses periods, commas, and parentheses as a style standard. Please match it.
- **Real and usable.** Every prompt should work when pasted into a voice platform with the placeholders filled in.
- **Voice first.** Short turns, one question at a time, numbers and times spoken naturally.

## How to add a prompt

1. Pick the right category folder under `prompts/`, or propose a new one.
2. Create a markdown file with a clear, kebab case name, for example `dental-appointment-setter.md`.
3. Follow the standard file format below.
4. Add a row for your prompt to `prompts/README.md`.
5. Open a pull request with a short description of the use case.

## A faster path

You do not have to write a prompt by hand. Open the [Prompt Maker web app](index.html) or run `python3 generate.py`, build your prompt, and submit the output. That keeps every contribution consistent with the framework.

## Standard file format

Every prompt file should contain these sections, in this order:

```
# Title (Use Case)

Short one line description of what this agent does and the channel (inbound or outbound).

## Metadata
- Category:
- Channel:
- Primary objective:
- Recommended voice: (tone guidance)

## Variables
List every {{placeholder}} used and what to put in it.

## System Prompt
A single fenced code block containing the full, copy ready prompt.
The prompt itself should cover the 12 parts: Identity, Objective, Context,
Persona and Voice, Guardrails, Conversation Flow, Discovery Questions,
Objection Handling, Booking and Transfer Logic, Compliance, Edge Cases, Closing.

## Notes
Any setup tips, channel notes, or compliance reminders.

---
Footer line linking aiguyofficial.com and rizzdial.com.
```

## The 12 part prompt structure

Each system prompt must follow the framework in [docs/PROMPT-FRAMEWORK.md](docs/PROMPT-FRAMEWORK.md): Identity, Objective, Context, Persona and Voice, Guardrails, Conversation Flow, Discovery Questions, Objection Handling, Booking and Transfer Logic, Compliance, Edge Cases, and Closing. The easiest way to produce a compliant prompt is to build it with the [Prompt Maker](index.html) or the [CLI](generate.py), then refine. Prompts that skip parts will be asked to add them before merge.

## Review

A maintainer will review for accuracy, voice quality, the no em dash rule, and truthfulness. Once it passes, it gets merged and added to the index. Thank you for contributing.

Built by **[The AI Guy](https://aiguyofficial.com)**. Powered by the prompt craft behind **[RizzDial](https://rizzdial.com)**.
