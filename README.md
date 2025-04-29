# Computer Vision

This repository contains code for computer vision techniques on live video feed.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Techniques](#techniques)

## Installation

To avoid dependency conflicts, it is recommended to use a virtual environment. You can create and activate one using the following commands:

On Windows:
```
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```
To install the necessary dependencies, run:
```
pip install -r requirements.txt
```
A video apparatus (such as a webcam) will be needed to run the program. A phone can also be used by using the [DroidCam app](https://droidcam.app/)
## Usage
To run the code, you can use the following command:
```
python main.py <method_name>
```
Multiple methods can also be run in succession:
```
python main.py <method_name_1> <method_name_2>
```
### Running the object_detection script

#### Prerequisites
Before running the `object_detection.py` script, navigate to the object_detection folder

1. Navigate to the `object_detection` folder using the following command:
    ```bash
    cd object_detection
    ```
2. Install the dependencies from `object_detection_requirements.txt`
    ```bash
    pip install -r object_detection_requirements.txt
    ```

3. **Run the Script**:
    Execute the `object_detection` script using:
    ```bash
    python object_detection.py
    ```


## Techniques
This repository includes implementations of the following computer vision techniques:
- color masking
- contours
- sobel filter
- laplacian filter
- convolutional neural network
