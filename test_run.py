from detect_model import detect_objects
from color_check import is_blue_car
import cv2

image_path = "test.jpg"  # Replace with your image path

image, car_boxes, person_boxes = detect_objects(image_path)

for box in car_boxes:
    if is_blue_car(image, box):
        color = (0, 0, 255)  # Red rectangle for blue car
    else:
        color = (255, 0, 0)  # Blue rectangle for non-blue car
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), color, 2)

for box in person_boxes:
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)  # Green for people

cv2.putText(image, f"Cars: {len(car_boxes)}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
cv2.putText(image, f"People: {len(person_boxes)}", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv2.imshow("Final Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
