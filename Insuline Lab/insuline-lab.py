# write a function to count the number of characters in a file
def file_size(file_path):
    with open(file_path, 'r') as f:
        len = 0
        for x in f:
            for y in x:
                len = len + 1
    f.close()
    return len

# Confirm the main text file has 110 characters
size = file_size("new-file.txt")
print(f"preproinsuline length is {size}")

# write the characters of the main file in string variable
with open("new-file.txt", 'r') as file:
    text = ""
    for x in file:
        for y in x:
            text = text + y
file.close()

# write Insulin sequece from original file
with open("Insuline-seq-clean.txt", 'w') as insulin:
    insuline_seq = text[:24]
    insulin.write(insuline_seq)
insulin.close()

# check size of file containing insuline sequence
insulin_size = file_size("Insuline-seq-clean.txt")
print(f"length of insuline sequence is {insulin_size}")


# write binsuline sequence in a new file
new_file = open("binsuline-seq-clean.txt", 'w')
binsuline_seq = text[24:54]
new_file.write(binsuline_seq)
new_file.close()

# Confirm length of binsuline sequence is 30
print(f"length of binsuline sequence is {len(binsuline_seq)}")

# Create cinsuline sequence file
with open("cinsulin-seq-clean.txt", 'w') as f2:
    cinsulin_seq = text[54:89]
    f2.write(cinsulin_seq)
f2.close()

# Confirm length of cinsuline sequence file
cinsuline_len = file_size("cinsulin-seq-clean.txt")
print(f"length of cinsuline sequence is {cinsuline_len}")

# Create ainsuline sequence file
with open("ainsulin-seq-clean.txt", 'w') as f3:
    cinsulin_seq = text[89:]
    f3.write(cinsulin_seq)
f3.close()

# Confirm length of ainsuline sequence file
ainsuline_len = file_size("ainsulin-seq-clean.txt")
print(f"length of ainsuline sequence is {ainsuline_len}")
