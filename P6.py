# importing required modules 
from zipfile import ZipFile 
  
# specifying the zip file name 
file_name = "namelists.zip"
  
# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    print('Extracting files now...') 
    zip.extractall() 
    print('Done!') 

with open('1.txt', 'r') as file1:
    with open('2.txt', 'r') as file2:
        with open('3.txt', 'r') as file3:
            same = set(file1).intersection(file2).intersection(file3)

same.discard('\n')

with open('some_output_file.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)