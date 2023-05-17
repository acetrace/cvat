#!/usr/local/bin/python3
import os
import sys
import json
from cli import main

#
# dir - a path to a directory with videos
# ----------
#  dir
#   - video_1.mov
#   - video_2.mp4
# =====================================
# Could be a set of frame images as well
# ----------
# dir
#   - video_1
#       - frame1.jpg
#       - frame2.jpg
#       - ....
#       - frameN.jpg
#   - video_2
#       - ...
#
dir = sys.argv[1]
project_id = f"{sys.argv[2]}"
credentials = sys.argv[3] if len(sys.argv) > 3 else 'acetrace:PofigPofig1'

labels = [{"name": "golball", "color": "#f68e83", "attributes": []}]
for filename in sorted(os.listdir(dir)):
    filepath = os.path.join(dir, filename)
    if os.path.isdir(filename):
        resources = [filepath + "/" + file for file in os.listdir(filepath)]
        main(['--auth', credentials, '--server-host', '18.191.203.127', '--server-port', '8080', 'create', '--labels',
              json.dumps(labels), '--project_id', project_id, '--image_quality', '100', filename, 'local', resources])
    else:
        main(['--auth', credentials, '--server-host', '18.191.203.127', '--server-port', '8080', 'create', '--labels',
              json.dumps(labels), '--project_id', project_id, '--image_quality', '100', filename, 'local', filepath])
