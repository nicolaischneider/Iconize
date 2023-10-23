import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='An Image Resizer by Nicolai Schneider.')
    parser.add_argument('image_path', type=str, help='Path to the image to be resized')
    parser.add_argument('--macos', action='store_true', help='Resize image for macOS')
    parser.add_argument('--ios', action='store_true', help='Resize image for iOS')
    parser.add_argument('--specific', nargs='+', type=int, help='Specific sizes to resize to. E.g. --specific 20 30, this will resize the image to 20x20 and 30x30 pixels.')
    args = parser.parse_args()

    if sum([args.macos, args.ios, args.specific is not None]) != 1:
        parser.error('Multiple parameters can\'t be set.')

    return args