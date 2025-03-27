from ultralytics import YOLO

model = YOLO(
    "/Users/prof3ssor/Documents/mouse-keyboard-detection/runs/detect/train2/weights/best.pt"
)
results = model(0, show=True, stream=True)
for result in results:
    boxes = result.boxes
