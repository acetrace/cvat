#!/usr/local/bin/python3
import os
import sys
from PIL import Image
import re

# Converts multiple video files to images in corresponding individual folder:
# - dir
#     - images
#         - frame_000001.PNG
#         - frame_000002.PNG
#
#
def video_to_images(dir):
    dir = os.path.join(dir, 'images')
    for filename in sorted(os.listdir(dir)):
        path = os.path.join(dir, filename)
        if os.path.isfile(path):
            prefix_match = re.search('frame_(\\d+)\\.PNG', filename, re.IGNORECASE)
            if prefix_match:
                print("converting " + filename + "...")
                out_name = '00' + prefix_match.group(1) + '.jpg'
                jpg_path = os.path.join(dir, out_name)
                im = Image.open(path)
                rgb_im = im.convert('RGB')
                rgb_im.save(jpg_path)
                os.remove(path)

def update_coco_paths(dir):
    path = os.path.join(dir, 'annotations', 'instances_default.json')
    if os.path.isfile(path):
        with open(path, 'r') as f:
            text = f.read()
            text = re.sub('frame_(\\d+)\\.PNG', '00\\1.jpg', text)
            f.close()
            with open(path, 'w') as out:
                out.truncate()
                out.write(text)
                out.close()

if __name__ == '__main__':
    dir = sys.argv[1]
    video_to_images(dir)
    update_coco_paths(dir)
