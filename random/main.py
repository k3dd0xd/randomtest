from PIL import Image, ImageFilter

img1 = Image.open("Umbrella2_Raw.png")

img = img1.filter(ImageFilter.DETAIL)

img.save("Umbrella2_detail.png")