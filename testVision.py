#!/usr/bin/python


import argparse
from enum import Enum
import io

from google.cloud import vision
from google.cloud.vision import types as types2
from PIL import Image, ImageDraw
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/tdoe321/projects/AuburnHacks-3a34beb48439.json"

class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5


def draw_boxes(image, bounds, color):
    """Draw a border around the image using the hints in the vector list."""
    draw = ImageDraw.Draw(image)

    for bound in bounds:
        draw.polygon([
            bound.vertices[0].x, bound.vertices[0].y,
            bound.vertices[1].x, bound.vertices[1].y,
            bound.vertices[2].x, bound.vertices[2].y,
            bound.vertices[3].x, bound.vertices[3].y], None, color)
    return image


def get_document_bounds(image_file, feature):
    """Returns document bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bounds = []

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types2.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation



    # Collect specified feature bounds by enumerating all document features
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        if (feature == FeatureType.SYMBOL):
                            bounds.append(symbol.bounding_box)

                    if (feature == FeatureType.WORD):
                        bounds.append(word.bounding_box)

                if (feature == FeatureType.PARA):
                    bounds.append(paragraph.bounding_box)

            if (feature == FeatureType.BLOCK):
                bounds.append(block.bounding_box)

        if (feature == FeatureType.PAGE):
            bounds.append(block.bounding_box)

    # The list `bounds` contains the coordinates of the bounding boxes.
    return bounds


def render_doc_text():
    image = Image.open("med-1.jpg")
    #bounds = get_document_bounds(filein, FeatureType.PAGE)
    #draw_boxes(image, bounds, 'blue')
    bounds = get_document_bounds("med-1.jpg", FeatureType.PARA)
    draw_boxes(image, bounds, 'red')
    #bounds = get_document_bounds(filein, FeatureType.WORD)
    #draw_boxes(image, bounds, 'yellow')

    image.save("out.jpg")


def main():
	render_doc_text()

if __name__ == '__main__':
    main()