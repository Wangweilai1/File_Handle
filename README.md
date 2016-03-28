#根据文件特定位置内容，改文件内容
import os
import re
def file_change(sChildPath, Queue, string2):
    i = 0
    with open(sChildPath) as fp:
        for line in fp.readlines():
            i = i + 1
            if i == 2:
                Queue[sChildPath] = line[-4:-1]
                string2.append(line[-4:-1])
                
def get_directory_contents(sPath, Queue, string1, string2):
    for sChlild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChlild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            string1.append(sChildPath)
            file_change(sChildPath, Queue, string2)



if __name__ == "__main__":
    sPath = ''
    Queue = {}
    string1 = []
    string2 = []
    sPath = input("Please Input the Path of File:")
    get_directory_contents(sPath, Queue, string1, string2)
    string2.sort()
    #print(string1)
    #print(string2)
    os.chdir('C://a')
    for i in range(0, len(string1)):
        postion = 0
        fristlen = 0
        string = ''
        with open(string1[i]) as fp:
            for line in fp.readlines():
                postion = postion + 1
                if postion == 2:
                    string = string + line[:-4]
                    string = string + string2[i] + '\n'
                    #fp.write(string)
                else:
                    string = string + line
            print(string)
        with open(string1[i], 'w') as fp:
            fp.write(string)
    #print("操作结束")
    #os.rename(string1[i],'0'+str(num)+'.png')    

