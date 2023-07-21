from PIL import Image
def get_concat_h(im1, im2):
        images = Image.new('RGB', (im1.width, im1.height + im2.height))
        images.paste(im1, (0, 0))
        images.paste(im2, (im1.width, 0))
        return images
