#Install and import PIL/Pillow library
from PIL import Image, ImageFilter

# Function to perform image manipulations
def manipulate_image(image_path, output_path, resize=None, crop_box=None, rotate_angle=None, 
                     flip_method=None, convert_mode=None):
    # Open the image
    image = Image.open(image_path)
    
    # 1. Show the image
    image.show()
    
    # 2. Resize the image if specified
    if resize:
        image = image.resize(resize)
        image.show()
    
    # 3. Crop the image if specified
    if crop_box:
        image = image.crop(crop_box)
        image.show()
    
    # 4. Rotate the image if specified
    if rotate_angle:
        image = image.rotate(rotate_angle)
        image.show()
    
    # 5. Transpose the image (flip horizontally or vertically) if specified
    if flip_method:
        image = image.transpose(flip_method)
        image.show()
    
    # 6. Convert the image to the specified mode (e.g., grayscale) if specified
    if convert_mode:
        image = image.convert(convert_mode)
        image.show()
    
    # 7. Save the final manipulated image
    image.save(output_path)
    print(f"Image saved to {output_path}")


# Function to apply filters
def apply_filters(image_path, output_path, blur=None, contour=None, detail=None, 
                  edge_enhance=None, edge_enhance_more=None, emboss=None, 
                  find_edges=None, sharpen=None, smooth=None, smooth_more=None):
    # Open the image
    image = Image.open(image_path)
    
    # Apply the specified filters if passed
    if blur:
        image = image.filter(ImageFilter.BLUR)
    if contour:
        image = image.filter(ImageFilter.CONTOUR)
    if detail:
        image = image.filter(ImageFilter.DETAIL)
    if edge_enhance:
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    if edge_enhance_more:
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    if emboss:
        image = image.filter(ImageFilter.EMBOSS)
    if find_edges:
        image = image.filter(ImageFilter.FIND_EDGES)
    if sharpen:
        image = image.filter(ImageFilter.SHARPEN)
    if smooth:
        image = image.filter(ImageFilter.SMOOTH)
    if smooth_more:
        image = image.filter(ImageFilter.SMOOTH_MORE)
    
    # Show the image after filter application
    image.show()
    
    # Save the final image with filters applied
    image.save(output_path)
    print(f"Image with filters saved to {output_path}")


# Usage
image_path = 'image.jpg'  # Replace with your image path
output_path = 'output_image.jpg'  # Replace with your desired output path

# Manipulation parameters
resize = (300, 300)  # Resize pixels (set to None to skip)
crop_box = (0, 0, 100, 100)  # Crop to a region from top-left corner (set to None to skip)
rotate_angle = 45  # Rotate by 45 degrees (set to None to skip)
flip_method = Image.FLIP_LEFT_RIGHT  # Flip horizontally (set to None to skip)
convert_mode = 'L'  # Convert to grayscale (set to None to skip)

# Call the function for image manipulation
manipulate_image(image_path, output_path, resize=resize, crop_box=crop_box, 
                 rotate_angle=rotate_angle, flip_method=flip_method, 
                 convert_mode=convert_mode)

# Filter parameters (set to None to skip each filter)
blur = None  # Apply blur filter (set to None to skip)
contour = None  # Apply contour filter (set to None to skip)
detail = None  # Apply detail filter (set to None to skip)
edge_enhance = None  # Apply edge enhance filter (set to None to skip)
edge_enhance_more = None  # Apply edge enhance more filter (set to None to skip)
emboss = None  # Apply emboss filter (set to None to skip)
find_edges = None  # Apply find edges filter (set to None to skip)
sharpen = None  # Apply sharpen filter (set to None to skip)
smooth = None  # Apply smooth filter (set to None to skip)
smooth_more = None  # Apply smooth more filter (set to None to skip)

# Call the function for filter application
apply_filters(image_path, output_path, blur=blur, contour=contour, detail=detail, 
              edge_enhance=edge_enhance, edge_enhance_more=edge_enhance_more, 
              emboss=emboss, find_edges=find_edges, sharpen=sharpen, 
              smooth=smooth, smooth_more=smooth_more)
