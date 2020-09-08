def batch(files_to_remove, path):
    # define batch file name
    folderName = path.rsplit('\\', -1)
    moveFileName = 'r_drive/'
    for i in range(len(folderName)):
        if i > 2:
            moveFileName += folderName[i] + '_'
    moveFileName += '.txt'
    # open file and write to it, then close
    moveFile = open(moveFileName, 'w')
    for i in files_to_remove:
        fileAndPath = path + '\\' + i
        fileAndPath = '"' + fileAndPath + '"'
        newLoc = 'C:/Users/wdg1dcr/Desktop/dupBackup/movedFiles'
        moveFile.write('move ' + fileAndPath + '*.* ' + newLoc + '\n')
    moveFile.close()

def list(fileName, d):
    outputFile = open('r_drive/' + fileName + '_output.txt', 'w')
    for k, v in d.items():
        if len(v) == 2:
            outputFile.write(str(v[0]) + '\\' + str(k) + ';' + str(v[1]) + '\\' + str(k) + '\n')
    outputFile.close()

def batch2(file_name, files_to_move):
    import os
    os.chdir('H:/temp/data_cleanse_batch_files')
    moveFileName = file_name + '.txt'
    moveFile = open(moveFileName, 'w')
    for i in files_to_move:
        print(i)
        newLoc_path = i
        newLoc_path = newLoc_path[7:]
        newLoc_path = newLoc_path[:newLoc_path.rindex('\\')]
        newLoc_path = newLoc_path.replace(' ', '')
        newLoc_path = newLoc_path.replace(',', '')
        newLoc = 'C:\\Users\\wdg1dcr\\Desktop\\dupBackup\\movedFiles2\\' + newLoc_path
        moveFile.write(f'md {newLoc} 2> nul & move \"{i}\"*.* {newLoc}\n')
    moveFile.close()
    os.chdir('C:\\Users\\WDG1DCR\\Desktop\\my_projects\\data_analysis\\data_cleanse')