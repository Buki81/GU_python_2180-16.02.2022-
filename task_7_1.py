import os


dir_name = 'my_project'
dir_tree = ('settings', 'mainapp', 'adminapp', 'authapp')
for dt in dir_tree:
    dir_path = os.path.join(dir_name, dt)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)