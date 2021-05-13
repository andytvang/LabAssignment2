"""
start
get the number of sheets
sheets / 5
round answer to next number
output the result to the user 
end
"""
import math

#input: sheet
def calculate(sheet):
    answer = sheet / 5
    rounded = math.cell(answer)
    print("sheet is : ", sheet)
    print("The answer is : ", answer)
    print("rounded is: ", rounded)
    print("=================================")
    return rounded
    #output: number of stamps needed

output = calculate(16)

print("Number of stamps needed is : ", output)