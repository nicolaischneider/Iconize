import os
from PIL import Image


def resize_image(input_path, output_path, size):
    image = Image.open(input_path)
    image = image.resize((size, size), Image.LANCZOS)
    image.save(output_path, "PNG")


def create_output_folder(image_path):
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_folder = os.path.join(os.path.dirname(image_path), base_name)

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    return output_folder, base_name


def resize_images(image_path, sizes):
    output_folder, base_name = create_output_folder(image_path)

    print()
    for size in sizes:
        output_name = f"{output_folder}/{base_name}_{size}.png"
        resize_image(image_path, output_name, size)
        print(f"Resized image for {size}x{size}")

    print()
    print("----------")
    print(
        f"All images have been resized. The images can be found here:\n{os.path.abspath(output_folder)}"
    )
    print()


def resize_for_macos(image_path):
    macos_sizes = [16, 32, 64, 128, 256, 512, 1024]
    resize_images(image_path, macos_sizes)


def resize_for_ios(image_path):
    ios_sizes = [20, 29, 40, 58, 76, 80, 87, 120, 152, 167, 180, 1024]
    resize_images(image_path, ios_sizes)


def resize_for_specific(image_path, sizes):
    resize_images(image_path, sizes)
