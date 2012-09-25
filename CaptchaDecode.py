import os
from PIL import Image, ImageColor
__author__ = 'lexuzz'

def cmp_image(img1,img2):
    return list(img1.getdata()) == list(img2.getdata())

def crop_white_space(img):
    ss = img.crop((3,6,img.size[0]-7,15))
    gg = Image.new('RGB', (ss.size[0], ss.size[1]))
    gg.paste(ss)
#    gg.save(img.filename[:-4] + '_crop.png', 'PNG')
    return gg

def test_crop(img):
    ss = img.crop((58,0,62,9))
    gg = Image.new('RGB', (ss.size[0], ss.size[1]))
    gg.paste(ss)
    gg.save(img.filename[:-4] + '_crop.png', 'PNG')

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
    return res.replace('_', '')

def decodeImageToData(image_name):
    crop_image = crop_white_space(Image.open(image_name))
    phone_number = decodeImage(crop_image)
    name = image_name.split('__')[0].split('/')[1]
    return name, phone_number


def decodeAllDirImagesToData(images_directory):
    d = {}
    for image_name in os.listdir(images_directory):
        if not image_name.startswith('.'):
            d[decodeImageToData(images_directory + image_name)[0]] = decodeImageToData(images_directory + image_name)[1]
    return d

#test_crop(Image.open(r'input/probel_crop.png'))
#crop_white_space(Image.open(r"input/Roman__3fnj.png"))
#print decodeImage(Image.open(r"input/probel_crop.png"))
decodeAllDirImagesToData('test/')