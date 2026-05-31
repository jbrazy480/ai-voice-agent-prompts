# How to Build World-Class Voice AI Prompts in 5 Minutes

### The RizzDial Prompt Engine - Setup Guide for the Skool Community

---

## What Is This?

We built a tool that writes voice AI agent prompts for you. Not generic, robotic scripts - prompts with real sales psychology baked in from Hormozi, Belfort, Sandler, and 100,000+ calls per day on RizzDial.

You answer 7 questions about your business. It generates a complete, ready-to-paste prompt that makes your AI agent sound like the sharpest, most empathetic salesperson your leads have ever talked to.

**What you get:**
- A pattern-interrupt opener that stops people from hanging up
- Sales psychology that keeps them on the phone and moves them toward "yes"
- iPhone call screening so your agent doesn't pitch a robot
- Objection handling that uses real psychology (not scripted comebacks)
- The full prompt pre-sliced into 12 sections so you can paste it directly into the RizzDial builder

**No coding required. No prompting experience needed. Just answer the questions.**

---

## Step 1: Install Claude Code

Claude Code is a tool from Anthropic (the company that makes Claude AI). It runs in your terminal (the command line on your computer). Don't worry - you don't need to know how to code.

### On a Mac:

1. Open the **Terminal** app (search "Terminal" in Spotlight, or find it in Applications → Utilities)
2. Copy and paste this command, then press Enter:
```
npm install -g @anthropic-ai/claude-code
```
3. If you get an error about npm not being found, you need to install Node.js first. Go to https://nodejs.org and download the LTS version. Install it, then try the command above again.
4. Once installed, you can launch Claude Code by typing:
```
claude
```

### On Windows:

1. Open **Command Prompt** or **PowerShell** (search for it in the Start menu)
2. Copy and paste this command, then press Enter:
```
npm install -g @anthropic-ai/claude-code
```
3. If you get an error about npm not being found, install Node.js first from https://nodejs.org (LTS version). Then try again.
4. Launch Claude Code by typing:
```
claude
```

### First Time Setup:

When you run `claude` for the first time, it will ask you to log in with your Anthropic account. Follow the prompts - it takes about 30 seconds.

---

## Step 2: Download the Prompt Engine

This is where you get the files that power the skill.

### Option A: Download from GitHub (Easiest)

1. Go to: **https://github.com/jbrazy480/metatech-rizzdial**
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Unzip the folder somewhere you'll remember (like your Desktop or Documents)

### Option B: Clone with Git (If you know Git)

Open your terminal and run:
```
git clone https://github.com/jbrazy480/metatech-rizzdial.git
```

---

## Step 3: Install the Skill

The "skill" is what lets you type `/new-voice-ai-prompt` inside Claude Code and have it walk you through building a prompt. You need to copy one file to the right place.

### Find the file:

Inside the folder you just downloaded, find this file:
```
.claude/commands/new-voice-ai-prompt.md
```

**Can't see it?** The `.claude` folder is hidden by default.
- **Mac:** In Finder, press `Cmd + Shift + .` (period) to show hidden files
- **Windows:** In File Explorer, click View → Show → Hidden Items

### Copy it to your Claude Code commands folder:

**Option 1 - Make it available for ALL your projects (recommended):**

Mac:
```
mkdir -p ~/.claude/commands
cp /path/to/metatech-rizzdial/.claude/commands/new-voice-ai-prompt.md ~/.claude/commands/
```
Replace `/path/to/metatech-rizzdial/` with wherever you downloaded the folder.

Windows:
```
mkdir %USERPROFILE%\.claude\commands
copy "C:\path\to\metatech-rizzdial\.claude\commands\new-voice-ai-prompt.md" "%USERPROFILE%\.claude\commands\"
```

**Option 2 - Make it available for just one project:**

Create a `.claude/commands/` folder inside your project directory and copy the file there.

### Don't want to use the terminal? Do it manually:

1. On your computer, go to your home folder:
   - **Mac:** Open Finder → Go → Home (or press `Cmd + Shift + H`)
   - **Windows:** Open File Explorer → type `%USERPROFILE%` in the address bar
2. Look for a folder called `.claude` - if it doesn't exist, create it
3. Inside `.claude`, create a folder called `commands` - if it doesn't exist
4. Copy the `new-voice-ai-prompt.md` file into that `commands` folder

**That's it. The skill is installed.**

---

## Step 4: Run the Skill

1. Open your terminal
2. Navigate to the folder where you downloaded the prompt engine:
```
cd /path/to/metatech-rizzdial
```
3. Launch Claude Code:
```
claude
```
4. Type:
```
/new-voice-ai-prompt
```
5. Hit Enter

---

## Step 5: Answer 7 Questions

The skill will ask you 7 questions, one at a time. Here's what to expect and how to prepare:

### Question 1: Your Offer
**What it asks:** "Feed me the offer."
**What to paste:** Everything about what your business sells - who you sell to, pricing, pain points, what makes you different, your guarantee. The more detail the better. If you have an offer document, paste the whole thing.

**Pro tip:** Before running the skill, write up your offer in a Google Doc or note. Include:
- What you sell
- Who you sell to (be specific - not "everyone")
- Pricing
- What problem you solve
- What makes you different from competitors
- Any guarantees you offer

### Question 2: Your Marketing Strategy
**What it asks:** "Feed me the marketing strategy."
**What to paste:** How you get leads. What ads are you running? What do the ads say? What does your landing page look like? What did the prospect see or do before this AI agent calls them?

**If you don't have a formal strategy document**, just describe:
- Where your leads come from (Facebook ads, Google, referrals, website form, etc.)
- What the ad or post says that gets them to respond
- What form they fill out or action they take
- What they're expecting when they get called

### Question 3: Agent Name
**What it asks:** "What do you want to name the AI agent?"
**Just pick a human name.** Eric, Mikayla, Jordan, Sarah - whatever feels right for your brand.

### Question 4: Transfer or Booking
**What it asks:** "Should the agent transfer, book, or both?"
**Pick one:**
- **(A) Transfer** - agent qualifies the lead and transfers them to a live person on your team
- **(B) Book** - agent qualifies and books an appointment on your calendar
- **(C) Both** - tries to transfer first, books an appointment if nobody's available (most common)

### Question 5: Company Name & Industry
**What it asks:** "What company and what industry?"
**Just tell it.** Example: "Bright Smile Dental - dental practice" or "ABC Solar - residential solar installation"

### Question 6: Timezone & Business Hours
**What it asks:** "What timezone and hours?"
**Example:** "America/New_York, Mon-Fri 9am-6pm ET, Sat 9am-2pm ET"

### Question 7: AI Disclosure
**What it asks:** "How should the agent respond when asked 'Are you AI?'"
**Pick one:**
- **(A) Truthful:** "Yes, I'm a virtual assistant for [your company]"
- **(B) Stay in character:** "I'm [name] with [company], I help with [thing]"
- **(C) Custom:** Tell it exactly what you want the agent to say

---

## Step 6: Get Your Prompt

After you answer all 7 questions, Claude will generate your complete prompt. It comes out in 12 sections, each labeled with `=== Section Name ===`.

**Each section maps to one input field in the RizzDial builder:**

| Section # | Section Name | Where to Paste |
|---|---|---|
| 1 | Project Instructions / Request | First field in the builder |
| 2 | Greetings | Second field |
| 3 | Call Flow | Third field |
| 4 | Character | Fourth field |
| 5 | Transfer Call | Fifth field |
| 6 | Critical Instructions / Guardrails | Sixth field |
| 7 | Custom Field References | Seventh field |
| 8 | What Your Company Does | Eighth field |
| 9 | Script | Ninth field |
| 10 | Objection Handling | Tenth field |
| 11 | Booking flow | Eleventh field |
| 12 | FAQ / Knowledge Base | Twelfth field |

**Just copy each section and paste it into the matching field. That's it.**

---

## What's Built Into Every Prompt

You don't need to know any of this - it's already baked in. But here's what makes these prompts different from anything you'd write yourself or get from ChatGPT:

**Sales Psychology:**
- Pattern-interrupt openers that stop people from hanging up
- The "Time Contract" - tells them exactly how long the call will take (builds trust)
- SPIN discovery - qualification questions that uncover real pain, not just checkboxes
- Loss aversion math - shows them what they're LOSING by not acting (2x more motivating than showing gains)
- The "Assumptive Bridge" - never asks IF they want to proceed, asks WHEN and HOW
- The "Silence Bomb" - ends every call with a question then 5 seconds of silence, which gets prospects to reveal their real objection

**Human-Sounding Voice:**
- Natural "um," "uh," "gotcha," "mmhmm" woven into the script
- Varied pacing - short sentences mixed with longer ones
- Real human reactions - "Oh, no kidding," "Wait, really?" "Yeah, that's tough"
- The agent never sounds like it's reading a script

**iPhone Call Screening:**
- When someone has iPhone call screening turned on, most AI agents pitch a robot and waste the call
- Our prompts detect the screening, respond with just a name, wait silently for up to 30 seconds, and only start the real conversation when a human picks up

**One Question at a Time:**
- The #1 reason AI calls fail is asking multiple questions at once
- Every prompt enforces: ask one question, shut up, wait for the answer, react, then ask the next one

---

## Troubleshooting

**"I don't see the /new-voice-ai-prompt command"**
- Make sure you copied the file to the right place (see Step 3)
- Make sure the file is named exactly `new-voice-ai-prompt.md`
- Try restarting Claude Code (type `exit`, then `claude` again)

**"npm is not recognized" or "command not found: npm"**
- You need to install Node.js first: https://nodejs.org (download the LTS version)
- After installing, close and reopen your terminal, then try again

**"I can't find the .claude folder"**
- It's a hidden folder. On Mac: press `Cmd + Shift + .` in Finder. On Windows: View → Show → Hidden Items in File Explorer

**"The output is too long / got cut off"**
- This can happen with very detailed offers. Try running the skill again - Claude Code handles long outputs well, but sometimes the display truncates. The full output is still there.

**"I want to edit the prompt after it's generated"**
- Absolutely - the generated prompt is a starting point. Copy it, paste it into a doc, and customize anything you want. The psychology and structure are the hard part - tweaking specific lines is easy.

---

## Need Help?

Drop your question in the Skool community. Include:
- What step you're stuck on
- What error message you're seeing (screenshot if possible)
- What operating system you're on (Mac or Windows)

We'll get you sorted.

---

**Built by MetaTech AI. Powered by 100,000+ calls per day on RizzDial.**
