# -*- coding: utf-8 -*-
"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

Python2.+ Only
"""

from PIL import Image
import os.path as filepath

def changeResolution(path,resol,saveDir):
    
    img = Image.open(path)
    x,y = img.size
    
    name = filepath.basename(path)
    
    print({name:(x,y)})
    alterx = float(x) / resol[0]
    altery = float(y) / resol[1]
    
    alter = alterx if alterx > altery else altery
    
    if(alter > 1):
        
        try:
            img.resize((int(x/alter),int(y/alter))).save(saveDir)#注意resize的参数是个二元组(x,y)
        except:
            print('alter resolution failed!')
            
if __name__ == '__main__':
    changeResolution('feature2.jpg',(580,481),'feature2-alter.jpg')
