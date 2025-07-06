import sys
sys.path.append('c:/source-code/hello-world/python-gha-demo/py_scripts')

# Import the module directly from the appended path
import math_ops

result = math_ops.square_number(5)
print(f"The square of 5 is: {result}")
