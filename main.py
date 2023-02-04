import io

import pyperclip as pyperclip
import webcolors
from PIL import Image
from collections import defaultdict


def get_image_from_clipboard():
    image_data = pyperclip.paste()
    if image_data.startswith("data:image"):
        image = Image.open(io.BytesIO(image_data.split(",")[1].encode()))
        return image
    else:
        print(image_data[:100])
        return None


def get_hex_value(argb_tuple):
    return webcolors.rgb_to_hex(argb_tuple[:3])


def get_colors(image):
    counts = defaultdict(int)
    colors = []
    for y in range(image.height):
        for x in range(image.width):
            rgb = image.getpixel((x, y))
            hex_value = get_hex_value(rgb)
            counts[hex_value] += 1
            if hex_value not in colors:
                colors.append(hex_value)
    return colors, counts


def main():
    image = Image.open("/Users/yanghyeonseo/Downloads/벚꽃.png")
    if image is None:
        print("No image found in clipboard")
        return
    colors, counts = get_colors(image)
    # print(colors, counts)
    avg = sum(counts.values()) / len(counts)
    # print(avg)
    sorted_dict = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    # print(sorted_dict)
    filtered = [color for color in colors if counts[color] > avg]
    print(filtered)


if __name__ == "__main__":
    main()
