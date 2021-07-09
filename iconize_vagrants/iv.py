"""Main module."""
#!/bin/sh
from PIL import Image, ImageDraw, ImageFont

import os
import cmapy
import random
import textwrap

def main():
    THRESHOLD = 18

    def luminance(pixel):
        return (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])


    def is_similar(pixel_a, pixel_b, threshold):
        return abs(luminance(pixel_a) - luminance(pixel_b)) < threshold


    colormap = random.choice(['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'])

    fg_color_, bg_color_ = random.sample(range(0, 256), 2)

    bg_color = tuple(cmapy.color(colormap, bg_color_, rgb_order=True))


    curdir = os.getcwd()
    dirname_ = os.path.split(curdir)[-1]

    machines_dir = '.vagrant/machines'
    for machine_ in os.listdir(machines_dir):
        for try_ in range(10):
            fg_color = tuple(cmapy.color(colormap, random.randint(0, 255), rgb_order=True))
            if is_similar(fg_color, bg_color, THRESHOLD):
                continue


        text = f"{machine_}"
        # text = f"{machine_} ({dirname_})"
        idfname_ = f'{machines_dir}/{machine_}/virtualbox/id'
        if os.path.exists(idfname_):
            id_ = open(f'{machines_dir}/{machine_}/virtualbox/id', 'r', encoding='utf-8').read()

            image = Image.new('RGB', (192, 192), color = bg_color)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf", 56, encoding='unic')

            margin = offset = 10
            for line in textwrap.wrap(text, width=7):
                draw.text((margin, offset), line, font=font, fill=fg_color)
                offset += font.getsize(line)[1]

            imgname =  f".image-{machine_}.png"   
            image.save(imgname)
            scmd = f'VBoxManage modifyvm  "{id_}" --iconfile {imgname} '
            print(scmd)
            os.system(scmd)

if __name__ == '__main__':
    main()

