""""
Calculadora infix

funcionamto:
[operação] [n1] [n2]

operações:
sum -> =
sub -> -
mul -> *
div -> /

"""

import sys
import os
from datetime import datetime

arguments = sys.argv[1:]

# TODO: Exception

if not arguments:
    operation = input("operação: ")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]

elif len(arguments) != 3:
    print("numero de argumentos invalidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation , * nums = arguments


valid_oprations = ("sum","sub","mul" ,"div")
if operation not in valid_oprations:
    print("operação invalida")
    print(valid_oprations)
    sys.exit(1)


validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"numero invalido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)


n1,n2 = validated_nums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER" , "")

with open(filepath, "a") as file_:
    file_.write(f"\n{timestamp} - {user} - {operation},{n1},{n2} = {result}")

print(f"o resultado é {result}")



