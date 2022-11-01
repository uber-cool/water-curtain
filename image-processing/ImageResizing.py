from PIL import Image


def resize_image(source_file, target_file, target_size=[128, 128]):
    src_image = Image.open(source_file)
    src_image.thumbnail(target_size)
    src_image.save(target_file)


resize_image("jali.jpg", "resized.png")
