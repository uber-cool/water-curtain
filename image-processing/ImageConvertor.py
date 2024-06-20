from BinaryFile import get_binary_file
from TextToFile import add_text_to_file

lines_to_show = ["Hello", "Pramod"]
file_with_text = add_text_to_file(lines_to_show, "target.png", 64)
get_binary_file(file_with_text, "binarized.txt")