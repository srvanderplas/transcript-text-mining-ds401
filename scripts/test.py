import os

i = 0
done = set(os.listdir('./Bad_documents_ppm_output/'))
for file in os.listdir('./Bad_documents_ppm_new/'):
    i+=1
    print(i)
    f = file.rsplit('.', 1)[0] + '.ppm'
    f = f.replace(' ','\ ')
    if f not in done:   
        cmd = "unpaper ./Bad_documents_ppm_new/" + f+ "  ./Bad_documents_ppm_output/" + f 
        os.system(cmd)