from rembg import remove
from PIL import Image

input_path = "bg_remove//pic.png"
output_path = "bg_remove//new1.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
