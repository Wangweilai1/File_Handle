#根据文件内容命名文件
import os
def file_change(sChildPath, string2):
    with open(sChildPath) as fp:
        string2.append(fp.read())  
                
def get_directory_contents(sPath, string2):
    for sChlild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChlild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            file_change(sChildPath, string2)



if __name__ == "__main__":
    sPath = ''
    string1 = []
    string2 = []
    sPath = input("Please Input the Path of File:")
    get_directory_contents(sPath, string2)
    string2.sort()
    i = 0
    postion = 0
    for i in range(0, len(string2)):
        postion = hex(i)[2:]
        string1 = 'c://a/PG_' + str(postion.upper()) + '.txt'
        print(string1)
        with open(string1, 'w+') as fp:
            i = i + 1
            fp.write(string2[i - 1])
