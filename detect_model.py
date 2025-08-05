from ultralytics import YOLO
import cv2

# Load pretrained YOLOv8 model
model = YOLO('yolov8n.pt')  # Or use yolov8s.pt for better accuracy

def detect_objects(image_path):
    image = cv2.imread(image_path)
    results = model(image)[0]

    car_boxes = []
    person_boxes = []

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, cls_id = result
        label = int(cls_id)

        if label == 2:  # Car class in COCO
            car_boxes.append((int(x1), int(y1), int(x2), int(y2)))
        elif label == 0:  # Person class
            person_boxes.append((int(x1), int(y1), int(x2), int(y2)))

    return image, car_boxes, person_boxes
