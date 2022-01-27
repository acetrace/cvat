import os
import sys
import json
from cli import run

dir = sys.argv[1]

for filename in sorted(os.listdir(dir)):
    filepath = os.path.join(dir, filename)
    ann = annotations_path + "/" + filename + ".json"
    resources = [filepath + "/" + file for file in os.listdir(filepath)]
    run(['--auth', credentials, '--server-host', 'localhost', '--server-port', '8080', 'create', '--labels', json.dumps(labels), '--annotation_path', ann, '--annotation_format', 'COCO 1.0', '--project_id', project_id, '--image_quality', '100', filename, 'local', resources])

    #'--annotation_format', 'COCO 1.0'

