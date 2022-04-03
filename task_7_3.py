import os
import shutil


root_dir = 'my_project'
dir_name = 'my_project/templates'

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for dir in dirs:
            purpose_dir = os.path.join(dir_name, dir)
            if not os.path.exists(purpose_dir):
                shutil.copytree(root, purpose_dir)

'''Не смог разобраться, почему в целевом каталоге получаются сдвоенные папки в данном коде.'''