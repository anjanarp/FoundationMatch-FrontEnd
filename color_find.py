import os, io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/anjanaparasuram/webpage_test/venv/ServiceAccountToken.json"

client = vision.ImageAnnotatorClient()

file_path = '/Users/anjanaparasuram/Desktop/forehead.JPG'

def color_find(file_path): 
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.image_properties(image=image).image_properties_annotation
    return response.dominant_colors

file1 = '/Users/anjanaparasuram/Desktop/forehead.JPG'


print(color_find(file1))
