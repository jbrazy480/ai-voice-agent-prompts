# Why they won

18 months of SuperAdmin call history (Feb 2025 to Aug 2026). Success metric is `hangup_reason=call_transfer` and/or a booked `appointment_date`. Do not use `call_successful`. Live prompt text was not available from SuperAdmin. These files reconstruct the winning call patterns. Client names, clinic names, doctor names, and phone numbers were stripped. Generic verticals only.

Platform sample: 425,334 AI calls, 2,958 live transfers. V1 Retell-style agent ids (`agent_...`) are the production bookers. `error_retell` was 53 platform-wide, so that stack is live. `machine_detected` is 0 everywhere.

Company transfer totals (sampled high-volume accounts):

| Vertical (generic) | Transfers | Calls |
|---|---|---|
| Medical practice | 593 | 7,664 |
| Dental (now inactive analog) | 485 | 11,732 |
| Medspa | 297 | 12,817 |
| Internal platform account | 99 | 25,878 |
| Credit / CS inbound | 77 | (account sample) |
| Senior living outbound | 41 | 13,196 |

High-volume outbound shops at about 15,000 calls transferred 3 times. Volume is not conversion.

`appointment_date` exists on some booked calls. SuperAdmin calendars are empty because calendars are GHL-owned. This note reports transfers. It does not invent appointment counts.

---

## What the winners actually do

- **Inbound converts 4 to 10x outbound on rate** because the human already raised their hand. Outbound wins raw bookings because it dials 10x more. Both belong in the library.
- **Transfer-when-hot is a conversion.** Do not make the bot grind to a calendar if a human closer is on the floor. The bot's job is: qualify in under 2 minutes, then `{{transfer_call}}`.
- **The live script is short.** Greet by company, confirm name, one-line reason (the campaign they came from), ask what they want, offer two concrete slots or transfer. One question at a time. No talking into a machine. Machine handling is a separate template.
- **Confirm name first on outbound.** "Hey, is this {{first_name}}?" then the reason. Skipping name-confirm kills trust.
- **Two slots, not "when works for you."** Morning and afternoon, or two named times. Assumptive Bridge.
- **Local CID and campaign-specific agents beat one generic agent.** Winners were per-offer (Botox, fillers, hair, GLP1) and per-location (two offices), not one mega prompt.
- **`call_successful` is a lie.** Voicemail 10 to 23 second talks are marked successful. Rank by transfer plus `appointment_date` only.
- **High outbound volume with no transfer** (solar leak, 15k-call shops) is a connection problem, not a prompt problem.

---

## V1 vs V2

V1 (Retell-style `agent_` ids) is what booked. V2 UUID twins were created (often labeled like "New ...") and had **zero** production calls on these winners. Do not rewrite winners onto V2 until V2 has a transfer count. A twin that has never taken traffic is not a proven prompt.

---

## How to use this

Copy the matching 12-section file. Swap `{{company}}`, `{{agent}}`, `{{offer}}`, hours, and the calendar functions if your stack is not GHL. Keep the short path. If you add a third discovery question, you are no longer on the winning pattern.
