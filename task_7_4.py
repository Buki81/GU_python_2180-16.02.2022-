import os


root = os.path.dirname(__file__)
f_path = os.path.join(root, 'some_data')
# {0: 1, 10: 0, 100: 0, 1000: 8, 10000: 81, 100000: 871, 1000000: 0}

keys = [0, 10, 100, 1000, 10000, 100000, 1000000]
dict_stat = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}
for root, dirs, files in os.walk(f_path):
    for file in files:
        f_size = os.stat(os.path.join(root, file)).st_size
        for i, key in enumerate(keys):
            if f_size <= keys[i]:
                dict_stat[keys[i]] += 1
                break
print(dict_stat)