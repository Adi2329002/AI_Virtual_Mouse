import cv2
import time
from src.core.hand_tracker import HandTracker
from src.core.mouse_controller import MouseController
from src.core.gesture_detector import GestureDetector


def main():
    hand_tracker = HandTracker()
    mouse_controller = MouseController()
    gesture_detector = GestureDetector()

    prev_time = 0

    while True:
        frame, results = hand_tracker.get_frame()

        if frame is None:
            break

        current_time = time.time()
        fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
        prev_time = current_time

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                hand_tracker.draw_landmarks(frame, hand_landmarks)

                index_tip = hand_landmarks.landmark[8]
                mouse_controller.move(index_tip.x, index_tip.y)

                # Left click
                if gesture_detector.detect_left_click(frame, hand_landmarks):
                    mouse_controller.left_click()

                # Right click
                if gesture_detector.detect_right_click(frame, hand_landmarks):
                    mouse_controller.right_click()

                # Drag logic
                if gesture_detector.detect_drag(frame, hand_landmarks):
                    mouse_controller.start_drag()
                else:
                    mouse_controller.stop_drag()

        cv2.putText(
            frame,
            f"FPS: {int(fps)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("AI Virtual Mouse - Professional", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    hand_tracker.release()


if __name__ == "__main__":
    main()
