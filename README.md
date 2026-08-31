# Medical Imaging PyTorch
## Advanced Medical Imaging Analysis Framework
### Accurate Segmentation, Loss Functions, and Pre-processing for Medical Imaging Tasks

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)

# Overview
Medical Imaging PyTorch is an open-source framework for medical image analysis, providing a comprehensive set of tools for segmentation, loss functions, and pre-processing.

## Features
### Accurate Segmentation
* Utilize advanced UNet and UNet3D architectures for accurate segmentation of medical images.
* Employ pre-trained models for efficient and robust segmentation.

### Customizable Loss Functions
* Implement Dice Loss, Masked Dice Loss, and Confident Mean Squared Error for accurate loss calculation.
* Fine-tune loss functions for specific medical imaging tasks.

### Advanced Pre-processing
* Apply filters, transforms, and augmentations to medical images.
* Utilize pre-processing techniques for data augmentation and normalization.

### Real-world Examples
### Segmentation of MRI Images
```python
from medicaltorch.models import UNet
from medicaltorch.datasets import MRI2DSegmentationDataset

# Load pre-trained UNet model
model = UNet()

# Load MRI dataset
dataset = MRI2DSegmentationDataset('path/to/mri/images')

# Perform segmentation
segmentation = model.predict(dataset)
```

### Usage in Medical Imaging Tasks
```python
from medicaltorch.datasets import SCGMChallenge2DTrain
from medicaltorch.models import UNet3D

# Load pre-trained UNet3D model
model = UNet3D()

# Load SCGM Challenge 2D Train dataset
dataset = SCGMChallenge2DTrain('path/to/train/images')

# Perform segmentation
segmentation = model.predict(dataset)
```

## Installation

```bash
git clone https://github.com/AvicenaIG/medical-imaging-pytorch.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Contributing
Contributions are welcome! Please submit pull requests or issues to improve the framework.

## License
Medical Imaging PyTorch is released under the MIT License.

* Copyright (c) 2026, medical-imaging-pytorch contributors
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.