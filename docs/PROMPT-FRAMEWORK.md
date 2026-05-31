# The 12 Part Voice AI Prompt Framework

The canonical framework behind this repo, the [Prompt Maker web app](../index.html), and the [CLI generator](../generate.py). Written by **James Hill ("The AI Guy")**, founder of **[RizzDial](https://rizzdial.com)**. More at **[aiguyofficial.com](https://aiguyofficial.com)**.

Most voice agents fail because the prompt was written like a chatbot prompt. Voice is real time, spoken, and unforgiving. It cannot show a wall of text, cannot rely on the caller re reading, and has to handle interruptions, silence, and detours. A great voice agent prompt has twelve parts. Skip one and the agent gets worse in a specific, predictable way.

---

## 1. Identity

Who the agent is. Name, role, and the company it represents. This anchors everything else.

- **Do:** "You are Mia, a scheduling coordinator for Glow Aesthetics Medspa."
- **Do:** state that, if asked, the agent is an AI assistant for the business, said plainly and warmly.
- **Don't:** leave the agent nameless or vague about who it works for.

Mini example: "You are Avery, a patient coordinator for Lakeside Family Clinic."

## 2. Objective

One measurable outcome. A voice agent with two goals achieves neither.

- **Do:** "Your single goal on every call is to book a consultation on the calendar."
- **Don't:** stack goals like "book, upsell, survey, and collect feedback" into one call.

Mini example: "Your single goal is to qualify the homeowner and book a consultation."

## 3. Context

Why this call is happening. Inbound or outbound, the lead source, the offer, the hours. Context is what makes the open feel expected instead of random.

- **Do:** "This is an outbound call to someone who filled out a form about solar. Lead with who you are and why you are calling."
- **Don't:** drop the agent into a call with no situational awareness.

Mini example: "This is an inbound call. The caller is reaching out to the clinic, so greet them and find out how you can help."

## 4. Persona and Voice

How the agent sounds. Tone, speaking style, and pace. The goal is a believable human presence, not a script reader.

- **Do:** define tone (warm, confident, efficient), short turns of one or two sentences, one question at a time, and numbers spoken naturally ("two thirty in the afternoon").
- **Don't:** allow long paragraphs, stacked questions, or robotic phrasing.

Mini example: "You sound warm, polished, and professional. Keep turns to one or two sentences."

## 5. Guardrails

What the agent must never do. This protects the brand and the caller.

- **Do:** require honesty (never invent prices, results, or facts), keep the agent in scope, and ban pressure, arguing, and false urgency.
- **Don't:** let the agent guess at things it does not know. It should say so and offer a human.

Mini example: "Never quote exact prices. Route pricing to the consult or a human."

## 6. Conversation Flow

The path from hello to goodbye, written as steps the agent follows while staying flexible.

- **Do:** open, confirm the right person, discover, position, drive the objective with two specific time options, confirm, close.
- **Don't:** ask "when works for you" with no options. Offer two concrete times.

Mini example: "Offer Thursday at eleven or Friday at three, then confirm and read it back."

## 7. Discovery Questions

The specific questions that surface need and fit. Asked one at a time, with real listening between them.

- **Do:** pick three to four questions that matter, like situation, timeline, decision role, and scope.
- **Don't:** interrogate. A discovery flow is a conversation, not a form.

Mini example: "Do you own your home. About what is your average monthly electric bill."

## 8. Objection Handling

Real responses to real pushback. Acknowledge briefly, answer honestly, return to the objective.

- **Do:** prepare the common ones: "who is this," "I am busy," "how much," "is this a real person," "just text me."
- **Don't:** argue or repeat the same line. One honest redirect, then respect the answer.

Mini example: "I am busy." Reply: "No problem, this takes about thirty seconds. Mornings or afternoons?"

## 9. Booking and Transfer Logic

What the agent actually does during the call, and exactly when.

- **Do:** name the booking target and the transfer target, with clear triggers. Capture name, contact, and reason every time.
- **Don't:** leave the action ambiguous. Spell out the trigger: "When they agree to a time, book it and read it back."

Mini example: "Transfer to a licensed agent when the caller qualifies or asks for a person."

## 10. Compliance

The rules that keep the calling legal and respectful. This varies by industry and region.

- **Do:** for outbound, honor do not call and opt out requests immediately, and call within reasonable hours. For healthcare, collect the minimum needed to schedule, never give medical advice, and route emergencies to local emergency services.
- **Don't:** ignore opt outs or collect sensitive details you do not need.

Mini example: "If the caller asks to stop calling, confirm it, stop immediately, and end politely."

## 11. Edge Cases

The non happy paths. Plan for them or the agent improvises badly.

- **Do:** cover voicemail, wrong number, not the right person, angry caller, silence or bad audio, and (for healthcare) a possible emergency.
- **Don't:** let the agent hang on awkwardly or loop when something goes off script.

Mini example: "Voicemail: leave a short friendly message with your name, the business, and a callback invitation, then end."

## 12. Closing

Exactly how the call ends, for every outcome. Without this, agents ramble.

- **Do:** define success (confirm, thank, end), soft no (offer a follow up time), and hard no or opt out (honor it, apologize, end). Always end with a warm sign off.
- **Don't:** let the agent trail off or fail to set expectations for what happens next.

Mini example: "Confirm the time, mention the confirmation text, thank them, and end warmly."

---

## Ship checklist

- One objective, stated once.
- Identity and context set up front.
- Persona sounds like a real top performer.
- Turns are one to two sentences, one question at a time.
- Numbers and times spoken naturally.
- Every common objection has a one line answer.
- Booking and transfer triggers are explicit.
- Compliance fits the industry and region.
- Edge cases handled, including voicemail.
- Clear closing for every outcome.

Build it with the [Prompt Maker](../index.html) or the [CLI](../generate.py), test it on live calls, and refine from the transcripts. That feedback loop is how a prompt gets sharp.

Built by **[The AI Guy](https://aiguyofficial.com)**. Powered by the prompt craft behind **[RizzDial](https://rizzdial.com)**.
