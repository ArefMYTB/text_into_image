from PIL import Image, ImageDraw, ImageFont
import numpy as np


def generate_text_image(text, font_path, font_size, output_path, image_size, text_color=(0, 0, 0)):
    img = Image.new('RGB', image_size, color='white')

    font = ImageFont.truetype(font_path, size=font_size)
  
    font = ImageFont.truetype(font_path, size=font_size)
  
    draw = ImageDraw.Draw(img)
  
    text_width = draw.textlength(text, font=font)
    text_height = font_size

    placement = (min_x + ((max_x - min_x) // 2 - text_width // 2), \
        min_y + ((max_y - min_y) // 2 - text_height // 2))

    draw.text(placement, text, fill=text_color, font=font)
  
    img.save(output_path)
    img.show()


font_size = 50
user_text = "fashion"
user_font_path = "C:/Windows/Fonts/Candara.ttf"
input_mask_path = "./mask2.jpg"
output_image_path = "text.jpg"

mask = Image.open(input_mask_path).convert("L")

mask_array = np.array(mask)

white_pixels = np.where(mask_array == 255)
min_x = np.min(white_pixels[1])
max_x = np.max(white_pixels[1])
min_y = np.min(white_pixels[0])
max_y = np.max(white_pixels[0])
bounding_box = (min_x, min_y, max_x, max_y)

generate_text_image(user_text, user_font_path, font_size, output_image_path, mask.size)
