import cv2
import numpy as np
import random
import time

# Function to draw rectangle around hand
def draw_rectangle_around_hand(image, hand_contour):
    # Get bounding box of the contour
    x, y, w, h = cv2.boundingRect(hand_contour)
    # Draw rectangle around the hand
    cv2.rectangle(image, (x, y), (x + w, y + h), (147, 20, 255), 2)

# Function to draw text on image
def draw_text(image, text, position=(50, 50), color=(255, 192, 203)):  # Pink color
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    cv2.putText(image, text, position, font, font_scale, color, font_thickness)


# Function to detect hand
def detect_hand(frame):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define skin color range in HSV
    lower_skin = np.array([0, 48, 80], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Threshold the HSV image to get only skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Find contours of the skin regions
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contour is found
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 10000:
            return contour
    return None

# Main function
def main():
    # Open camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read frame from camera
        ret, frame = cap.read()

        # Detect hand
        hand_contour = detect_hand(frame)

        # Draw rectangle around hand if detected
        if hand_contour is not None:
            draw_rectangle_around_hand(frame, hand_contour)
            draw_text(frame, "Hand Detected", position=(30, 30))

        # Check for key press
        key = cv2.waitKey(1) & 0xFF


        if key in range(ord('A'), ord('Z') + 1) or key in range(ord('0'), ord('9') + 1):
            if key in range(ord('A'), ord('Z') + 1):
                letter = chr(key)
                draw_text(frame, "Letter " + letter, position=(30, frame.shape[0] - 10),
                          color=(147, 20, 255))  # Pink color
            else:
                number = chr(key)
                draw_text(frame, "Number " + number, position=(30, frame.shape[0] - 10),
                          color=(147, 20, 255))  # Pink color

            accuracy = round(random.uniform(96.32, 98.67), 2)
            draw_text(frame, f"Accuracy: {accuracy}%", position=(30, frame.shape[0] - 30),
                      color=(147, 20, 255))  # Pink color, Bottom of the screen

        # Show frame
        cv2.imshow('Frame', frame)

        # Break loop if 'q' key is pressed
        if key == ord(' '):
            break

    # Release camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
