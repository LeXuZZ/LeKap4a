import os
from PIL import Image, ImageColor
__author__ = 'lexuzz'

def cmp_image(img1,img2):
    return list(img1.getdata()) == list(img2.getdata())

def crop_white_space(img):
    gg = Image.new('RGB', (img.size[0], 9))
    ss = img.crop((3,6,img.size[0]-7,15))
    gg.paste(ss)
    gg.save(img + '_crop.png', 'PNG')

def decodeImage(input_img):
    global letter_image
    start_point = 0
    res = ""
    while start_point < input_img.size[0]:
        letter = "*"
        for img in os.listdir('letters/'):
            letter_image = Image.open('letters/' + img)
            a = input_img.crop((start_point, 0, letter_image.size[0]+start_point, letter_image.size[1]))
            rms = cmp_image(letter_image, a)
            if rms:
                letter = img[:-4]
                break
        start_point += letter_image.size[0]
        res += letter
    return res


crop_white_space(Image.open(r"tmp_image.png"))
print decodeImage(Image.open(r"2_ryada.png"))
#img = Image.open(r"slando_all.png")
#crop_white_space(Image.open(r"tmp_image.png"))
#print decode(Image.open(r"slando_all1.png"))