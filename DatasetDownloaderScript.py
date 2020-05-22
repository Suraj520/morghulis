from morghulis.widerface import Wider
widerface_home = 'datasets/widerface'
!mkdir -p {widerface_home}
widerface = Wider(widerface_home)
widerface.download()
len([img for img in widerface.images()])
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
darknet_output_dir = '{}/darknet'.format(widerface_home)
widerface.export(darknet_output_dir, target_format='darknet')

"""widerface.__dict__

!tail  datasets/widerface/wider_face_split/wider_face_train_bbx_gt.txt

"""Check that darknet artifacts were properly created:"""

!ls {darknet_output_dir}

!cat {darknet_output_dir}/train.txt

!wc -l {darknet_output_dir}/train.txt

!ls -la {darknet_output_dir}/
!pip install --upgrade pillow==6.1.0

from PIL import Image 



Image.open('datasets/widerface/WIDER_train/images/0--Parade/0_Parade_marchingband_1_849.jpg')"""
