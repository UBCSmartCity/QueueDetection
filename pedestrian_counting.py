#----------------------------------------------
#--- Author         : Ahmet Ozlu
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 27th January 2018
#----------------------------------------------

# Imports
import tensorflow as tf

# Object detection imports
from utils import backbone
from api import object_counting_api

# input_video = "./input_images_and_videos/pedestrian_survaillance.mp4"
# input_video = './input_images_and_videos/1054114508-preview.mp4'
# input_video = './input_images_and_videos/1058054536-preview.mp4'

# input_video = './input_images_and_videos/1043996653-preview.mp4'
# input_video = './input_images_and_videos/stock-footage-people-queue-or-waiting-in-line.mp4'
# input_video = "./input_images_and_videos/ubc4.avi"
input_video = "./input_images_and_videos/ubc3.avi"


# By default I use an "SSD with Mobilenet" model here. See the detection model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtxt')

is_color_recognition_enabled = False # set it to true for enabling the color prediction for the detected objects
roi = 540 # roi line position #385
deviation = 10 # the constant that represents the object counting area #1
custom_object_name = 'person'
object_counting_api.cumulative_object_counting_x_axis(input_video, detection_graph, category_index, is_color_recognition_enabled, roi, deviation, custom_object_name) # counting all the objects




# for x axis , roi = 385
#  for y axis , roi = 185