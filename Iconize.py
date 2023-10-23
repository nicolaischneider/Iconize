from argument_parser import parse_args
from image_resizer import resize_for_macos, resize_for_ios, resize_for_specific


def main():
    args = parse_args()

    image_path = args.image_path

    if args.macos:
        resize_for_macos(image_path)
    elif args.ios:
        resize_for_ios(image_path)
    elif args.specific:
        resize_for_specific(image_path, args.specific)


if __name__ == "__main__":
    main()
