# Test Cases: Yap Messenger Application

## TC-01: Voice Recording Cancellation on Minimal Swipe
- **Preconditions**: User is authorized; Main screen is open; Microphone permission is granted.
- **Steps**:
  1. Long-press the central "Yap" button to start voice recording.
  2. Without releasing the finger, move it down by approximately 20 pixels.
  3. Observe the interface reaction.
- **Expected Result**: Recording continues, as a 20px shift is within the hold zone and not an explicit cancellation gesture.
- **Actual Result**: Recording is immediately canceled.

## TC-02: Push Notifications After Logout
- **Preconditions**: User A is logged in on Device 1. Device 2 is ready with User B.
- **Steps**:
  1. On Device 1, open Profile and tap "Logout".
  2. From Device 2, send a message to User A.
  3. Check Device 1 for system notifications.
- **Expected Result**: No notifications appear on Device 1, as the FCM token should be unlinked from the profile in Firestore.
- **Actual Result**: The message notification appears on Device 1.

## TC-03: Empty Audio File on Instant "Yap" Release
- **Preconditions**: Main screen is open; recipient is selected.
- **Steps**:
  1. Start recording by holding the button.
  2. Instantly release the button or swipe up and immediately tap "Send" before the preview mode activates.
  3. Check the received message on the recipient's side.
- **Expected Result**: A valid audio file is saved, uploaded to Supabase Storage, and playable by the recipient.
- **Actual Result**: The recipient sees a voice message card, but the audio is unplayable and has a file size of 0 bytes.

## TC-04: Quick Access Contacts Desync on Deletion
- **Preconditions**: User X is added to the quick access panel on the main screen.
- **Steps**:
  1. Navigate to the "Friends" section.
  2. Delete User X from the friends list.
  3. Return to the main screen and check the quick access panel.
- **Expected Result**: User X is removed from the quick access panel.
- **Actual Result**: User X remains visible, causing errors when attempting to send a message.

## TC-05: Emoji Reaction Appending Instead of Replacing
- **Preconditions**: Recipient is selected; Yap input panel is open.
- **Steps**:
  1. Type an arbitrary text phrase in the input field.
  2. Tap any quick emoji reaction icon.
  3. Check the content of the input field/message.
- **Expected Result**: The text message is cleared, and the mode switches to sending a pure reaction.
- **Actual Result**: The emoji symbol is simply appended to the end of the existing text.

## TC-06: Empty Friends List in Offline Mode
- **Preconditions**: Friends list was previously loaded successfully while online.
- **Steps**:
  1. Enable "Airplane Mode" on the device.
  2. Open the "Friends" tab.
  3. Observe the list state.
- **Expected Result**: The previously cached friends list is displayed with an offline mode indicator.
- **Actual Result**: The screen displays a completely empty list (EmptyState component); local cache is not utilized.

## TC-07: Mute Status Desync for Same Sender
- **Preconditions**: Multiple messages from User V are present in the notifications list.
- **Steps**:
  1. Tap "Mute notifications" on one of User V's message cards.
  2. Check the mute icon status on the other message cards from User V.
- **Expected Result**: All message cards from User V update to reflect the muted status.
- **Actual Result**: Only the tapped card updates; other cards from the same sender retain the unmuted icon.

## TC-08: Incoming Friend Requests Disappear After Search Clear
- **Preconditions**: One active incoming friend request is present.
- **Steps**:
  1. Open the "Add Friends" screen (request is visible).
  2. Type an arbitrary code into the search field.
  3. Completely delete all characters from the search field.
- **Expected Result**: The incoming request card reappears on the screen.
- **Actual Result**: The request list becomes empty and does not restore until the screen is fully restarted.
