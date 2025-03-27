from ultralytics import YOLO

model = YOLO("yolo11n")
model.train(
    data="/Users/prof3ssor/Documents/mouse-keyboard-detection/data.yaml",
    epochs=100,
    device="mps",
)
