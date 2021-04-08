from pdf2image import convert_from_path

import os
count=0
directory = r'/Users/anjana/Documents/DS_Capstone/data-sorted/2_Moderate_Documents/'
for j,filename in enumerate(os.listdir(directory)):
    if filename.endswith(".pdf"):
        images = convert_from_path(directory+filename,fmt='ppm')
        for i, image in enumerate(images):
            count+=1
            filename = filename.rsplit('.', 1)[0]
            fname = "/Users/anjana/Documents/DS_Capstone/data-sorted-copy/Moderate_documents_ppm_new/" + filename + "_"+str(count) + ".ppm"
            image.save(fname, "PPM")
    else:
        continue