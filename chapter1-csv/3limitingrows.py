df_first1000rows = pd.read_csv('data.csv', nrows = 1000)

################################################################

df = pd.read_csv('data.csv', 
                nrows = 500,
                skiprows = 1000,
                header = None)

################################################################

df = pd.read_csv('data.csv', 
                nrows = 500,
                skiprows = 1000,
                header = None,
                names = df_first1000rows)
