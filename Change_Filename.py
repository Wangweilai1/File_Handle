import os
def get_directory_contents(sPath):
    string = ''
    for sChlild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChlild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            string = file_change(sChildPath)
            string = string + '.txt'
            os.rename(sChildPath, string[2:])
            
def file_change(sChildPath):
    i = 0
    string0 = ''
    with open(sChildPath) as fp:
        for line in fp.readlines():
            i = i + 1
            if i == 2:
                string0 = hex(int(line[-4:-1], 16) + 0x30)
                return string0.upper()



if __name__ == "__main__":
    sPath = ''
    sPath = input("Please Input the Path of File:")
    os.chdir('C://a')
    get_directory_contents(sPath)
    print("操作结束")

            
    
