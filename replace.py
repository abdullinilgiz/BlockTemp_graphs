
data = ""
with open('4.5_1.txt', 'r') as file:
    data = file.read().replace(',', '.')

with open("4.5_1_d.txt", "w") as out_file:
    out_file.write(data)