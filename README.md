# Visual Fidelity Metric

A program made for comparing images and extracting videos using PSNR, SSIM, and LPIPS metrics.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Set up Virtual Environment](#set-up-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
  - [Extracting Videos](#extracting-videos)
  - [Comparing Images](#comparing-images)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Description

Visual Fidelity Metric is a tool designed for comparing images and extracting video frames using three popular metrics:
- PSNR (Peak Signal-to-Noise Ratio)
- SSIM (Structural Similarity Index)
- LPIPS (Learned Perceptual Image Patch Similarity)

This tool helps in assessing the quality and fidelity of images and videos by providing quantitative comparisons through a user-friendly GUI.

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

Make sure you have the following software installed:
- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [Git](https://git-scm.com/)

### Clone the Repository

First, clone the repository to your local machine:
```sh
git clone https://github.com/yudhistiraindyka/VisualFidelityMetric.git
cd VisualFidelityMetric
```
### Set up Virtual Environment

#### On Windows
```
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

## Usage

### Extracting Videos

To extract each frame from a video, use the following command:
```
python src/video_extract.py
```
This will open the GUI for frame extraction program.

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/e25b2b5e-846a-49fa-bf7f-c2de71ed3306" alt="Example Image" width="400" />
</p>

1. Click browse, then navigate to the video that want to be extracted, click ok
2. Click extract frames, then choose the output folder (preferably separate folders for native and upscaled)
3. The progress should appear and we can wait until it finishes

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/c8bfb5bf-aef5-4459-8197-f86283e74f8e" alt="Example Image" width="400" />
</p>




### Comparing images

To compare two images using the provided metrics, use the following command:
```
python src/main_app.py
```
This will open the GUI for image comparison.

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/a9efccd4-0ee5-446a-aca2-7e449f3fc180" alt="Example Image" width="800" />
</p>

1. Click on the "Select First Image (Native)" and choose the native image
2. Click on the "Select Second Image (Upscaled)" and choose the upscaled image

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/7f8f1cca-059c-4018-b7d4-0d94dada61c6" alt="Example Image" width="800" />
</p>

3. Click on the comparison method that you want (PSNR, SSIM, LPIPS)
4. The result should appear

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/8bd817e4-4a4f-4b48-b165-490b6b2cec05" alt="Example Image" width="800" />
</p>
