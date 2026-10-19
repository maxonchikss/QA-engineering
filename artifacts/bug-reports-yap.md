# Bug Reports: Yap Messenger Application

## BUG-01: Voice Recording Cancels on Minimal Vertical Swipe
- **Severity**: Critical
- **Component**: MainYapButton.kt (Yap Screen)
- **Type**: UI / Logic
- **Description**: The voice recording process is aborted when the user's finger moves down by just ~20 pixels, even though this is well within the designated hold zone.
- **Steps to Reproduce**: Long-press the Yap button → Move finger down ~20px without releasing → Observe interface.
- **Expected**: Recording continues.
- **Actual**: Recording is immediately canceled.

## BUG-02: Push Notifications Received After Account Logout
- **Severity**: Critical
- **Component**: MyProfileViewModel.kt (Profile)
- **Type**: Integration / Logic
- **Description**: After logging out, the device continues to receive Firebase Cloud Messaging (FCM) push notifications intended for the logged-in user, violating data privacy.
- **Steps to Reproduce**: Log in on Device 1 → Logout → Send message from Device 2 → Check Device 1 notifications.
- **Expected**: No notifications on Device 1 (FCM token should be unlinked).
- **Actual**: Notification appears on Device 1.

## BUG-03: Empty Audio File Sent on Instant "Yap" Release
- **Severity**: Critical
- **Component**: MainYapButton.kt / HomeViewModel.kt
- **Type**: Logic / Concurrency
- **Description**: Rapidly releasing the record button or swiping up to send immediately finalizes the file stream prematurely, resulting in a 0-byte corrupted audio file.
- **Steps to Reproduce**: Hold record button → Instantly release and tap "Send" → Check recipient's view.
- **Expected**: Valid, playable audio file.
- **Actual**: Unplayable voice message card with 0 bytes.

## BUG-04: Quick Access Contacts Desync on Deletion
- **Severity**: Medium
- **Component**: HomeViewModel.kt (Main Screen)
- **Type**: Logic / State Management
- **Description**: The quick access panel on the main screen does not listen to state changes in the main friends list, causing deleted users to remain visible.
- **Steps to Reproduce**: Add User X to quick access → Delete User X from Friends → Return to Main Screen.
- **Expected**: User X disappears from quick access.
- **Actual**: User X remains visible, causing errors on tap.

## BUG-05: Emoji Reaction Appends to Text Instead of Replacing
- **Severity**: Medium
- **Component**: HomeViewModel.kt (Main Screen)
- **Type**: UI / Logic
- **Description**: Tapping a quick emoji reaction does not clear the text input buffer, resulting in a mixed text-and-emoji message instead of a pure reaction.
- **Steps to Reproduce**: Type text → Tap emoji reaction icon → Check input field.
- **Expected**: Text is cleared; pure reaction is prepared for sending.
- **Actual**: Emoji is appended to the end of the existing text.

## BUG-06: Empty Friends List Displayed in Offline Mode
- **Severity**: Medium
- **Component**: FriendsViewModel.kt / UserRepository.kt
- **Type**: Logic / Cache Handling
- **Description**: The application fails to fall back to locally cached friend data when the network is unavailable, showing an empty state instead.
- **Steps to Reproduce**: Load friends online → Enable Airplane Mode → Open Friends tab.
- **Expected**: Cached friends list displayed with offline indicator.
- **Actual**: Empty state shown.

## BUG-07: Mute Status Desync for Multiple Messages from Same Sender
- **Severity**: Medium
- **Component**: NotificationsViewModel.kt
- **Type**: UI / Logic
- **Description**: Muting notifications for a specific user only updates the UI state of the single card that was tapped, leaving other cards from the same sender with the outdated "unmuted" icon.
- **Steps to Reproduce**: Tap "Mute" on one message card from User V → Check other cards from User V.
- **Expected**: All cards from User V update to the muted state.
- **Actual**: Only the tapped card updates.

## BUG-08: Incoming Friend Requests Disappear After Clearing Search
- **Severity**: Medium
- **Component**: AddUserViewModel.kt
- **Type**: UI / Logic
- **Description**: Interacting with the search bar (typing and then clearing the text) resets the incoming requests list state, making active requests disappear until the screen is fully reloaded.
- **Steps to Reproduce**: Open Add Friends screen → Type in search → Clear search field.
- **Expected**: Incoming request card reappears.
- **Actual**: List remains empty.
