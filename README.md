# Mouse and Keyboard Detection

This repository contains tools and resources for detecting and training models related to mouse and keyboard activities using YOLO (You Only Look Once) object detection framework.

## Project Structure

- **data/**: Directory containing datasets for training and validation.
- **data/train/**: Training dataset.
- **data/val/**: Validation dataset.
- **output/**: Directory for storing model outputs and logs.
- **classes.txt**: List of class labels for detection.
- **data.yaml**: Configuration file for YOLO training.
- **notes.json**: Notes and metadata related to the project.
- **yolo11n.pt**: Pre-trained YOLO model weights.
- **yolo_detect.py**: Script for running detection using the YOLO model.
- **yolo_train.py**: Script for training the YOLO model.

## Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Change the directory of path inside data.yaml:
   Replace with your absolute path of the data folder.

3. Train the model:

   ```bash
   python yolo_train.py
   ```

4. Copy or Move the best.pt file from output/train*/weights/best.pt to the same folder as yolo_detect.py

5. Run detection:

   ```bash
   python yolo_detect.py
   ```
