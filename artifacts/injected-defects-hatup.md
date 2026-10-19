# Injected Defects Specification: HatUp Application

*Note: These 5 defects were intentionally injected into the "HatUp" MVP to simulate a realistic QA handover scenario and practice black-box detection.*

## DEF-01: Negative Donation Amount Allowed
- **Type**: Logic / Validation Error
- **Component**: `DonationFragment`
- **Description**: The system allows users to input and submit negative donation amounts (e.g., -500). The "Support" button remains active, and the transaction processes successfully, violating basic financial logic.
- **Reproduction**: Navigate to donation screen → Enter "-500" in the amount field → Tap "Support".

## DEF-02: Favorite Artists List Does Not Sync to Profile
- **Type**: Logic / UI State Error
- **Component**: `ProfileFragment`, `ArtistDetailFragment`
- **Description**: When a user adds an artist to their favorites from the artist's card, the local state updates, but the "Favorites" section in the User Profile remains empty and does not reflect the change.
- **Reproduction**: Add an artist to favorites → Navigate to Profile tab → Observe that the favorites list is empty.

## DEF-03: Hardcoded Identical Event Descriptions
- **Type**: Architecture / UI Error
- **Component**: `EventDetailFragment`, `Event.java`
- **Description**: The text description of an event is hardcoded in the XML layout and is not bound to the `Event` data model. As a result, all artist cards display the exact same event description, regardless of the actual artist or event metadata.
- **Reproduction**: Open event cards for two different artists → Compare the text descriptions (they will be identical).

## DEF-04: Incorrect Donation Goal Progress Calculation
- **Type**: Arithmetic Error
- **Component**: `DonationFragment` (`addGoalCard` method)
- **Description**: When a donation is made, the "Collected" progress bar decreases by the donated amount instead of increasing. (e.g., If the goal is 3000₽ and the user donates 500₽, the displayed collected amount becomes 2500₽).
- **Reproduction**: Note the current "Collected" amount → Make a donation → Observe that the amount decreases.

## DEF-05: Comment Character Limit Mismatch
- **Type**: UI / UX Error
- **Component**: `DonationFragment`, `fragment_artist_donation.xml`
- **Description**: The UI hint states that the comment field allows up to 500 characters (for donations ≥ 500₽). However, the XML attribute `android:maxLength="50"` hard-limits the input to 50 characters, cutting off the text abruptly and misleading the user.
- **Reproduction**: Enter a donation amount ≥ 500₽ → Type more than 50 characters in the comment field → Observe that input is blocked at 50 characters.
