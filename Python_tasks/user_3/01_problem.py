print("=========================================================")
file1 = open("D:/Working_dir/Programming/Outside/Non-brack_01/input_file_1.txt", "r")
input_1 = file1.read()
print("Input from file 1:")
print(input_1)
input_1 = input_1.split('\n')

file2 = open("D:/Working_dir/Programming/Outside/Non-brack_01/input_file_2.txt", "r")
input_2 = file2.read()
print("\nInput from file 2:")
print(input_2)
input_2 = input_2.split('\n')

l = len(input_1)
final_text = ''

for x in range(l):
	final_text += f"{input_1[x]} {input_2[x]}\n"

file3 = open("D:/Working_dir/Programming/Outside/Non-brack_01/input_file_3.txt", "w")
file3.write(final_text)

print("Output in 3rd FIle:")
print(final_text)
print("=========================================================")
