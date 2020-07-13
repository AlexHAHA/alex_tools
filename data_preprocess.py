"""
Author: alexxue
"""
__version__ = '0.1'
__all__ = ['generate_txt',
            'generate_train_and_valid_txt',
            'rename_files_withstartnumbers',
        ]
import os
import random

def generate_txt(src_dir, txt_file, with_fp=False):
    """
    读取文件夹内的所有图片文件名并写入txt文件

    Args:
    -src_dir: path of images folder
    -txt_file: the file will be written, write the name of each images into each line in txt file
    -with_fp: if true, write each line with image full path, if false, just the image name
    """
    f_txt = open(txt_file, mode='w')
    src_pics = os.listdir(src_dir)

    for i,sp in enumerate(src_pics):
        if with_fp:
            name = os.path.join(src_dir,sp) + "\n"
        else:
            name = sp
        f_txt.write(name)
    print("Finished")

def generate_train_and_valid_txt(src_dir, res_dir, ratio="8:2", with_fp=False):
    """
    读取文件夹内的所有图片文件名并打乱图片文件顺序后，按照指定比例存入train.txt和valid.txt文件

    Args:
    -src_dir: path of images folder
    -res_dir: path of results where train.txt and valid.txt will be created, each line in *.txt if the full path of image
    -ratio: the ratio of train number and valid number
    -with_fp: if true, write each line with image full path, if false, just the image name
    """
    file_train = os.path.join(res_dir, "train.txt")
    file_valid  = os.path.join(res_dir, "valid.txt")
    ratio_train = float(ratio.split(":")[0])/10

    src_pics = os.listdir(src_dir)
    random.shuffle(src_pics)
    train_numbers = int(len(src_pics)*ratio_train)
    valid_numbers = len(src_pics) - train_numbers
    print(f'writing to train.txt: {train_numbers} pics')
    with open(file_train, mode='w') as f:
        for i in range(train_numbers):
            pic_name = os.path.basename(src_pics[i])
            if with_fp:
                line = os.path.join(src_dir, pic_name)
            else:
                line = pic_name
            f.write(line+'\n')
    
    print(f'writing to valid.txt: {valid_numbers} pics')
    with open(file_valid, mode='w') as f:
        for i in range(train_numbers, len(src_pics)):
            pic_name = os.path.basename(src_pics[i])
            if with_fp:
                line = os.path.join(src_dir, pic_name)
            else:
                line = pic_name
            f.write(line+'\n')

def rename_files_withstartnumbers(src_dir, start_idx=0):
    """
    对目标文件夹内的所有图片进行重命名，文件名以5位数字顺序命名，从指定序号开始

    Args:
    -src_dir: path of images folder
    -start_idx: the start number will be used as the new name for first image
    """
    src_pics = os.listdir(src_dir)
    for i,sp in enumerate(src_pics):
        old_file = os.path.join(src_dir,sp)
        #print(old_file)
        # get file's extend name
        ext_name = os.path.splitext(sp)[1]
        #print(ext_name)
        new_file = os.path.join(src_dir,"{:0>5d}{}".format(i+start_idx,ext_name))
        #print(old_file,new_file)
        os.rename(old_file,new_file)

def test_fun1():
    path = r"D:\CETCA_DeepLearning\CETCA_UAVDataSet\dataset_zigong20200109\images"
    rename_files_withstartnumbers(path)

def test_fun2():
    path_images = r"D:\CETCA_DeepLearning\CETCA_UAVDataSet\dataset_htswinter_ruanjiangongchengbu2\outputs\images"
    path_main  = r"D:\CETCA_DeepLearning\CETCA_UAVDataSet\dataset_htswinter_ruanjiangongchengbu2\outputs"
    generate_train_and_valid_txt(path_images, path_main)
def generate_txt
if __name__ == '__main__':
    test_fun2()

