import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Read video (or use webcam: cv2.VideoCapture(0))
cap = cv2.VideoCapture('shoplifting_clip.mp4')

while cap.isOpened():
    # Read the frame
    ret, frame = cap.read()
    if not ret:
        break  # Exit the loop if the video ends

    # Convert frame to RGB (Mediapipe requirement)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    # Analyze gestures if pose landmarks are detected
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        # Extract coordinates (x, y) of key points (e.g., left hand, right hand, torso)
        left_hand = np.array([landmarks[mp_pose.PoseLandmark.LEFT_WRIST].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST].y])
        right_hand = np.array([landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].y])
        torso = np.array([landmarks[mp_pose.PoseLandmark.LEFT_HIP].x,
                          landmarks[mp_pose.PoseLandmark.LEFT_HIP].y])

        # Calculate distances (e.g., hand to torso)
        left_hand_to_torso = np.linalg.norm(left_hand - torso)
        right_hand_to_torso = np.linalg.norm(right_hand - torso)

        # Determine if the gesture is suspicious based on distance
        min_distance = min(left_hand_to_torso, right_hand_to_torso)
        threshold = 0.25  # Adjust this threshold as needed

        # Simulate a confidence score based on distance
        # If distance is small, high confidence of suspicious behavior
        suspicious_confidence = max(0, (threshold - min_distance) / threshold * 100)
        normal_confidence = 100 - suspicious_confidence

        # Display action labels and confidence scores
        if min_distance < threshold:
            cv2.putText(frame, "Suspicious Gesture Detected!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(frame, f"Suspicious: {suspicious_confidence:.2f}%", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            cv2.putText(frame, f"Normal: {normal_confidence:.2f}%", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Draw pose landmarks on the frame
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Display the frame
    cv2.imshow('Pose Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()