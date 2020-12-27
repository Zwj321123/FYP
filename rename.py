# importing os module
import os

num = 576
for count, filename in enumerate(os.listdir("E:/study/S3/FYP/Dataset/woods")):
    dst =str(num+count) + ".jpg"
    src ='E:/study/S3/FYP/Dataset/woods/'+ filename
    dst ='E:/study/S3/FYP/Dataset/woods/'+ dst

    # rename() function will
    # rename all the files
    os.rename(src, dst)
