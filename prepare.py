import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
#import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler

url = (
    "https://archive.ics.uci.edu/static/public/891/data.csv"
)


class PrepareData:
    """
    Downloads the data from cdc repository and applies several
    successive transformations to prepare it for modeling. The `run`
    method calls all the steps
    """

    def __init__(self, download_new=True):
        """
        Parameters
        ----------
        download_new : bool, determines whether new data will be downloaded
        or whether local saved data will be used
        """
        self.download_new = download_new

    def download_data(self, x):
        """
        Reads in a single dataset from the CDC website as csv

        Return: DataFrame
        """
        if x == 1:
            return pd.read_csv(url)

    def write_data(self, data, directory, **kwargs):
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

    def read_local_data(self, name, directory):
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

    def run(self):
        """
          Run all cleaning and transformation steps

          Returns
          -------
          Dictionary of DataFrames
          """

        names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
        data = {}

        for i in names:
            if self.download_new:
                data[f"{i}"] = self.download_data(1)
            else:
                data[f"{i}"] = self.read_local_data(i, 'data/raw')

        return data

    def select_columns(self, df):
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

    def run2(self):
        """
          Run all cleaning and transformation steps

          Returns
          -------
          Dictionary of DataFrames
          """
        names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
        data = {}
        for i in names:

            if self.download_new:
                data[f"{i}"] = self.download_data(1)
            else:
                data[f"{i}"] = self.read_local_data(i, 'data/raw')

            df = self.select_columns(df)  # step 1:  select column in data cleaning
            data[f"{i}"] = df
        return data

    def update_labels(self, df):
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

    def run3(self):
        """
          Run all cleaning and transformation steps

          Returns
          -------
          Dictionary of DataFrames
          """
        names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
        data = {}
        for i in names:
            if self.download_new:
                data[f"{i}"] = self.download_data(1)
            else:
                data[f"{i}"] = self.read_local_data(i, 'data/raw')
            df = self.update_labels(df)
            df = self.select_columns(df)  # step 1:  select column in data cleaning
            data[f"{i}"] = df
        return data

    def group_data(self, df, x, y):
        """
       Run all cleaning and transformation steps

       Returns
       -------
       counts and percentages of x,y in a DataFrames
       """

        # Assuming your DataFrame 'people' has columns 'GeneralHealth' and 'Type'

        # Filter data for relevant columns
        df = df[[x, y]]

        # Calculate counts using value_counts()
        counts = df[x].value_counts().to_frame(name="Count")

        # Calculate percentages (optional)
        # I want percentages:
        percentages = (counts["Count"] / len(df)) * 100
        counts["Percentage"] = percentages.apply("{:.1f}%".format)  # Format as percentages

        # Display the table
        return counts

    def run4(self):
        """
       Run all cleaning and transformation steps

       Returns
       -------
       Dictionary of DataFrames
       """
        names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
        data = {}
        for i in names:
            if self.download_new:
                data[f"{i}"] = self.download_data(1)
            else:
                data[f"{i}"] = self.read_local_data(i, 'data/raw')

            df = self.update_labels(df)  # step 1: update labels
            df = self.select_columns(df)  # step 2:  select column in data cleaning
            df = self.group_data(df, "GeneralHealth", "Type")  # step 4:
            data[f"{i}"] = df
        return data

    def run5(self):
        """
       Run all cleaning and transformation steps

       Returns
       -------
       Dictionary of DataFrames
       """
        names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
        data = {}
        for i in names:
            if self.download_new:
                data[f"{i}"] = self.download_data(1)
            else:
                data[f"{i}"] = self.read_local_data(i, 'data/raw')
            df = self.update_labels(df)  # step 1: update labels
            df = self.select_columns(df)  # step 2:  select column in data cleaning
            df = self.group_data(df, "income", "Type")  # step 3: group data
            data[f"{i}"] = df
        return data

    def run6(self):
        """
       Run all cleaning and transformation steps

       Returns
       -------
       Dictionary of DataFrames
       """
        names = ['menhealth', 'menhealth', 'physical', 'dietary', 'heart', 'sex', 'edu', 'all']
        data = {}
        for i in names:
            if self.download_new:
                data[f"{i}"] = self.download_data(1)
            else:
                data[f"{i}"] = self.read_local_data(i, 'data/raw')
            df = self.update_labels(df)  # step 1: update labels
            df = self.select_columns(df)  # step 2:  select column in data cleaning
            df = self.group_data(df, "education", "Type")  # step3: group data and count
            data[f"{i}"] = df
        return data

    def make_prediction(self, user_input):
        """
       Run all cleaning and transformation steps
       input X = df[['Income','GenHlth','MentHlth','PhysHlth','DiffWalk']]

       Returns
       -------
       Dictionary of DataFrames
       """
        cols = ['Income', 'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk']
        df = self.read_local_data('all', 'data/raw')
        y = df['Diabetes_binary']
        X = df[cols]
        scaler = StandardScaler()
        scaler.fit(X)
        X_scaled = scaler.transform(X)

        rfc = RandomForestClassifier(random_state=1234)
        rfc.fit(X_scaled, y)
        data = user_input
        reshaped_data = np.array(data).reshape(1, 5)
        prediction = rfc.predict(reshaped_data)

        if prediction[0] == 0:
            probability_pred = rfc.predict_proba(reshaped_data)[:, 0]
            result = probability_pred[0] * 100
            prt = f"You have a {result:.0f}% probability you will not be diagnosed with diabetes."
        else:
            probability_pred = rfc.predict_proba(reshaped_data)[:, 0]
            result = probability_pred[0] * 100
            prt = f"You have a {result:.0f}% probability you will be diagnosed with diabetes."

        return prt

    def graph_df(self, df, x, y):
        """
       input:dataframe, x, y
       Returns
       -------
       graph
       """

        df = df[[x, y]]
        t = f'{x} vs {y}'
        # Calculate counts and percentages
        counts = df[[x, y]].value_counts()
        percentages = (counts / len(df)) * 100
        # Create the bar chart
        plt.figure(figsize=(20, 6))
        ax = counts.plot(kind='bar')

        # Add percentage labels
        for i, v in enumerate(counts):
            ax.text(i, v + 0.1, f'{v} ({percentages[i]:.1f}%)', ha='center', va='bottom')

        plt.ylabel('Count')
        plt.xticks(fontsize=12)
        plt.title(t)
        plt.show()
        return plt
