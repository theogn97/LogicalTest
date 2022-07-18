output_str = ""

for i in range(1, 51):
    if i != 1:
        output_str += ","

    if i % 15 == 0:
        output_str += "Frontend Backend"
    elif i % 5 == 0:
        output_str += "Backend"
    elif i % 3 == 0:
        output_str += "Frontend"
    else:
        output_str += str(i)

print(output_str)
