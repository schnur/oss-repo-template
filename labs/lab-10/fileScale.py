from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageOps

'''def turnWhite(imageName, newName):
    img = Image.open(imageName+'.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[3]!=0:
            newData.append((255, 255, 255, 255))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(newName+".png", "PNG") '''

img = Image.open("shoe1.jpg")
img = ImageOps.grayscale(img)

np_im = np.array(img)
print(np_im.shape)
np_im = (np_im - np.min(np_im))/np.ptp(np_im)

#print(np_im.shape)
#datas=img.getdata()
#print(datas)
#newData = []

#for item in datas:
    #newData.append((item[0]/255,item[1]/255,item[2]/255,item[3]))
#img.putdata(newData)
plt.imshow(np_im)
plt.show()
#img.save("new"+".jpg", "JPEG")
#new_im = Image.fromarray(np_im)
#new_im.save("new.jpg")
img.close()
#np_im = np.array(im)

#print(np_im)
#new_arr = ((np_im + 0) * (1/1) * 255).astype('uint8')
#print(new_arr)