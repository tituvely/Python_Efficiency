import os
from PIL import Image

def main():
    size = (150, 150)
    img_file = 'cat.jpg'

    f = ('%s_resized.%s' % (os.path.splitext(img_file)[0], 'jpg'))
    try:
        img = Image.open(img_file)
        img.thumbnail(size)
        img.save(f, 'JPEG', quality=100)
    except IOError:
        print ('Can not create thumbnail for %s' % img_file)

if __name__ == '__main__':
    main()