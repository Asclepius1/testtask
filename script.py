import os
import pandas

def get_file_name(file): 
       
    if '.' in file:
        if '.' != file[0]:
            return ((file)[:len(file)-3]).rstrip('.')
            
        else: return file
        
    else: return file
    

def get_dir_name(path):
    
    dir_name = os.path.split(path)
    return dir_name[1]

def get_file_type(file, path):

    dot=file.rfind(".")
    if '.' in file:
        if '.' != file[0]:
            return file[dot+1:]
            
        else: return "file"
        
    elif os.path.isdir(path+'/'+file):
        return "dir"
        
    else: return "file"
        
        
def next_path_dir(path):
    
    path = path.replace("\'" , "/")
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            return path +'/'+ i
        
    return False
        
all_res_fn=[]
all_res_id=[]
all_res_dn=[]
all_res_ft=[]

temp_path = "" #--------------------------path main directory-------------------------
path_to_xl = ""#--------------------------path your excel-------------------------

while True:
    id = 0
    file_conten = os.listdir(temp_path)
    for conten in file_conten:
        id+=1
        all_res_id.append(id)
        all_res_dn.append(get_dir_name(temp_path))
        all_res_fn.append(get_file_name(conten))
        all_res_ft.append(get_file_type(conten,temp_path))
    if next_path_dir(temp_path) == False:
        break
    else:
        if next_path_dir(temp_path) == []:
            continue
        temp_path = next_path_dir(temp_path)    

df = pandas.DataFrame({
    
    'Номер строки':all_res_id,
    'Папка в которой лежит файл':all_res_dn,
    'название файла':all_res_fn,
    'расширение файла':all_res_ft
})

df.to_excel(excel_writer=path_to_xl, index=False)