from zipfile import ZipFile 
import sys
file_name = sys.argv[1]
# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
    AllFiles = zip.namelist()
    zip.extractall()
    #print(AllFiles)   
    files = [open(name) for name in AllFiles]
    sets = [set(line.strip() for line in file) 
            for file in files]
    common = set.intersection(*sets)
    #print(common)
print("Please check the output file for the common")    
with open('output.txt', 'w') as file_out:
    for line in common:        
        print(line)
        file_out.write(line + '\n')
file_out.close()