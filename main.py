# coding:utf-8
# ref: https://pypi.org/project/GPSPhoto/
import os
from GPSPhoto import gpsphoto

def main():
    orig_pic = '/Users/leon/Code/modPhotoGPS/data/IMG_0071.jpg'
    print(os.path.exists(orig_pic))
    data = gpsphoto.getGPSData(orig_pic)
    rawdata = gpsphoto.getRawData(orig_pic)
    for tag in data.keys():
        print("%s: %s" % (tag, data[tag]))

    print("Hellps")


if __name__ == "__main__":
    main()
