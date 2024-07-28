import numpy as np
import pandas as pd

url = (
    "https://archive.ics.uci.edu/static/public/891/data.csv"
)


def download_data(x):
 """
 Reads in a single dataset from the CDC website as csv

 Return: DataFrame
 """
 if x == 1:
  return pd.read_csv(url)

 def write_data(data, directory, **kwargs):
  """
  Writes each raw data DataFrame to a file as a CSV

  Parameters
  ----------
  data : dictionary of DataFrames

  directory : string name of directory to save files i.e. "data/raw"

  kwargs : extra keyword arguments for the `to_csv` DataFrame method

  Returns
  -------X_test.to_csv('data/prepared/X_test_ScoreNewData.csv',index=False)
  None
  Note bashlash is a special character so will need to double the path string
  directory name, name of key.csv.  forwardign any keyword argument
  """
  for name, df in data.items():
   # df.to_csv(f'data/raw/{name}.csv')
   df.to_csv(f'{directory}/{name}.csv', **kwargs)

   def read_local_data(name, directory):
    """
    Read in one CSV as a DataFrame from the given directory

    Parameters
    ----------
    name : menhealth or menhealth or physical or dietary,heart,sex,edu,al

    directory : string name of directory to save files i.e. "data/raw"

    Returns
    -------
    DataFrame
    """
    return pd.read_csv(f"{directory}/{name}_data.csv")

   def run():
    """
    Run all cleaning and transformation steps

    Returns
    -------
    Dictionary of DataFrames
    """
    names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
    data = {}
    for i in names:
     data[f"{i}"] = read_local_data(i, 'data/raw')
    return data

   def select_columns(df):
    """
    Selects fewer columns
    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    df : DataFrame
    """
    sample_df = pd.DataFrame(df.sample(n=300), columns=df.columns)
    cols = df.columns

    # choose few columns

    labels = ['Diabetes_binary', 'Gender', 'Types', 'MentHlth', 'GeneralHealth', 'Type',
              'income', 'education', 'Sex', 'PhysHlth', 'PhysActivity', 'Fruits',
              'Veggies', 'HeartDiseaseorAttack']

    filt = cols.isin(labels)

    return sample_df.loc[:, filt]

   def run2():
    """
    Run all cleaning and transformation steps

    Returns
    -------
    Dictionary of DataFrames
    """
    names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
    data = {}
    for i in names:
     df = read_local_data(i, 'data/raw')
     df = select_columns(df)  # step 1:  select column in data cleaning
     data[f"{i}"] = df
    return data

   def update_labels(df):
    """
    Replace a few of the area names using the REPLACE_AREA dictionary.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    df : DataFrame
    """
    people = df
    people['Gender'] = np.where(people['Sex'] == 0, 'men', 'women')
    people['Type'] = np.where(people['Diabetes_binary'] == 0, 'nondiabetic', 'diabetic')
    definitions = pd.Series([0, "Excellent", "Very good", "Good", "Fair", "Poor", "UNKNOWN"], dtype="category")
    people['GeneralHealth'] = np.vectorize(reversefactor.get)(people[['GenHlth']])
    definitions = pd.Series([0, "<10K", "10-15K", "15-20K", "20-25K", "25K-35K", "35-50K", "50-75K", "75>"],
                            dtype="category")
    people['income'] = np.vectorize(reversefactor.get)(people[['Income']])
    definitions = pd.Series([0, "None", "1-8", "9-11", "12orGED", "C1-3", "C4+"], dtype="category")
    people['education'] = np.vectorize(reversefactor.get)(people[['Education']])

    return people

   def run3():
    """
    Run all cleaning and transformation steps

    Returns
    -------
    Dictionary of DataFrames
    """
    names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
    data = {}
    for i in names:
     df = read_local_data(i, 'data/raw')
     df = update_labels(df)
     df = select_columns(df)  # step 1:  select column in data cleaning

     data[f"{i}"] = df
    return data


def group_data(df, x, y):
 import pandas as pd

 # Assuming your DataFrame 'people' has columns 'GeneralHealth' and 'Type'

 # Filter data for relevant columns
 df = people[[x, y]]

 # Calculate counts using value_counts()
 counts = df[x].value_counts().to_frame(name="Count")

 # Calculate percentages (optional)
 # I want percentages:
 percentages = (counts["Count"] / len(df)) * 100
 counts["Percentage"] = percentages.apply("{:.1f}%".format)  # Format as percentages

 # Display the table
 return counts


def run4():
 """
 Run all cleaning and transformation steps

 Returns
 -------
 Dictionary of DataFrames
 """
 names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
 data = {}
 for i in names:
  df = read_local_data(i, 'data/raw')
  df = update_labels(df)  # step 1: update labels
  df = select_columns(df)  # step 2:  select column in data cleaning
  df = group_data(df, "GeneralHealth", "Type")  # step 4:
  data[f"{i}"] = df
 return data


def run5():
 """
 Run all cleaning and transformation steps

 Returns
 -------
 Dictionary of DataFrames
 """
 names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
 data = {}
 for i in names:
  df = read_local_data(i, 'data/raw')
  df = update_labels(df)  # step 1: update labels
  df = select_columns(df)  # step 2:  select column in data cleaning
  df = group_data(df, "income", "Type")  # step 3: group data
  data[f"{i}"] = df
 return data


def run6():
 """
 Run all cleaning and transformation steps

 Returns
 -------
 Dictionary of DataFrames
 """
 names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
 data = {}
 for i in names:
  df = read_local_data(i, 'data/raw')
  df = update_labels(df)  # step 1: update labels
  df = select_columns(df)  # step 2:  select column in data cleaning
  df = group_data(df, "education", "Type")  # step3: group data and count
  data[f"{i}"] = df
 return data
















