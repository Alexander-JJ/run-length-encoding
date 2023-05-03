# Run-Length Encoding (RLE) Image Compression
This Python script demonstrates how to apply Run-Length Encoding (RLE) compression on binary-colored images. The program supports BMP, TIFF, PCX, PNG, and JPEG file formats.

## Dependencies
- Python 3.6 or later
- Pillow (Python Imaging Library Fork)

To install Pillow, run the following command:

`pip install Pillow`

## Usage
1. Place your input images (BMP, TIFF, PCX, PNG, or JPEG) in a folder named `input_images` located in the same directory as the script.
2. Run the script:
`ython rle_image_compression.py`
3. The script will compress the images using RLE and save them with a _compressed suffix in the same folder (input_images).

## Output
The program outputs the following information for each image:

- Image name
- Compression time (in seconds)
- Compression ratio (original file size divided by compressed file size)

Please note that this implementation may not provide optimal compression results for the supported file formats, as they have their own specific compression methods. This script serves as a demonstration of RLE compression and can be extended to better handle each file format.
