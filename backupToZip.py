# Backing Up a Folder Into ZIP File

#! python3
#backup to zip.py - copies an entire folder and its contents into
#a ZIP file whose filename increments.

import zipfile, os
def backupToZip(folder):
    #Backup the entire contents of 'folder' into a ZIP file.

    folder = os.path.abspath(folder)  #make sure foledr is absolute

    #Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    #Create the ZIP file.
    print('Creating %s...' %(zipFilename))
    backupZip = zipfile.zipfile(zipFilename, 'w')

    #Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' %(foldername))
        #Add the current folder to the ZIP file.
        backupZip.write(foldername)
        #Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.base(folder) + '_'
            if filename.startswith(newBase) and filename.endwith('.zip'):
                continue   #do not backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')
    #backupToZip('C:'\\delicious)




































