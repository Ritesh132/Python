import os
import re
import shutil

os.chdir(r'C:\delicious\walnut\waffles')
path = os.getcwd()


prefix_regex = re.compile(r'(a)(\d{,3})')

i = 1
for file in os.listdir():
    mo = prefix_regex.search(file)
    if mo:
        old_name = os.path.abspath(file)
        new_suffix = mo.group(1) + str(i).zfill(3) + '.jpg'
        new_name = os.path.join(path, new_suffix)
        i += 1
        print('Renaming: %s to %s' % (old_name, new_name))
        shutil.move(old_name, new_name)