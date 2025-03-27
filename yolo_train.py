from ultralytics import YOLO

model = YOLO("yolo11n")
model.train(data="data.yaml", epochs=100, device="mps", project="output", name="train1")
