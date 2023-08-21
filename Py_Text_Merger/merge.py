def merge_text_files(input_files, output_file):
    with open(output_file, 'w') as out_file:
        for file_name in input_files:
            with open(file_name, 'r') as in_file:
                for line in in_file:
                    out_file.write(line)

# List of input text files to merge
input_files = ['a.txt', 'b.txt']

# Output file to store merged text
output_file = 'merged_output.txt'

merge_text_files(input_files, output_file)

print(f"Text files merged into {output_file}")
