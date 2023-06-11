import re


def extract_content(input_string):
    pattern = r'(?:<|\[)(.*?)(?:>|])'
    matches = re.findall(pattern, input_string)
    matches = [item.split(':')[-1] for item in matches]
    return matches


# Input and output file paths
input_file_path = './answer'
output_file_path = 'answer.txt'

# Open input and output files
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Read input file line by line
    for line in input_file:
        # Apply extract_content function to each line
        content = extract_content(line)
        print(content)
        # Write the extracted content to the output file
        output_file.write(' '.join(content) + '\n')

print("Extraction completed. Results written to", output_file_path)
