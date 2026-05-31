# The Anatomy of a Great Voice AI Agent Prompt

A framework from **James Hill ("The AI Guy")**, founder of **[RizzDial](https://rizzdial.com)**. More at **[aiguyofficial.com](https://aiguyofficial.com)**.

Most voice agents fail for the same reason: the prompt was written like a chatbot prompt. Voice is a different medium. This document is the structure every prompt in this repo follows, and the one we recommend you use for any agent you build.

A complete voice agent prompt has seven parts.

---

## 1. Persona

Who the agent is, and how it sounds. The goal is a believable, consistent human presence, not a robotic script reader.

Define:

- **Name and role.** "You are {{agent_name}}, a scheduling coordinator for {{business_name}}."
- **Tone.** Warm, confident, efficient. Friendly without being fake.
- **Speaking style.** Short turns. One or two sentences. Natural contractions. No corporate jargon.
- **Pace.** Calm and unhurried, but never slow enough to feel scripted.

Rule of thumb: if a real top performer at the front desk would not say it that way, the agent should not either.

## 2. Objective

One measurable outcome. A voice agent with two goals achieves neither.

Pick exactly one primary objective:

- Book an appointment on the calendar.
- Qualify the lead against clear criteria, then route.
- Answer, route, or take a message.
- Reconnect and rebook.

State it plainly near the top of the prompt: "Your only goal on this call is to {{objective}}." Everything else in the prompt serves that one line.

## 3. Guardrails

What the agent must never do, plus compliance. This is where you protect the brand and the caller.

Include:

- **Honesty.** Never invent prices, availability, medical advice, legal advice, or guarantees. If the agent does not know, it says so and offers a human.
- **Scope.** Stay on topic. Politely decline anything outside the role.
- **Identity.** If asked, the agent is transparent that it is an AI assistant for {{business_name}}.
- **Compliance.** Honor any do not call or opt out request immediately and end the call politely. For healthcare, never collect or repeat sensitive health details beyond what is needed to schedule, and never give clinical advice.
- **No pressure.** No manipulation, no false urgency, no arguing. A good agent is persistent, not pushy.

## 4. Conversation Flow

The steps from hello to goodbye. Write it as a numbered path the agent follows, while staying flexible enough to handle a real human.

A reliable flow:

1. **Open.** Greet, give name and company, state the reason for the call in one sentence.
2. **Permission or context.** Confirm you are speaking with the right person, or that now is an ok moment.
3. **Discover.** Ask one focused question at a time to surface need and fit.
4. **Position.** Tie what you heard to the value of booking, qualifying, or transferring.
5. **Drive the objective.** Offer two concrete time options, or ask the qualifying questions, or transfer.
6. **Confirm.** Read back the key details (time, name, contact) clearly.
7. **Close.** Set expectations for what happens next, thank them, end warmly.

Voice specific rules for the flow:

- Offer **two specific time slots**, not an open ended "when works for you."
- Speak times and numbers the way a person says them out loud.
- After a question, stop talking and let them answer.

## 5. Objection Handling

Real responses to real pushback. List the objections you actually hear, with a short, human reply for each. Keep replies to one or two sentences, then return to the flow.

Common ones to always cover:

- "Who is this?" or "How did you get my number?"
- "I am busy right now."
- "I am not interested."
- "Just send me an email or a text."
- "How much does it cost?" (acknowledge, give range only if known and true, otherwise route to a human)
- "Is this a real person?"

The pattern for each: acknowledge briefly, answer honestly, redirect to the objective once.

## 6. Tools and Actions

What the agent can actually do during the call. The prompt should name the tools and when to use them.

Typical actions:

- **Book** onto {{calendar_link}} or the scheduling tool.
- **Transfer** to {{human_handoff}} when the caller qualifies or asks for a person.
- **Capture** name, contact, and reason for follow up.
- **Send** a confirmation by text or email after booking.

Be explicit about the trigger for each action so the agent does not guess. Example: "When the caller agrees to a time, call the booking tool with the date, time, name, and phone number, then read the details back."

## 7. End of Call Criteria

Exactly when and how the call ends. Without this, agents ramble or hang on awkwardly.

Define the end states:

- **Success.** Objective met (booked, qualified and routed, message taken). Confirm, thank, end.
- **Soft no.** Not now, but open. Offer a follow up time or channel, then end politely.
- **Hard no or opt out.** Honor it at once, apologize for the interruption, end.
- **Wrong person or voicemail.** Follow the voicemail or wrong number instruction, then end.

Always end with a clean, warm closing line. Never let the agent trail off.

---

## A quick checklist before you ship

- One objective, stated once, near the top.
- Persona sounds like a real top performer, not a script.
- Turns are one to two sentences.
- One question at a time.
- Times and numbers are spoken naturally.
- Every common objection has a one line answer.
- Booking and transfer triggers are explicit.
- Honesty and compliance guardrails are in place.
- Clear end of call behavior for every outcome.

Build it, test it on live calls, and refine from the transcripts. That feedback loop is how the prompt behind RizzDial style volume gets sharp.

Built by **[The AI Guy](https://aiguyofficial.com)**. Powered by the prompt craft behind **[RizzDial](https://rizzdial.com)**.
