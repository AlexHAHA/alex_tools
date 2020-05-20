import os
import random
from tqdm import tqdm
"""
Function: 读取文件夹内的所有图片文件名并写入txt文件
"""
def generate_txt(txt_file, src_dir):
    f_txt = open(txt_file, mode='w')
    src_pics = os.listdir(src_dir)
    for i,sp in tqdm(enumerate(src_pics)):
        name = os.path.join(src_dir,sp) + "\n"
        f_txt.write(name)

"""
Function: 读取文件夹内的所有图片文件名并打乱图片文件顺序后，按照指定比例存入train.txt和valid.txt文件
"""
def generate_train_and_valid_txt(src_dir, res_dir, ratio="8:2"):
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
            line = os.path.join(src_dir, pic_name)
            f.write(line+'\n')
    
    print(f'writing to valid.txt: {valid_numbers} pics')
    with open(file_valid, mode='w') as f:
        for i in range(train_numbers, len(src_pics)):
            pic_name = os.path.basename(src_pics[i])
            line = os.path.join(src_dir, pic_name)
            f.write(line+'\n')

"""
Function: 对目标文件夹内的所有图片进行重命名，文件名以5位数字顺序命名，从00000开始
"""
def rename_files_withnumbers(src_dir):
    src_pics = os.listdir(src_dir)
    for i,sp in enumerate(src_pics):
        old_file = os.path.join(src_dir,sp)
        #print(old_file)
        # get file's extend name
        ext_name = os.path.splitext(sp)[1]
        #print(ext_name)
        new_file = os.path.join(src_dir,"{:0>5d}{}".format(i,ext_name))
        #print(old_file,new_file)
        os.rename(old_file,new_file)

"""
Function: 对目标文件夹内的所有图片进行重命名，文件名以5位数字顺序命名，从指定序号开始
"""
def rename_files_withstartnumbers(src_dir, start_idx=0):
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

if __name__ == '__main__':
    test_fun2()

