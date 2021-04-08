import os
import shutil


src1 = './good_combined'
dest1 = './Good_compiled'



src2 = './moderate_combined/'
dest2 = './Moderate_compiled/'


src3 = './bad_combined'
dest3 = './Bad_compiled'

for file in os.listdir(src1):

    prefix = str(file.split('_')[0])
    path = dest + prefix
    print(path)
    if not os.path.exists(path):
        os.makedirs(path)

    shutil.copyfile(src+file,path+'/'+file) 
