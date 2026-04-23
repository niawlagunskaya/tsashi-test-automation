# Tsashi Test Automation Strategy

## Goal
Build a maintainable QA automation framework that validates Tsashi through the right testing layers:
- UI tests for critical end-to-end user journeys
- API tests for business logic and state changes
- selective database checks when needed

The framework should demonstrate:
- clear test design
- correct use of automation layers
- realistic product-level validation

---

## Product Areas in Scope

### 1. Authentication
- user login (existing user)
- new user redirect to onboarding/profile

### 2. Events / Plans
- events page loads
- cards are visible
- joined state is reflected

### 3. Queue (Core Feature)
- join plan/event
- leave queue
- joined state update
- My events consistency

### 4. My Events
- joined items appear
- leaving removes item
- state stays consistent

---

## Test Layer Strategy

### UI Tests (High-value only)
UI tests validate critical user journeys and visible state transitions.

#### UI covers:
- existing user can log in
- events/plans page loads
- user can join a plan/event
- joined state updates in UI (Join → Leave queue)
- joined item appears in My Events
- user can leave queue and state resets

#### UI does NOT cover:
- deep negative scenarios
- backend-only logic
- repetitive validation better suited for API

---

### API Tests (Primary logic validation)
API tests validate backend behavior efficiently.

#### API covers:
- login/auth response success
- events/plans list retrieval
- join request success
- leave request success
- duplicate join handling
- unavailable/closed event behavior
- My events response correctness

---

### Database Validation (Selective)
Used only when necessary.

#### DB used for:
- confirming join/leave state after actions
- debugging inconsistencies

#### DB not used for:
- main assertions of user flows

---

## Initial Regression Scope (Version 1)

### UI Regression Pack
1. existing user can log in
2. events/plans page loads successfully
3. user can join a plan/event and see updated state
4. joined item appears in My Events
5. user can leave queue and state resets

---

### API Regression Pack
1. login API returns success
2. events/plans list returns valid data
3. join API request succeeds
4. leave API request succeeds
5. duplicate join is handled correctly

---

## Execution Plan

### Phase 1 — UI Foundation
- stable login flow
- stable events page navigation
- join action with correct UI state validation

### Phase 2 — API Layer
- implement API client
- add join/leave API tests
- validate backend state independently from UI

### Phase 3 — Expanded Coverage
- onboarding / profile flow
- negative scenarios
- CI improvements
- selective DB validation

---

## Future Coverage (Backlog)

### Account Management
- new user sign up
- profile completion
- profile update
- profile deletion

### Additional Scenarios
- duplicate join attempts
- unavailable/closed events
- invalid onboarding inputs
- permission/access checks

---

## Design Principles
- avoid hard sleeps
- rely on Playwright auto-waiting and assertions
- keep UI tests minimal and business-focused
- prefer API for logic validation
- keep page objects small and reusable
- use environment-driven test data
- prioritize reliability over quantity

---

## Naming Convention

### UI tests
- test_existing_user_can_log_in
- test_user_can_join_plan_and_see_updated_state
- test_joined_item_appears_in_my_events
- test_user_can_leave_queue

### API tests
- test_login_api_returns_success
- test_events_list_api_returns_items
- test_join_api_creates_state
- test_leave_api_removes_state

---

## Success Criteria (Version 1)
The framework aims to ensure:
- reliable validation of user flows
- proper separation of testing layers
- maintainable and scalable test structure