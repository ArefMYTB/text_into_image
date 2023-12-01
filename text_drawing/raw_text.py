
from PIL import Image, ImageDraw, ImageFont


def generate_text_image(text, font_path, output_path, image_size=(400, 200), text_color=(0, 0, 0)):
    img = Image.new('RGB', image_size, color='white')

    font = ImageFont.truetype(font_path, size=40)
  
    draw = ImageDraw.Draw(img)
    draw.text((180, 80), text, fill=text_color, font=font)
  
    img.save(output_path)
    img.show()


# Example usage
user_text = "Fine"
user_font_path = "Sookie.ttf"
output_image_path = "generated_image.jpg"

generate_text_image(user_text, user_font_path, output_image_path)
