from PIL import Image, ImageFilter

# 1. Open an image from the specified path
image_path = 'weirdhands.jpg'

# Replace with your image path
image = Image.open('weirdhands.jpg')

# 2. Show the image (for debugging)
image.show()

# 3. Resize the image (let's say to 300x300 pixels)
resized_image = image.resize((300, 300))

# Display resized image
resized_image.show()

# 4. Crop the image (cropping a 100x100 area from top-left corner)
cropped_image = image.crop((0, 0, 100, 100))

# Display cropped image
cropped_image.show()

# 5. Rotate the image by 45 degrees
rotated_image = image.rotate(45)

# Display rotated image
rotated_image.show()

# 6. Transpose the image (flip horizontally)
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

# Display flipped image
flipped_image.show()

# 7. Convert the image to grayscale (mode 'L')
grayscale_image = image.convert('L')

# Display grayscale image
grayscale_image.show()

# 8. Apply a filter (e.g., blur the image)
blurred_image = image.filter(ImageFilter.BLUR)

# Display blurred image
blurred_image.show()

# 9. Save the final manipulated image (e.g., save as 'output.jpg')
output_path = 'newhands,jpg'
# Replace with your desired output path
image.save(output_path)
print(f"Image saved to {newhands.jpg}")


