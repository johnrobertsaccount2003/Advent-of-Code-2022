import os
import sys

os.system("git add --all")


os.system("git commit -m " + sys.argv[0])

os.system("git push origin main")
