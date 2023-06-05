from operator import is_
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def draw_cross(image_path, color):
 is_horizontal = input('horizontal? True / False ')
 if is_horizontal == 'True':
  is_horizontal = True
 else:
  is_horizontal = False
 img = Image.open(image_path).convert('RGB')
 pixels = img.load()
 width, height = img.size

 if is_horizontal:
  for i in range(width):
   pixels[i, height // 2] = color
 else:
  for j in range(height):
   pixels[width // 2, j] = color

 img.save('output.png')

#viewer = [[]]*2 # массив саб графиков
#for i in range(2):
 #viewer[i] = fig.add_subplot(plot_countx,plot_county,i+1)
 #viewer[i].imshow(np.array(image_box[i])) # делаем график изображения
#fig.show()

 # Plot color distribution of original image
 img_output_1 = Image.open('/content/drive/MyDrive/Python/dataf/753ee15e228fb5f2a89a4f09e530e31b.jpg')
 r, g, b = img.split()
 colors = ('r', 'g', 'b')
 for channel, color in zip((r, g, b), colors):
  plt.hist(np.array(channel).ravel(), bins=256, color=color, alpha=0.5)

 # Plot color distribution of output image
 img_output = Image.open('output.png')
 r, g, b = img_output.split()
 colors = ('r', 'g', 'b')
 for channel, color in zip((r, g, b), colors):
  plt.hist(np.array(channel).ravel(), bins=256, color=color, alpha=0.5)

 img1 = Image.open(image_path)
 # Show original and output images
 fig, axs = plt.subplots(1,2)
 axs[0].imshow(img1)
 axs[0].set_title('Original Image')
 axs[1].imshow(img_output)
 axs[1].set_title('Output Image')

 plt.show()

# Example usage:
draw_cross('/content/drive/MyDrive/Python/dataf/753ee15e228fb5f2a89a4f09e530e31b.jpg', (255, 0, 0))




