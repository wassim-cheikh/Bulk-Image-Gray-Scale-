# Image Gray Scale Converter

This Python script converts images to grayscale using the Pillow library. It supports both single image conversion and bulk conversion of images within a specified folder.

## Features

- Converts one or many images to grayscale.
- Supports customization of pixel conversion ratios.
- Saves converted images to an output folder.

## Requirements

- Python 3.11.4
- Pillow library (`pip install Pillow`)

## Usage

### Configuration

Edit the `constants.py` file to configure the script parameters:

- **USE_FOLDER**: Set to `True` for bulk image grayscale conversion from a folder, or `False` to convert a single image (you will be prompted to enter the image path).
- **FOLDER_PATH**: Absolute path to the input folder (used only if `USE_FOLDER` is `True`).
- **OUTPUT_FOLDER**: Absolute path to the output folder where converted images will be saved.
- **RED, GREEN, BLUE**: Pixel conversion ratios for grayscale. Default is set to global grayscale ratios.

### Running the Script

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Image-gray-scale.git
2. Navigate to the project directory:


cd Image-gray-scale
3. Install dependencies: 


pip install -r requirements.txt
4. Edit constants.py to configure parameters as per your requirements.

5. Run the script:

python main.py



