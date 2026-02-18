import cv2
from src.core.hand_tracker import HandTracker
from src.core.mouse_controller import MouseController
from src.core.gesture_detector import GestureDetector


def main():
    hand_tracker = HandTracker()
    mouse_controller = MouseController()
    gesture_detector = GestureDetector()

    while True:
        frame, results = hand_tracker.get_frame()

        if frame is None:
            break

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                hand_tracker.draw_landmarks(frame, hand_landmarks)

                # Move mouse using index finger
                index_tip = hand_landmarks.landmark[8]
                mouse_controller.move(index_tip.x, index_tip.y)

                # Detect click gesture
                if gesture_detector.detect_click(frame, hand_landmarks):
                    mouse_controller.click()

        cv2.imshow("AI Virtual Mouse - Professional", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    hand_tracker.release()


if __name__ == "__main__":
    main()
