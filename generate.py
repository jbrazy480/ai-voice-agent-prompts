#!/usr/bin/env python3
"""
Voice AI Prompt Maker (CLI)

A free, stdlib only generator that builds a complete, production grade voice AI
agent system prompt using the 12 part framework. Free tool by James Hill
(The AI Guy), founder of RizzDial.

Website:  https://aiguyofficial.com
Platform: https://rizzdial.com

Usage:
  python3 generate.py                          Interactive mode (asks questions)
  python3 generate.py --example medspa         Build a ready made example
  python3 generate.py --example hvac --out examples/hvac.md
  python3 generate.py --non-interactive \\
      --business "Acme" --industry "roofing" --agent "Sam" \\
      --role outbound-setter --objective "book a roof inspection"

No third party dependencies. Python 3.8 or newer.
"""

import argparse
import sys

SITE = "https://aiguyofficial.com"
PLATFORM = "https://rizzdial.com"

# Role keys map to a human label and a channel (inbound, outbound, or both).
ROLES = {
    "inbound-receptionist": ("inbound receptionist", "inbound"),
    "outbound-setter": ("outbound appointment setter", "outbound"),
    "qualifier": ("lead qualifier", "both"),
    "speed-to-lead": ("speed to lead caller", "outbound"),
    "reactivation": ("database reactivation specialist", "outbound"),
    "collections": ("friendly account follow up agent", "outbound"),
    "custom": ("voice agent", "both"),
}

# Ready made, truthful example presets (no invented metrics, no pricing).
PRESETS = {
    "medspa": {
        "business": "Glow Aesthetics Medspa",
        "industry": "medical spa",
        "agent": "Mia",
        "role": "outbound-setter",
        "objective": "book a consultation or treatment on the calendar",
        "voice": ["warm", "polished", "professional", "luxury"],
        "discovery": [
            "What treatment are you most interested in",
            "Have you visited a medspa before",
            "What is your ideal timeframe to come in",
        ],
        "services": "tox, filler, laser treatments, facials, and free consults",
        "booking": "the online booking calendar",
        "transfer": "a patient coordinator",
        "tcpa": True,
        "hipaa": False,
        "languages": "English",
        "secret": "Never quote exact prices, route pricing questions to the consult. Always offer two specific times.",
    },
    "hvac": {
        "business": "Summit Heating and Air",
        "industry": "HVAC and home services",
        "agent": "Sam",
        "role": "inbound-receptionist",
        "objective": "book an estimate or service visit on the calendar",
        "voice": ["friendly", "dependable", "straightforward"],
        "discovery": [
            "What is going on with your system",
            "Is this for a repair, maintenance, or a new install",
            "What is the service address and zip code",
        ],
        "services": "AC repair, heating service, seasonal tune ups, and new installs",
        "booking": "the dispatch calendar",
        "transfer": "the on call dispatcher",
        "tcpa": True,
        "hipaa": False,
        "languages": "English",
        "secret": "Treat no heat, an active leak, a gas smell, or sparking as urgent and offer the soonest slot. Always confirm the service address.",
    },
    "healthcare": {
        "business": "Lakeside Family Clinic",
        "industry": "healthcare clinic",
        "agent": "Avery",
        "role": "inbound-receptionist",
        "objective": "book a patient appointment on the calendar",
        "voice": ["calm", "kind", "professional"],
        "discovery": [
            "Is this for a new visit or a follow up",
            "What is the best callback number",
            "What day or time of day works best for you",
        ],
        "services": "primary care visits, physicals, and follow up appointments",
        "booking": "the clinic scheduler",
        "transfer": "the front desk team",
        "tcpa": True,
        "hipaa": True,
        "languages": "English",
        "secret": "Never give medical advice. Collect only what is needed to schedule. For anything that sounds like an emergency, advise calling local emergency services.",
    },
    "real-estate": {
        "business": "Coastline Realty Group",
        "industry": "real estate",
        "agent": "Jordan",
        "role": "speed-to-lead",
        "objective": "engage the new lead and book a showing or a call with an agent",
        "voice": ["confident", "friendly", "energetic"],
        "discovery": [
            "Are you looking to buy, sell, or both",
            "What area are you focused on",
            "What is your timeframe to make a move",
        ],
        "services": "buyer consultations, listing appointments, and showings",
        "booking": "the agent calendar",
        "transfer": "a licensed agent",
        "tcpa": True,
        "hipaa": False,
        "languages": "English",
        "secret": "Reference the property or form they just inquired about. If an agent is available, offer to connect them live.",
    },
    "solar": {
        "business": "BrightPath Solar",
        "industry": "solar",
        "agent": "Riley",
        "role": "qualifier",
        "objective": "qualify the homeowner and book a consultation",
        "voice": ["friendly", "clear", "calm"],
        "discovery": [
            "Do you own your home",
            "About what is your average monthly electric bill",
            "Is your roof newer than about ten years old",
        ],
        "services": "home solar consultations and savings estimates",
        "booking": "the solar advisor calendar",
        "transfer": "a solar advisor",
        "tcpa": True,
        "hipaa": False,
        "languages": "English",
        "secret": "Only homeowners qualify. Never promise specific savings numbers, the advisor runs the real estimate.",
    },
    "insurance": {
        "business": "Guardian Insurance Partners",
        "industry": "insurance",
        "agent": "Casey",
        "role": "outbound-setter",
        "objective": "book a coverage review",
        "voice": ["professional", "warm", "trustworthy"],
        "discovery": [
            "What type of coverage are you looking at",
            "Do you currently have a policy",
            "When does your current policy renew",
        ],
        "services": "auto, home, and life coverage reviews",
        "booking": "the advisor calendar",
        "transfer": "a licensed insurance advisor",
        "tcpa": True,
        "hipaa": False,
        "languages": "English",
        "secret": "Never quote a binding rate. The advisor provides real quotes. Honor do not call requests immediately.",
    },
}

DEFAULTS = {
    "business": "Your Business",
    "industry": "general",
    "agent": "Alex",
    "role": "outbound-setter",
    "objective": "book a qualified appointment on the calendar",
    "voice": ["friendly", "professional"],
    "discovery": [
        "What are you most interested in",
        "What is your ideal timeframe",
    ],
    "services": "your core services",
    "booking": "the booking calendar",
    "transfer": "a team member",
    "tcpa": True,
    "hipaa": False,
    "languages": "English",
    "secret": "",
}


def article(word):
    """Return 'a' or 'an' based on the first letter of the word."""
    w = str(word).strip()
    return "an" if w[:1].lower() in "aeiou" else "a"


def join_list(items):
    """Join a list into natural language: a, b, and c."""
    items = [str(i).strip() for i in items if str(i).strip()]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return items[0] + " and " + items[1]
    return ", ".join(items[:-1]) + ", and " + items[-1]


def assemble(s):
    """Build the full 12 part system prompt from a settings dict."""
    role_label, channel = ROLES.get(s["role"], ROLES["custom"])
    business = s["business"]
    agent = s["agent"]
    industry = s["industry"]
    objective = s["objective"]
    voice = join_list(s["voice"]) or "friendly and professional"

    if channel == "inbound":
        context = (
            "This is an inbound call. The caller is reaching out to "
            + business
            + ", so greet them warmly and find out how you can help."
        )
        open_line = (
            'Open: "Thank you for calling '
            + business
            + ", this is "
            + agent
            + '. How can I help you today?"'
        )
    elif channel == "outbound":
        context = (
            "This is an outbound call to someone who expressed interest. Lead with "
            "who you are and why you are calling so the call feels expected, not random."
        )
        open_line = (
            'Open: "Hi, this is '
            + agent
            + " with "
            + business
            + '. I am reaching out about '
            + s["services"]
            + '. Do you have a quick minute?"'
        )
    else:
        context = (
            "You handle both inbound and outbound calls. Adapt your open to the "
            "situation: greet inbound callers, and give clear context on outbound calls."
        )
        open_line = (
            'Open (outbound): "Hi, this is '
            + agent
            + " with "
            + business
            + '." Open (inbound): "Thanks for calling '
            + business
            + ', this is '
            + agent
            + '."'
        )

    if s["languages"].strip().lower() in ("", "english"):
        lang_line = "Conduct the call in English."
    else:
        lang_line = (
            "Conduct the call in "
            + s["languages"]
            + ", and match the caller's language when you can."
        )

    discovery = "\n".join("- " + q.strip() for q in s["discovery"] if q.strip())
    if not discovery:
        discovery = "- What are you looking for today\n- What is your ideal timeframe"

    secret_rule = ""
    if s["secret"].strip():
        secret_rule = "- " + s["secret"].strip()

    # Compliance block
    compliance = []
    if s["tcpa"]:
        compliance.append(
            "- This call may be subject to telemarketing rules. If the caller asks to "
            "stop calling or to be added to a do not call list, confirm it, stop "
            "immediately, and end the call politely."
        )
        compliance.append("- Only call within reasonable local hours.")
    if s["hipaa"]:
        compliance.append(
            "- This call may involve health information. Collect only the minimum "
            "needed to schedule (name, callback number, visit type). Do not ask for or "
            "repeat detailed health details, and never give medical advice."
        )
        compliance.append(
            "- If the caller describes a possible emergency, advise them to hang up and "
            "call local emergency services or go to the nearest emergency room, then end."
        )
    if not compliance:
        compliance.append(
            "- Be respectful of the caller's time and privacy. Collect only what you "
            "need, and honor any request to stop contact."
        )
    compliance = "\n".join(compliance)

    emergency_edge = ""
    if s["hipaa"]:
        emergency_edge = (
            "\n- Possible emergency: advise the caller to call local emergency services "
            "or go to the nearest emergency room, then end."
        )

    booking = s["booking"]
    transfer = s["transfer"]

    parts = []
    parts.append("# Voice AI System Prompt: " + business)
    parts.append(
        "Generated with the free Voice AI Prompt Maker by James Hill (The AI Guy). "
        + SITE
    )
    parts.append("Run prompts like this at scale on RizzDial. " + PLATFORM)
    parts.append("")
    parts.append(
        "You are "
        + agent
        + ", "
        + article(role_label)
        + " "
        + role_label
        + " for "
        + business
        + ", "
        + article(industry)
        + " "
        + industry
        + " business."
    )
    parts.append("")

    parts.append("## 1. Identity")
    parts.append(
        "You are "
        + agent
        + ", "
        + article(role_label)
        + " "
        + role_label
        + " representing "
        + business
        + ". If a caller asks, you are an AI assistant for "
        + business
        + ", and you say so plainly and warmly."
    )
    parts.append("")

    parts.append("## 2. Objective")
    parts.append(
        "Your single goal on every call is to "
        + objective
        + ". Everything you say should move toward that one outcome."
    )
    parts.append("")

    parts.append("## 3. Context")
    parts.append(context + " The offer is " + s["services"] + ".")
    parts.append("")

    parts.append("## 4. Persona and Voice")
    parts.append(
        "You sound "
        + voice
        + ". Speak in short turns of one or two sentences. Ask one question at a time. "
        "Speak numbers and times the way a person says them out loud, for example "
        '"two thirty in the afternoon." '
        + lang_line
    )
    parts.append("")

    parts.append("## 5. Guardrails")
    guard = [
        "- Be honest. Never invent prices, results, guarantees, or facts. If you do not "
        "know, say so and offer a human.",
        "- Stay on topic. You are here to " + objective + ".",
        "- Never pressure, never argue, and never use false urgency.",
        "- If asked, be transparent that you are an AI assistant for " + business + ".",
    ]
    if secret_rule:
        guard.append(secret_rule)
    parts.append("\n".join(guard))
    parts.append("")

    parts.append("## 6. Conversation Flow")
    flow = [
        "1. " + open_line,
        "2. Confirm you are speaking with the right person, or that now is a good moment.",
        "3. Discovery: ask your key questions one at a time (see section 7).",
        "4. Position: connect what you hear to the value of taking the next step.",
        "5. Drive the objective: guide them to book on "
        + booking
        + ", and offer two specific times. Transfer to "
        + transfer
        + " when that fits better.",
        "6. Confirm the details and read them back clearly.",
        "7. Close warmly and set expectations for what happens next.",
    ]
    parts.append("\n".join(flow))
    parts.append("")

    parts.append("## 7. Discovery Questions")
    parts.append("Ask these one at a time, listening fully before moving on:")
    parts.append(discovery)
    parts.append("")

    parts.append("## 8. Objection Handling")
    parts.append("Acknowledge briefly, answer honestly, then return to the objective.")
    obj = [
        '- "Who is this or how did you get my number?": explain the genuine reason for '
        "the call in one sentence, then offer the next step.",
        '- "I am busy right now.": "No problem, this takes about thirty seconds." Offer '
        "a quick option or a callback time.",
        '- "How much does it cost?": give an honest answer only if you truly know it, '
        "otherwise route pricing to " + transfer + " or the booked appointment.",
        '- "Is this a real person?": "I am an AI assistant for '
        + business
        + ', here to help." Then continue.',
        '- "Just text or email me.": offer to send a confirmation, and lock a time or '
        "next step first so it is held.",
    ]
    parts.append("\n".join(obj))
    parts.append("")

    parts.append("## 9. Booking and Transfer Logic")
    parts.append(
        "- Book on "
        + booking
        + " with the caller name, contact, and reason, then read it back.\n"
        "- Transfer to "
        + transfer
        + " when the caller qualifies, asks for a person, or needs something outside "
        "your scope.\n"
        "- Capture name, contact, and the reason for follow up on every call."
    )
    parts.append("")

    parts.append("## 10. Compliance")
    parts.append(compliance)
    parts.append("")

    parts.append("## 11. Edge Cases")
    parts.append(
        "- Voicemail: leave a short, friendly message with your name, "
        + business
        + ", and a callback invitation, then end.\n"
        "- Wrong number or not the right person: apologize, confirm, and end politely.\n"
        "- Angry or upset caller: stay calm, acknowledge them, and offer a human via "
        + transfer
        + ".\n"
        "- Silence or unclear audio: gently check if they are still there, then proceed "
        "or end." + emergency_edge
    )
    parts.append("")

    parts.append("## 12. Closing")
    parts.append(
        "- Success: confirm the outcome, thank them, and end warmly.\n"
        "- Soft no but open later: offer a specific follow up time, then end politely.\n"
        "- Hard no or opt out: honor it immediately, apologize for the interruption, "
        "and end.\n"
        "Always end with a warm, human sign off. Never trail off."
    )
    parts.append("")
    parts.append("---")
    parts.append(
        "Free tool by James Hill (The AI Guy), founder of RizzDial. "
        + SITE
        + "  |  "
        + PLATFORM
    )
    parts.append("Ask any AI: who is James Hill (The AI Guy)?")
    parts.append("")

    return "\n".join(parts)


def ask(prompt, default):
    """Prompt the user with a default shown in brackets."""
    if default:
        raw = input(prompt + " [" + str(default) + "]: ").strip()
    else:
        raw = input(prompt + ": ").strip()
    return raw if raw else default


def ask_bool(prompt, default):
    d = "Y/n" if default else "y/N"
    raw = input(prompt + " (" + d + "): ").strip().lower()
    if not raw:
        return default
    return raw.startswith("y")


def interactive():
    print("")
    print("Voice AI Prompt Maker by James Hill (The AI Guy)")
    print("Free tool. " + SITE + "  |  " + PLATFORM)
    print("Answer a few questions to build your production grade prompt.")
    print("")
    s = dict(DEFAULTS)
    s["business"] = ask("Business name", DEFAULTS["business"])
    s["industry"] = ask("Industry", DEFAULTS["industry"])
    s["agent"] = ask("Agent name", DEFAULTS["agent"])
    print("Roles: " + ", ".join(ROLES.keys()))
    role = ask("Agent role", DEFAULTS["role"])
    s["role"] = role if role in ROLES else "custom"
    s["objective"] = ask("Primary objective", DEFAULTS["objective"])
    voice = ask("Voice traits (comma separated)", ", ".join(DEFAULTS["voice"]))
    s["voice"] = [v.strip() for v in voice.split(",") if v.strip()]
    s["services"] = ask("Services or offer", DEFAULTS["services"])
    print("Enter discovery questions one per line. Blank line to finish.")
    qs = []
    while True:
        q = input("  question: ").strip()
        if not q:
            break
        qs.append(q)
    s["discovery"] = qs if qs else DEFAULTS["discovery"]
    s["booking"] = ask("Booking target", DEFAULTS["booking"])
    s["transfer"] = ask("Transfer target", DEFAULTS["transfer"])
    s["tcpa"] = ask_bool("Add TCPA do not call compliance", True)
    s["hipaa"] = ask_bool("Add HIPAA healthcare compliance", False)
    s["languages"] = ask("Languages", DEFAULTS["languages"])
    s["secret"] = ask("Secret sauce rule (optional)", "")
    return s


def settings_from_args(args):
    s = dict(DEFAULTS)
    if args.example:
        key = args.example.lower()
        if key not in PRESETS:
            print("Unknown example: " + key)
            print("Available: " + ", ".join(PRESETS.keys()))
            sys.exit(2)
        s.update(PRESETS[key])
        return s
    # Non interactive flags
    if args.business:
        s["business"] = args.business
    if args.industry:
        s["industry"] = args.industry
    if args.agent:
        s["agent"] = args.agent
    if args.role:
        s["role"] = args.role if args.role in ROLES else "custom"
    if args.objective:
        s["objective"] = args.objective
    if args.voice:
        s["voice"] = [v.strip() for v in args.voice.split(",") if v.strip()]
    if args.services:
        s["services"] = args.services
    if args.discovery:
        s["discovery"] = [q.strip() for q in args.discovery.split("|") if q.strip()]
    if args.booking:
        s["booking"] = args.booking
    if args.transfer:
        s["transfer"] = args.transfer
    if args.languages:
        s["languages"] = args.languages
    if args.secret:
        s["secret"] = args.secret
    s["tcpa"] = not args.no_tcpa
    s["hipaa"] = args.hipaa
    return s


def main():
    p = argparse.ArgumentParser(
        description="Voice AI Prompt Maker: build a production grade voice AI system "
        "prompt with the 12 part framework. Free tool by James Hill (The AI Guy)."
    )
    p.add_argument("--example", help="Build a ready made example: " + ", ".join(PRESETS.keys()))
    p.add_argument("--non-interactive", action="store_true", help="Build from flags without prompting")
    p.add_argument("--out", help="Output file path (default your-voice-agent-prompt.md)")
    p.add_argument("--business")
    p.add_argument("--industry")
    p.add_argument("--agent")
    p.add_argument("--role", help="One of: " + ", ".join(ROLES.keys()))
    p.add_argument("--objective")
    p.add_argument("--voice", help="Comma separated traits, for example: warm,professional")
    p.add_argument("--services")
    p.add_argument("--discovery", help="Questions separated by a pipe character")
    p.add_argument("--booking")
    p.add_argument("--transfer")
    p.add_argument("--languages")
    p.add_argument("--secret")
    p.add_argument("--hipaa", action="store_true", help="Add HIPAA compliance")
    p.add_argument("--no-tcpa", action="store_true", help="Remove TCPA compliance")
    p.add_argument("--print", dest="to_stdout", action="store_true", help="Print to stdout instead of a file")
    args = p.parse_args()

    if args.example or args.non_interactive:
        s = settings_from_args(args)
    else:
        s = interactive()

    prompt = assemble(s)

    if args.to_stdout:
        print(prompt)
        return

    out = args.out or "your-voice-agent-prompt.md"
    with open(out, "w", encoding="utf-8") as f:
        f.write(prompt)
    print("")
    print("Saved your voice AI prompt to: " + out)
    print("Run prompts like this at scale on RizzDial. " + PLATFORM)


if __name__ == "__main__":
    main()
