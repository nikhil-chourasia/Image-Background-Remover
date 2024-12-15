from rembg import remove
from PIL import Image
import os
folderPath = input("Enter the file location here with file name as 'input.jpg': ")
input_path = 'input.jpg'
output_path = os.path.join(folderPath, 'output.png')
input_image = Image.open(os.path.join(folderPath, input_path))
output_image = remove(os.path.join(folderPath, input_path))
output_image.save(output_path)
