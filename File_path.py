#输出指定位置下所有文件的路径
import os
def print_directory_contents(sPath):
    for sChlild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChlild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            #print(sChildPath)
            with open("C://path.txt", 'a') as fp:
                fp.write(sChildPath)
                fp.write('\n')

if __name__ == "__main__":
    sPath = ''
    sPath = input("Please Input the Path of File:")
    if 'path.txt' in os.listdir('C://'):
        os.remove("C://path.txt")
    print_directory_contents(sPath)

