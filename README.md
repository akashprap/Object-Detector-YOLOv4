# Object Detector using YOLOv4

This repository contains code for an Object Detector implemented using YOLOv4. The model is trained to detect objects from five classes: Person, Bird, Animal, Building, and Tree.

## Installation

To set up and run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/akashprap/Object-Detector-YOLOv4.git
   cd Object-Detector-YOLOv4
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Execute the `object_tracking.py` script to perform object detection and tracking using the trained YOLOv4 model. Ensure that the necessary weights and configuration files are available in the correct directories.

Example usage:
```bash
python object_tracking.py
```

## Directory Structure

- `cfg/`: Contains configuration files for the YOLOv4 model.
- `weights/`: Stores the trained weights for the custom YOLOv4 model.
- `object_tracking.py`: Main script for object tracking.
- `object_detection.py`: Main script for object detection.
- `requirements.txt`: Lists all the required libraries and their versions.

## Customization

To customize the model for different classes or fine-tuning, modify the configuration files (`cfg/*.cfg`) and consider retraining the model using your dataset or following the provided instructions.

## Contributors

- Akash Prajapati 
