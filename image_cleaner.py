from PIL import Image
import numpy 

img = Image.open('mario_right_small.png')



img2 = numpy.array(img)

output = numpy.zeros([int(img2.shape[0]),int(img2.shape[1]),3])

for i in range (int(img2.shape[0])):
	for j in range (int(img2.shape[1])):
		for rgb in range(3):
			output[i][j][rgb] = img2[i][j][rgb]
		if output[i][j][0]==238 or output[i][j][0] == 239:
			for rgb in range(3):
				output[i][j][rgb] = 255



output2 = Image.fromarray(numpy.uint8(output))
output2.show()
output2.save('mario_right_small_clean.png')