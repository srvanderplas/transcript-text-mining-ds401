import os
from multiprocessing import Pool


def do_stuff(src,dest):
    i = 0
    for file in os.listdir(src):
        i+=1

        from_name = file.rsplit('.', 1)[0] + '.ppm'
        to_name = file.rsplit('.', 1)[0] + '.png'
        print(dest,to_name,i)
        from_name = from_name.replace(' ','\ ')
        to_name = to_name.replace(' ','\ ')

        cmd = "magick convert " + src + from_name+ " "+ dest + to_name 
        os.system(cmd)

def do_stuff_in_parallel():
    src1 = './Bad_documents_ppm_output/'
    dest1 = './Bad_documents_png/'
    os.makedirs(dest1)
    do_stuff(src1,dest1)

    src2 = './Good_documents_ppm_output/'
    dest2 = './Good_documents_png/'
    os.makedirs(dest2)
    do_stuff(src2,dest2)

    src3 = './Moderate_documents_ppm_output/'
    dest3 = './Moderate_documents_png/'
    os.makedirs(dest3)
    do_stuff(src3,dest3)

    inputs = [[src1,dest1],[src2,dest2],[src3,dest3]]
    pool = Pool(processes=len(inputs))
    pool.map(do_stuff, inputs)

if __name__ == '__main__':
    do_stuff_in_parallel()