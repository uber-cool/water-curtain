from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def get_font_size(text, pixels):
    length = len(text)
    width_per_letter = int(pixels / length)
    return int(1.5 * width_per_letter)


def get_font_object(font_path, lines, pixels):
    final_font_size = 100000
    for text in lines:
        approximate_font_size = get_font_size(text, pixels)
        if approximate_font_size < final_font_size:
            final_font_size = approximate_font_size
            largest_line = text

    while True:
        font_object = ImageFont.truetype(font_path, final_font_size, encoding='unic')
        get_length = font_object.getlength(largest_line)
        if get_length < pixels:
            final_font_size += 1
        else:
            font_object = ImageFont.truetype(font_path, final_font_size - 1, encoding='unic')
            break

    return font_object


def add_text_to_file(lines_to_show, target_file_path, pixels=128, font_file_path="fonts/BakbakOne-Regular.ttf"):

    font = get_font_object(font_file_path, lines_to_show, pixels)
    joined_text = "\n".join(lines_to_show)

    multiline = font.getsize_multiline(joined_text)
    blank_image = Image.new("RGB", (pixels, multiline[1]), (255, 255, 255))
    blank_image.save("blank_image.png", "PNG")

    image_editable = ImageDraw.Draw(blank_image)
    image_editable.text((0, 1), joined_text, (0, 0, 0), font=font, align="center")
    blank_image.save(target_file_path)
    return target_file_path
