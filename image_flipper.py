from PIL import Image
import numpy 

img = Image.open('mario_enemy.png')



img2 = numpy.array(img)

output = numpy.zeros([int(img2.shape[0]/10),int(img2.shape[1]/10),3])

for i in range (int(img2.shape[0]/10)):
	for j in range (int(img2.shape[1]/10)):
		for rgb in range(3):
			output[i][j][rgb] = img2[i*10][j*10][rgb]


output2 = Image.fromarray(numpy.uint8(output))
output2.show()
output2.save('mario_enemy_small.png')
