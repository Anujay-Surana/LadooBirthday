import os
import json

# Path to your images folder
images_path = './images/'
images_list = os.listdir(images_path)

# Filter list for image files if needed (by extension)
images_list = [img for img in images_list if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Print the list in JSON format
print(json.dumps(images_list))
print(len(images_list))
