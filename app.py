
import re
import base64
import sys

import eel

from lib.camera import Camera


def parse_args():
    # TODO: not comprehensive
    num_args = len(sys.argv)
    outp = {}

    for idx in range(1, num_args):
        arg = sys.argv[idx]
        match = re.search("^--", arg)

        if match != None:
            key = re.sub("^--", "", arg)
            outp[key] = []
        else:
            outp[key].append(arg)

    for key in outp:
        if len(outp[key]) == 1:
            outp[key] = ''.join(outp[key])
        elif len(outp[key]) == 0:
            outp[key] = True

    return outp


@eel.expose
def start_video_feed():
    data = cam.read_stream()

    for each in data:
        # Convert bytes to base64 encoded str, as we can only pass json to frontend
        blob = base64.b64encode(each)
        blob = blob.decode("utf-8")
        eel.updateImageSrc(blob)()

@eel.expose
def take_snapshot(filename):
    path = snapshot_folder + '/'
    cam.take_snapshot(path + filename)


args = parse_args()
options = {
    'mode': 'chrome',
    'cmdline_args': ['--kiosk'],
    'size': (800, 600),
    'position': (50, 50)
}

usage_msg = f"""
    usage: { sys.argv[0] } [FLAGS]
        --help                  show this usage text
        --snapshots <folder>    override default snapshots folder [snapshots]
        --device <id>           override default device id [0]
"""

if args.get('help', None) == True:
    print(usage_msg)
    sys.exit()

snapshot_folder = args.get('snapshots', 'snapshots')
dev_id = int(args.get('device', '0'))
cam = Camera(dev_id)

eel.init('assets')
eel.start('index.html', **options)