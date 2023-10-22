import os
from PIL import Image
import sys

def resize_image(input_path, output_path, size):
    """Resize the image to the specified size and save it."""
    image = Image.open(input_path)
    image = image.resize((size, size), Image.LANCZOS)
    image.save(output_path, "PNG")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 resize_icon.py <path_to_image> (--ios|--macos)")
        sys.exit(1)

    input_path = sys.argv[1]
    platform = sys.argv[2]
    base_name = input_path.split(".")[0]

    # Create a directory with the name of the original image
    if not os.path.exists(base_name):
        os.mkdir(base_name)

    # Define sizes for iOS and macOS app icons
    ios_sizes = [20, 29, 40, 58, 76, 80, 87, 120, 152, 167, 180, 1024]
    macos_sizes = [16, 32, 64, 128, 256, 512, 1024]

    sizes = ios_sizes if platform == "--ios" else macos_sizes if platform == "--macos" else []

    if not sizes:
        print("Invalid platform specified. Use --ios or --macos.")
        sys.exit(1)

    for size in sizes:
        output_name = f"{base_name}/{base_name}_{size}.png"
        resize_image(input_path, output_name, size)
        print(f"Resized image for {size}x{size}")

    print(f"All sizes for {platform} have been generated and stored in the folder!")

if __name__ == "__main__":
    main()