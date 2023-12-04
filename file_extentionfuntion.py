file_name = input("enter the file name: ")
def extention(f):
    file_extention = file_name.split('.')[1]
    return file_extention
extention = extention(file_name)
print(f"the extention of thefile is: '{extention}'")
