import os

directory = r'C:\Users\OMEN\Desktop\wfh'

file_count = 0

file_names = []

if os.path.exists(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_count += 1
            file_names.append(filename)
else:
    print("Directory does not exist.")

print("Total files in directory:", file_count)


print("File names:")
for name in file_names:
    print(name)
