from PIL import Image
from main import save_edited_image
from main import add_to_edited_table

def watermark_photo(input_image_path, watermark_image_path, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
     # add watermark to image
    if (base_image.size > watermark.size):
        base_image.paste(watermark, position)
        save_edited_image(base_image, 'newimage.jpg')
        #base_image.show()

