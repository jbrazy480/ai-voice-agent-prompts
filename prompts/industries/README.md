# Converting industry pack

Hand-built 12 section prompts for the industries this library actually serves. Opt-in plus solar cold. Generic verticals only. MIT.

This folder does **not** replace:

- Generated verticals in `prompts/*.md` (engine output)
- Winner templates in `prompts/winners/` (medical, medspa, dental)

Copy a file, swap the placeholders, keep the short path. If you add a fifth qualification question on a voice call, you left the converting pattern.

Why these convert: [WHY-THESE-CONVERT.md](WHY-THESE-CONVERT.md).

The CLI (`generate.py`) still emits the generated verticals. It does not rewrite this pack.

## Voice (every file)

- After they pick up (outbound) or after the inbound greeting: ~"How are you doing today?"
- Then immediately the reason. No extra small talk.
- Honest AI disclosure, one sentence: AI assistant for `{{company_name}}`. Book or transfer if someone is available.
- Two named slots. Never "when works for you."
- Transfer if a human is available and they are hot. Book if the calendar is open.
- If the calendar is empty, transfer if a human is available, else two named slots.
- AMD or voicemail: hang up. Do not leave a message.
- TCPA: if they say do not call, confirm and end.

## Files

### Solar (flagship)

| File | Use |
|---|---|
| [solar-outbound-cold.md](solar-outbound-cold.md) | Cold call and aged list. 2026 post-ITC. Four quals. Hang-tight transfer. |
| [solar-outbound-optin.md](solar-outbound-optin.md) | Form, ad, or quote request. Three quals. Optional bill link after the book. |
| [solar-inbound.md](solar-inbound.md) | They called you or a mailer. |

### Home and local

| File | Use |
|---|---|
| [hvac-inbound.md](hvac-inbound.md) | Repair or diagnostic. No phone diagnosis. `{{diagnostic_fee}}`. |
| [hvac-outbound-optin.md](hvac-outbound-optin.md) | Membership or quote follow-up. |
| [roofing-inbound.md](roofing-inbound.md) | Leak or storm. Address confirm. No claim coaching. |
| [roofing-outbound-optin.md](roofing-outbound-optin.md) | Inspection in `{{city}}`. |
| [automotive-inbound.md](automotive-inbound.md) | Service or sales. |
| [automotive-outbound-optin.md](automotive-outbound-optin.md) | Service-due or internet lead. |

### Regulated

| File | Use |
|---|---|
| [insurance-inbound.md](insurance-inbound.md) | Must disclose AI. Do not quote or bind. |
| [insurance-outbound-optin.md](insurance-outbound-optin.md) | Quote follow-up. Carrier and renewal. |
| [mortgage-inbound.md](mortgage-inbound.md) | Disclose `{{nmls_id}}`. No promised rate. |
| [mortgage-outbound-optin.md](mortgage-outbound-optin.md) | Opt-in plus `{{rate_or_reason}}`. RESPA and TCPA. |
| [credit-repair-inbound.md](credit-repair-inbound.md) | Never promise a score. FCRA. |
| [credit-repair-outbound-optin.md](credit-repair-outbound-optin.md) | Opt-in. Transfer to specialist. |
| [legal-pi-inbound.md](legal-pi-inbound.md) | Incident basics. No legal advice. Transfer to intake. |

### Sales and property

| File | Use |
|---|---|
| [real-estate-inbound.md](real-estate-inbound.md) | They called the office. Fair Housing. |
| [real-estate-outbound-optin.md](real-estate-outbound-optin.md) | ISA from listing or ad. 3 questions, not full LPMAMA. |
| [b2b-saas-outbound-optin.md](b2b-saas-outbound-optin.md) | 30-second permission. 15 minute demo. `{{outcome}}`. |
| [marketing-agency-inbound.md](marketing-agency-inbound.md) | Inquiry. Book a strategy call. |
| [marketing-agency-outbound-optin.md](marketing-agency-outbound-optin.md) | Form fill about `{{offer}}`. |

### Care, education, hospitality

| File | Use |
|---|---|
| [senior-living-inbound.md](senior-living-inbound.md) | Family call. Trigger event. Tour. No medical advice. |
| [fitness-inbound.md](fitness-inbound.md) | Tour or class. Not medical medspa. |
| [education-inbound.md](education-inbound.md) | Program and start date. Transfer to admissions. |
| [restaurant-inbound.md](restaurant-inbound.md) | Reservations and events only. Keep short. |
| [beauty-salon-inbound.md](beauty-salon-inbound.md) | Hair, nails, spa booking. Not medical medspa. |

## Placeholders

`{{company_name}}`, `{{agent_name}}`, `{{first_name}}`, `{{offer}}`, `{{lead_source}}`, `{{state}}`, `{{utility}}`, `{{city}}`, `{{bill_threshold}}`, `{{transfer_number}}`, `{{diagnostic_fee}}`, `{{nmls_id}}`, `{{rate_or_reason}}`, `{{outcome}}`.

Transfer action: `{{transfer_call}}`.
Booking: `{{ghl_calendar_availability_}}`, `{{book_appointment_GHL_}}`.
