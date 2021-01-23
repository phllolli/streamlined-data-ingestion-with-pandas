# Chapter 1: Importing Data from Flat Files

# Introduction to flat files

## Flat Files

- Simple, easy-to-produce format
- Data stored as plain text (no formatting)
- One row per line
- Values for different fields are separated by delimiter
- Most common flat file type: comma-separated values (CSV)

```python
import pandas as pd

df = pd.read_csv('data.csv', sep = ',')
# sep = delimiter/separator
```

# Modifying flat file imports

`DataFrame.shape` : (rows, columns)

## Limiting Columns

`usecols`

```python
col_name = ['col1', 'col2', 'col4']
col_index = [0, 1, 3]

df = pd.read_csv('data.csv', usecols=col_name)
# df = pd.read_csv('data.csv', usecols=col_num)
```

## Limiting Rows

`nrows`

```python
df = pd.read_csv('data.csv', nrows = 1000)
# first 1000 rows
```

`skiprows`

- Use `nrows` and `skiprows` together to process a file in chunks
- `skiprows` accepts a list of row numbers, a number of rows, or a function to filter rows
- Set `header=None` so `pandas` knows there are no column nams

```python
df = pd.read_csv('data.csv', 
                nrows = 500,
                skiprows = 1000,
                header = None)
# row 1000 to 1500
```

## Assigning Column Names

- Supply column names by passing a list to the `names` argument
- The list **MUST** have a name for every column in your data
- **If you only need to rename a few columns, do it after the import!**

```python
df = pd.read_csv('data.csv', 
                nrows = 500,
                skiprows = 1000,
                header = None,
                names = df_first1000rows)
```

# Handling errors and missing data

## Common Flat File Import Issues

- Column data types are wrong
- Missing values
- Records that `pandas` cannot read

## Specifying Data Types

- Use the `dtype` keyword argument to specify column data types
- `dtype` takes a dicitonary of column names and data types

```python
df = pd.read_csv('data.csv', dtype = {'col1': str})

# show the type of the columns
print(df.dtypes)
```

## Customizing Missing Data Values

- `pandas` automatically interprets some values as missing or NA
- Use the `na_values` keyword argument to set custom missing values
- Can pass a single value, list, or dictionary of columns and values

```python
df = pd.read_csv('data.csv',
                 na_values = {'col1': 0})
```

## Lines with Errors

- Set `error_bad_lines = False` to skip unparseable records
- Set `warn_bad_lines = True` to see messages when records are skipped

```python
df = pd.read_csv('data.csv',
                 error_bad_lines = False,
                 warn_bad_lines = True)
```