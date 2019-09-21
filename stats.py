import json
import os

if __name__ == '__main__':
    for filename in os.listdir('data'):
        with open(os.path.join('data', filename)) as f:
            data = json.load(f)
        print(f'{filename} : {len(data)}')
