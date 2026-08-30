# Winner library (18-month production)

Production-proven 12-section RizzDial prompts reconstructed from SuperAdmin call history (Feb 2025 to Aug 2026). Success metric is live transfer (`hangup_reason=call_transfer`) and/or a booked `appointment_date`. Do not rank by `call_successful`.

Client names, clinic names, doctor names, cities-as-brands, and phone numbers were stripped. Generic verticals only: medspa, medical practice, dental.

These files do not replace [templates/](../../templates/) (keep 01 to 11 as they are). They also do not replace the generated vertical starters in [prompts/](../). Use this folder when you want the short, transfer-when-hot pattern that actually transferred.

MIT. Same license as the rest of this repo. See [LICENSE](../../LICENSE).

Full writeup: [WHY-THEY-WON.md](WHY-THEY-WON.md).

---

## When to use each

| File | Use when | Pattern |
|---|---|---|
| [01-inbound-medspa-transfer.md](01-inbound-medspa-transfer.md) | Inbound medspa. Human already called. Transfer to scheduling when hot. Two-slot if they want a time. | Winner #4 |
| [02-outbound-medspa-two-slot.md](02-outbound-medspa-two-slot.md) | Outbound medspa specials. Confirm name. One-line offer. Two named slots. Transfer if they want a person. | Winners #7 and #8 |
| [03-inbound-medical-social.md](03-inbound-medical-social.md) | Inbound medical / telemed from social. Best rate. HIPAA-aware. Transfer to front desk when hot. | Winners #5 and #9 |
| [04-outbound-medical-reactivation.md](04-outbound-medical-reactivation.md) | Outbound medical check-in or social follow-up. Confirm name. Do not interrogate. Two slots or transfer. | Winners #2 and #3 |
| [05-inbound-dental.md](05-inbound-dental.md) | Inbound dental front desk. Emergency vs consult fork. Transfer emergencies immediately. Two-slot the rest. | Winner #6 |
| [06-outbound-dental-reactivation.md](06-outbound-dental-reactivation.md) | Outbound dental recall / database reactivation. Highest raw transfers. Confirm name. Two slots. Never talk into a machine. | Winner #1 |

Every file uses all 12 RizzDial sections in order. Notation: `~"..."` spoken, right arrow for actions, `{{...}}` CRM. Booking uses `{{ghl_calendar_availability_}}` then `{{book_appointment_GHL_}}` (optional integration, swap-able).

---

## Agent leaderboard (generic labels)

Ranked by live transfers, not by `call_successful`.

| Rank | Generic label | Transfers | Calls | Rate | Direction | Notes |
|---|---|---|---|---|---|---|
| 1 | Dental outbound setter | 372 | 9,334 | ~4% | Outbound | Highest raw transfers. Avg ~36s (lots of no-answer). |
| 2 | Medical outbound location A | 221 | 3,522 | ~6% | Outbound | Per-location agent. |
| 3 | Medical outbound location B | 211 | 3,401 | ~6% | Outbound | Twin office, not one mega prompt. |
| 4 | Medspa inbound | 147 | 600 | 25% | Inbound | Avg 69s. Transfer-when-hot. Also books some GHL consults on the line. |
| 5 | Medical inbound location A | 100 | 270 | 37% | Inbound | Best rate. Social inbound. Avg ~100s. |
| 6 | Dental inbound | 99 | 2,321 | 4% | Inbound | Avg 78s. 1,788 user hangups (front desk volume). |
| 7 | Medspa outbound Botox specials | 69 | (not a full-board sample) | n/a | Outbound | Two-slot offers. Transfer when they want a human. |
| 8 | Medspa outbound | 58 | (not a full-board sample) | n/a | Outbound | Confirm name, one-line reason, transfer when hot. |
| 9 | Medical inbound location B | 57 | 275 | 21% | Inbound | Avg ~99s. |

Do not invent appointment counts. SuperAdmin calendars are empty (GHL-owned). Say transfers unless you are documenting the GHL booking functions.

---

## House rules for this folder

- All 12 sections, this order: Project Instructions, Greetings, Call Flow, Character, Transfer Call, Critical Instructions, Custom Field References, What Your Company Does, Script, Objection Handling, Booking and Calendar, FAQ.
- Named psychology baked in: Time Contract, Permission Close, SPIN, Loss Aversion, Chris Voss labeling, the Takeaway, Assumptive Bridge, Silence Bomb, emotional matching, one question at a time.
- No em dashes or en dashes.
- No real customer names, phone numbers, clinic names, doctor names, or production company names.
- No machine-detection / voicemail talk tracks here. That is a separate template.
- V1 (`agent_` ids) is what booked. Do not rewrite these onto V2 UUID twins until V2 has a transfer count.
