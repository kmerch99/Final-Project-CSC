#user would import image from files
from PIL import Image

from PIL import Image, ImageEnhance, ImageFilter

def blur_image (img, radius=5):
    """
    Applies Gaussian blur to the input image with the given radius.
    """
    return img.filter(ImageFilter.GaussianBlur(radius))

def resize_image(img, new_width, new_height):
    """
    Resizes the input image to the specified width and height.
    """
    return img.resize((new_width, new_height))

def adjust_contrast(img, factor=1.0):
    """
    Adjusts the contrast of the input image.
    A factor if 1.0 means no change.
    Values less than 1.0 reduce contrast, values greater than 1.0 increase contrast
    """
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)

def merge_images(img1, img2, alpha=0.5):
    """
    Merges two images together with a given alpha (transparency) value.
    Resizes img2 to be the size of img1 before blending.
    """
    img2_resized = img2.resize(img1.size)
    return Image.blend(img1, img2_resized, alpha)

def manipulate_image(img1, img2=None, blur_radius=None, contrast_factor=1.4,
                     new_width=None, new_height=None, alpha=None):
    """
    Manipulate an image based on provided parameters.

    Parameters:
    - blur_radius: Apply Gaussian blur if value is provided.
    - contrast_factor: Adjust contrast if value is provided.
    - new_width, new_height: Resize the image if values are provided.
    - alpha: Merge img1 with img2 if alpha and img2 are provided.

    The function applies with the operations in sequence, and each operation is optional
    """
    #load an image
    img = Image.open('weirdhands.jpg')

     #Step 1: Apply blur (if blur_radius is provided)
    if blur_radius is not None:
        img1 = blur_image(img1, blur_radius)

    #Step 2: Adjust contrast (if contrast_factor is provided)
        if contrast_factor is not None:
            img1 = adjust_contrast(img1, contrast_factor)

    #Step 3: Resize image (if new_width and new_height are provided)
        if new_width is not None and new_height is not None:
            img1 = resize_image(img1, new_width, new_height)

    #Step 4: Merge with another image (if img2 and alpha are provided)
        if img2 is not None and alpha is not None:
            img1 = merge_images(img1, img2, alpha)

    #Display the image
            Image.show()

    #Return the manipulated image
        return img

    
