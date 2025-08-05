import cv2
import numpy as np

def is_blue_car(image, box):
    x1, y1, x2, y2 = box
    car_crop = image[y1:y2, x1:x2]

    if car_crop.size == 0:
        return False

    # Convert to HSV for better color detection
    hsv = cv2.cvtColor(car_crop, cv2.COLOR_BGR2HSV)

    # Define blue color range
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # Create mask for blue areas
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Check how much of the crop is blue
    blue_ratio = cv2.countNonZero(mask) / (car_crop.size / 3)

    return blue_ratio > 0.2  # You can tweak this threshold
