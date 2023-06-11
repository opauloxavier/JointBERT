def compare_file_lengths(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        for i in range(len(lines1)):
            line1 = lines1[i].strip()
            line2 = lines2[i].strip()
            print('Line1:', line1)
            print('Line2:', line2)
            assert len(line1) == len(line2)


# Usage example
file1 = './data/conda/CONDA_public_data/answer.txt'
file2 = './data/conda/answer.txt'
compare_file_lengths(file1, file2)
