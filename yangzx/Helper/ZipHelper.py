import zipfile
import os
import sys

"""
压缩指定文件夹下的所有文件
:param dirpath: 目标文件夹路径
:param outFullName: 压缩文件保存路径+xxxx.zip
:return: 无
"""
def ZipDir(dirpath='', outFullName=''):
    #outFullName = "..\\..\\..\\Communal\\ReversalPicture.zip"
    #dirpath = "..\\..\\..\\Communal\\ReversalPictureImg"
    if dirpath == '':
        print("缺少压缩路径目标")
        return False
    if outFullName == '':
        print("缺少保存路径，默认保存至当前文件夹下")
        outFullName = sys.path[0] + "\\File.zip"
    with zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            #fpath = path.replace(dirpath, '')
            fpath = dirpath
            for filename in filenames:
                zf.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zf.close()
    print("文件夹\"{0}\"已压缩为\"{1}\".".format(dirpath, outFullName))
    
    
    
    
# 主函数
if __name__ == '__main__':
    ZipDir()