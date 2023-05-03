import os
import time
from PIL import Image

def rle_encode(image):
    data = list(image.getdata())
    rle = []
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            rle.append((data[i - 1], count))
            count = 1

    rle.append((data[-1], count))
    return rle

def rle_compress_image(input_file, output_file):
    image = Image.open(input_file)
    image = image.convert("1")
    start_time = time.time()

    rle_data = rle_encode(image)
    compressed_image = Image.new("1", image.size)
    compressed_image.putdata([x[0] for x in rle_data for _ in range(x[1])])

    compressed_image.save(output_file)

    end_time = time.time()
    compression_time = end_time - start_time
    original_size = os.path.getsize(input_file)
    compressed_size = os.path.getsize(output_file)
    compression_ratio = original_size / compressed_size

    return compression_time, compression_ratio

def main():
    supported_formats = ['.bmp', '.tiff', '.pcx', '.png', '.jpeg', '.jpg']
    input_directory = "Your/Directory/Here"

    for filename in os.listdir(input_directory):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in supported_formats:
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(input_directory, f"{os.path.splitext(filename)[0]}_compressed{file_ext}")

            compression_time, compression_ratio = rle_compress_image(input_file, output_file)

            print(f"Image: {filename}")
            print(f"Compression time: {compression_time:.2f} seconds")
            print(f"Compression ratio: {compression_ratio:.2f}")

if __name__ == "__main__":
    main()
