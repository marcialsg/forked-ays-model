# take every .py file in the current directory and convert it to a .txt file
# use the same name but add '_TXT' in the end.
# save it as a .txt file

import os

for file in os.listdir("."):
    if file.endswith(".py"):
        with open(file, "r") as f:
            lines = f.readlines()
        with open(file[:-3] + "_TXT.txt", "w") as f:
            f.writelines(lines)