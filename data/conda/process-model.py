import pandas as pd


TYPE = 'dev'

SOURCE = f'./{TYPE}/CONDA_valid_leaderboard.csv'
SAVE_PATH = f'./{TYPE}'

# import CONDA_train_leadebord.csv on dataframe
dataset = pd.read_csv(
    SOURCE, usecols=['tokenized', 'intentClass', 'slotClasses'], encoding="utf-8", encoding_errors='ignore')


# save tokenized column as txt, represents the seq_in file
seq_in = dataset['tokenized'].values
seq_in = [str(x) for x in seq_in]
seq_in = '\n'.join(seq_in)
with open(f'{SAVE_PATH}/seq.in', 'w') as f:
    f.write(seq_in)
    f.close()

# save intentClass column as txt, represents the label file
label = dataset['intentClass'].values
label = [str(x) for x in label]
label = '\n'.join(label)
with open(f'{SAVE_PATH}/label', 'w') as f:
    f.write(label)
    f.close()

# save seq_out column as txt, represents the seq_out file
seq_out = dataset['slotClasses'].values
seq_out = [str(x) for x in seq_out]
seq_out = '\n'.join(seq_out)
with open(f'{SAVE_PATH}/seq.out', 'w') as f:
    f.write(seq_out)
    f.close()
