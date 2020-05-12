import torch
from torchtext import data

import os
import cv2

from bounding_box import bounding_box
from PIL import Image


INPUT_IMG_DIR = "/fcos/datasets/coco/val2017"
OUTPUT_IMG_DIR = "/visualizer/output"
INFERENCES_RESULT = "/fcos/output/fcos/R_50_1x/inference/coco_instances_results.json"

fields = {"image_id": ("image_id", data.Field()), "bbox": (
    "bounding_box_lrtb", data.Field(sequential=True))}
inference_result = data.TabularDataset(
    path=INFERENCES_RESULT, format='json', fields=fields)

# print(inference_result.examples[0].number[0])
# print(inference_result.examples[0].lrtb[0])

# for root, dirs, files in os.walk(INPUT_IMG_DIR):
# print(files)

assert(len(inference_result.examples[0].image_id) == len(
    inference_result.examples[0].bounding_box_lrtb))

for i in range(len(inference_result.examples[0].image_id)):
    image_id = inference_result.examples[0].image_id[i]
    bounding_box_lrtb = inference_result.examples[0].bounding_box_lrtb[i]

    input_image_path = INPUT_IMG_DIR + "/" + str(image_id).zfill(12) + ".jpg"
    output_image_path = OUTPUT_IMG_DIR + "/" + str(i) + ".jpg"

    # assert(bounding_box_lrtb[0] < image)
    image = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

    print("bounding_box: ", bounding_box_lrtb)
    print("image: ", image.shape)

    """
    assert(bounding_box_lrtb[0] <= image.shape[1])
    assert(bounding_box_lrtb[1] <= image.shape[1])
    assert(bounding_box_lrtb[2] <= image.shape[0])
    assert(bounding_box_lrtb[3] <= image.shape[0])
    """

    bounding_box.add(
        image, bounding_box_lrtb[0], bounding_box_lrtb[2], bounding_box_lrtb[1], bounding_box_lrtb[3])
    cv2.imwrite(output_image_path, image)
