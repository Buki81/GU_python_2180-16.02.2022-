import os


root = os.path.dirname(__file__)
f_path = os.path.join(root, 'some_data')

keys = [0, 10, 100, 1000, 10000, 100000, 1000000]
dict_stat = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}