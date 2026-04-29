# Tsashi Test Automation Framework

Automation framework for **Tsashi** — a platform for shared activities and events.

Built to validate real product behavior across UI, API, and data layers, with focus on reliability, structure, and fast feedback.

---

## Purpose

This framework tests how the system behaves in real use — not just UI interactions.

- validate critical user flows end-to-end  
- ensure consistency across UI, API, and data  
- catch issues before release  
- keep tests stable and meaningful  

---

## Approach

Testing is split across layers:

- **UI** → critical end-to-end flows  
- **API** → business logic and state validation  
- **Database** → selective checks when needed  

UI stays lean. Logic is validated where it belongs.

---

## Tech Stack

- Python  
- Pytest  
- Playwright  
- Page Object Model  
- GitHub Actions (CI)  
- Supabase (PostgreSQL)  
- Vercel  

---

## Current Coverage

### UI
- existing user login  
- events / plans page  
- join flow  
- joined state validation  
- My Events consistency  
- leave queue flow  

### Planned
- API layer (auth, events, join/leave)  
- negative scenarios (duplicate join, unavailable events)  
- improved test data handling  

---

## Project Structure

```text
tsashi-test-automation/
├── api/
├── components/
├── config/
├── data/
├── fixtures/
├── pages/
├── tests/
│   ├── ui/
│   └── api/
├── utils/
├── conftest.py
├── TEST_STRATEGY.md
└── requirements.txt
```
## Principles
- no hard sleeps
- stable selectors over fragile locators
- tests validate behavior, not implementation
- UI tests stay focused and high-value
- API tests cover logic faster
- clear structure over quick fixes
  
## Setup
install dependencies
```pip install -r requirements.txt```
install playwright
```playwright install```
create ```.env``` file 
```
BASE_URL=https://www.tsashi.com
TEST_USER_EMAIL=your_email
TEST_USER_PASSWORD=your_password
HEADLESS=false
```
## CI 
Designed to run in GitHub Actions for fast feedback on changes.

## Status
In progress.

### Current focus:
stabilizing core flows
expanding API coverage
improving reliability
