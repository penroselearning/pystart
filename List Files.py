import os
basedir = os.path.abspath(os.path.dirname(__file__))

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(basedir):
    for file in f:
      if file.find('.py') >= 0:
        files.append(os.path.join(r, file))

print(f'{len(files)} .py files Found! in the directory : {basedir}')
for f in files:
    print(f)