from BinaryFile import get_binary_file
from TextToFile import add_text_to_file


file_with_text = add_text_to_file("Hari Om", "target.png", 128)
get_binary_file(file_with_text, "binarized.txt")