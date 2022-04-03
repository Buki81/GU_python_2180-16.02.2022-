import os


with open('config.yaml') as f:
    for row in f:
        dir_name = row.split(':')[0]
        dir_path = os.path.join(dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for file in row.split(':')[-1].split('\n')[0].split(', '):
            # print(file)
            with open(os.path.join(dir_path, file), 'x', encoding='UTF-8'):
                pass