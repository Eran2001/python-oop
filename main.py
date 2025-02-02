import re

txt = "EraN"

validation = re.search("^E.*N$", txt)

if validation:
  print("Yes")
else:
  print("No")
  