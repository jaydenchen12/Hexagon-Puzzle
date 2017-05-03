import os

operatingSystem = os.name

windowsPath = "E:\Python27\python.exe"
macPath = 'python /user/local/finalproject/'

if operatingSystem == 'nt':
   path = windowsPath
else:
    path = macPath

print path
#os.system(path+" PicturePuzzle.py")

execfile("HexagonV2.py")
execfile("HexagonV2.py")


'''

    macPath = 'python /user/local/finalproject/'


    if Operatingsystem == 'windows':
        path = windowsPath
    elif Operatingsystem == 'mac':
        path = macPath
'''