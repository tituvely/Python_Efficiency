import os
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

def get_exif_info():
    # img_file에 스마트폰으로 찍은 사진을 넣으면 GPS 정보가 출력됨
    img_file = 'minions.jpg'
    img = Image.open(img_file)

    exif = img._getexif()
    if exif is None:
        print('There are no exif information in the photo.')
        return

    exif_data = {}
    for tag_id, tag_value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        
        if tag == 'GPSInfo':
            gps_data = {}
            for gps_id in tag_value:
                gps_tag = GPSTAGS.get(gps_id, gps_id)
                gps_data[gps_tag] = tag_value[gps_id]

            exif_data[tag] = gps_data
        else:
            exif_data[tag] = tag_value
    
    return exif_data

def print_exif_info(exif_data):
    for key, value in exif_data.items():
        if type(value) is dict:
            for sub_key, sub_value in value.items():
                print('%s : %s' % (sub_key, sub_value))
            
            continue
    
        print('%s : %s' % (key, value))

def main():
    print_exif_info(get_exif_info())

if __name__ == '__main__':
    main()