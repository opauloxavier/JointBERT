import pandas as pd


TYPE = 'test'

SOURCE = f'./{TYPE}/CONDA_{TYPE}_leaderboard.csv'
SAVE_PATH = f'./{TYPE}'

# import CONDA_train_leadebord.csv on dataframe
dataset = pd.read_csv(
    SOURCE, usecols=['tokenized'])

# save utterance column as txt, represents the seq_in file
seq_in = dataset['tokenized'].values
seq_in = [str(x) for x in seq_in]
seq_in = '\n'.join(seq_in)
with open(f'{SAVE_PATH}/seq.in', 'w') as f:
    f.write(seq_in)
    f.close()
