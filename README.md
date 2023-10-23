# Iconize

**Iconize** is a command-line tool designed to assist developers in creating the myriad of icon sizes required for Xcode projects, especially when targeting both iOS and macOS platforms. With the varying device sizes and resolutions, ensuring that your app icon looks crisp and clear on all devices can be a challenge. Iconize simplifies this process, allowing developers to focus on building great apps.

## Installation
To install Iconize globally:
```bash
pip install git+https://github.com/nicolaischneider/Iconize.git
```

## Usage
```bash
iconize <path_to_image> [--macos] [--ios] [--specific <sizes>]
```

### Parameters:

- **path_to_image**: The path to the image you want to resize.
  
- **--macos**: Resize the image for macOS. This will resize the image to the following sizes: 16, 32, 64, 128, 256, 512, 1024 pixels.

- **--ios**: Resize the image for iOS. This will resize the image to the following sizes: 20, 29, 40, 58, 76, 80, 87, 120, 152, 167, 180, 1024 pixels.

- **--specific**: Specify custom sizes to resize to. For example: `--specific 20 30` will resize the image to 20x20 and 30x30 pixels.

> **Note**: Only one of `--macos`, `--ios`, or `--specific` should be used at a time.

### Examples:

1. To resize an image for macOS:
   ```bash
   iconize image.png --macos
   ```

2. To resize an image for iOS:
   ```bash
   iconize image.png --ios
   ```

3. To resize an image to specific sizes (here 20x20 and 30x30 pixels):
   ```bash
   iconize image.png --specific 20 30
   ```

After resizing, the tool will create a directory named after the original image and store all the resized images inside that directory.

## Contributing

If you find any issues or have suggestions, please create an issue.