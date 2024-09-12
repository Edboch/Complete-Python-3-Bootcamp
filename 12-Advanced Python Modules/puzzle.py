import shutil
import os
import regex
# print(os.getcwd())
# file = shutil.unpack_archive('C:/Udemy_Python/12-Advanced Python Modules/unzip_me_for_instructions.zip','C:/Udemy_Python/12-Advanced Python Modules/answer_unzip',format = 'zip')

numbers = []
phone_pattern = r'\d{3}-\d{3}-\d{4}'
test = regex.match(phone_pattern,'000-222-5523')
print(test)

for folder,subfolder,files in os.walk('C:/Udemy_Python/12-Advanced Python Modules/answer_unzip/extracted_content'):
    for file in files:
        with open(folder+'/'+file,'r') as f:
            text = f.read()
            phones = regex.findall(phone_pattern,text)
            if phones != []:
                numbers.extend(phones)

print(numbers)