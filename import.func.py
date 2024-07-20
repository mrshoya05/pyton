
#importing in python is a process of loading code from pythomn modules in to the  current script 

import math

result = math.sqrt(9)
print(result)


# to install just  single or limited functions we  import functionns  with specific  names:
from math import sqrt, pi
result = sqrt(9)*pi
print(result)

# improt as another name

from math import sqrt as s
mono = s(49)
print(mono)