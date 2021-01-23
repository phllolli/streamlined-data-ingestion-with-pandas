col_name = ['col1', 'col2', 'col4']
col_index = [0, 1, 3]

df = pd.read_csv('data.csv', usecols=col_name)
# df = pd.read_csv('data.csv', usecols=col_num)