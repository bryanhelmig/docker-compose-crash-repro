#!/usr/bin/env python

# make a ton of gibberish javascript files, images and python files...

import random
import string
import os

ROOT = 'assets'

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

JS_FOLDER = 'js'
JS_COUNT = 12
JS_BYTES_EACH = 1000 * 1000 * 3 # N megs

def make_js_paths(count=JS_COUNT, root=ROOT):
    for num in range(count):
        yield os.path.join(root, JS_FOLDER, str(num) + '.js')


IMAGE_FOLDER = 'images'
IMAGE_COUNT = 600
IMAGE_PX_SIZE = 128

def make_image_paths(count=IMAGE_COUNT, root=ROOT):
    for num in range(count):
        yield os.path.join(root, IMAGE_FOLDER, str(num) + '.png')


def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in xrange(length))

def make_js_line():
    return 'var {} = "{}";'.format(random_string(50), random_string(500))

def build_js_file(size=JS_BYTES_EACH):
    return '\n'.join(
        make_js_line() for _ in xrange(size / len(make_js_line()))
    )

def build_image_file(px=IMAGE_PX_SIZE):
    import initials_avatar as avatar
    return avatar.bytes(random_string(1), size=px)

def write_js_files(count=JS_COUNT):
    for path in make_js_paths(count=count):
        with open(path, 'w') as f:
            f.write(build_js_file())

def write_image_files(count=IMAGE_COUNT):
    for path in make_image_paths(count=count):
        with open(path, 'w') as f:
            f.write(build_image_file())

if __name__ == '__main__':
    ensure_dir(os.path.join(ROOT, JS_FOLDER))
    ensure_dir(os.path.join(ROOT, IMAGE_FOLDER))
    write_js_files()
    write_image_files()
