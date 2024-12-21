# Image Background Remover 🎨🖼️

This project is a simple **Command-Line Interface (CLI) tool** for removing the background of an image using Python. It utilizes the `rembg` library to perform background removal and outputs the processed image with a transparent background. ✂️✨

## Features 🚀

- Removes the background from an image effortlessly. 🎯
- Accepts input as a `.jpg` file and outputs the result as a `.png` file with a transparent background. 🖌️
- Lightweight and efficient, leveraging the power of the `rembg` library. ⚡

## Prerequisites ✅

Ensure you have the following installed on your system:

- Python (>= 3.6) 🐍
- Pip (Python package manager) 📦

## Installation 🛠️

1. Clone the repository or download the script.

    ```
    git clone https://github.com/nikhil-chourasia/Image-Background-Remover.git
    cd Image-Background-Remover
    ```

2. Install the required Python libraries:

    ```
    pip install rembg pillow
    ```

## Usage 🖥️

1. Place the input image (named `input.jpg`) in the folder where the script is located.
2. Run the script using the command:

    ```
    python image_background_remover.py
    ```

3. When prompted, enter the full folder path where the image is located (ensure the image is named `input.jpg`):

    ```
    Enter the file location here with file name as 'input.jpg': /path/to/folder
    ```

4. The script will process the image and save the output as `output.png` in the same folder. 🖼️✨

## How It Works 🤔

1. The script uses the `rembg` library to process the background removal. ✂️
2. The input image is read using the `Pillow` library. 🖼️
3. The processed image is saved with a transparent background as `output.png`. 🌈

## Notes 📝

- Make sure the input image is named `input.jpg`. 📂
- The output image will be saved as `output.png` in the same folder as the input image. 🖌️
- You can modify the script to customize input and output paths or add error handling as needed. 🛠️

## Contributing 🤝

Feel free to contribute to this project by submitting issues or pull requests. Let's make it better together! 🌟

## License 📜

This project is licensed under the MIT License. See the LICENSE file for details. 🏷️
