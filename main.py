import os
folders = ['for-update-csv', 'actual-csv', 'updated-csv']
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"[Csv Update Master] The {folder} folder for working with files was not found!\nFolder {folder} has been created successfully\n")
if not os.listdir('actual-csv'):
    print("[Csv Update Master] There are no files in the actual-csv folder. Please put the files in it\n")
elif not os.listdir('for-update-csv'):
    print("[Csv Update Master] There are no files in the for-update-csv folder. Please put the files in it\n")
else:
    from system.utils import updater