from PIL import Image

def image_resize(w,h):
    img = Image.open('maxresdefault.jpg')
    print(f"Currnt image size {img.size}")
    new_img = img.resize((w,h))
    new_img.save(f"maxresdefault{str(w)}x{str(h)}.jpg")

width = int(input("Enter Width of the image : "))
height = int(input("Enter Height of the image : "))
image_resize(width,height)
