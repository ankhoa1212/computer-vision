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
A video apparatus (such as a webcam) will be needed to run the program.
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

Navigate to the `object_detection` folder using the following command:
```bash
cd object_detection
```
Install the dependencies from `object_detection_requirements.txt`

## Steps to Run the Script

1. **Clone the Repository (if applicable)**:
    If the script is part of a repository, clone it using:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install Dependencies**:
    Install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
    Ensure that the `requirements.txt` file is present in the same directory as the script.

3. **Run the Script**:
    Execute the `object_detection` script using:
    ```bash
    python object_detection.py
    ```

4. **Additional Configuration (if any)**:
    If the script requires specific configuration files or environment variables, ensure they are properly set up before running the script.

## Notes
- If you encounter any issues, verify that all dependencies are installed correctly and that your Python version is compatible.
- Refer to the script's README or comments for additional details or troubleshooting steps.
## Techniques
This repository includes implementations of the following computer vision techniques:
- color masking
- contours
- sobel filter
- laplacian filter
- convolutional neural network
