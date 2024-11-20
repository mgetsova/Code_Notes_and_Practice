import pandas as pd 

# FROM LEETCODE INTRO TO PANDAS 15

'''
Get the size of a pandas df
'''
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows, columns = players.shape
    return [rows, columns]

'''
Display the first 3 rows
'''
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return(employees.head(3))

'''
Select the name and age of the student with student_id = 101
'''
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]

'''
Create a new column 'bonus' that is double the existing column 'salary'
'''
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"]*2
    return  employees


'''
Drop rows with duplicate email
'''
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])

'''
Drop missing name rows
'''
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'], inplace=True)
    return students

'''
Rename (all) columns in order
'''
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.columns = ['student_id', 'first_name', 'last_name', 'age_in_years']
    return students

'''
Change datatype of grade column
'''
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

'''
Fill in missing data in quantitiy column
'''
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products

'''
concatenate two dataframes with same columns into one (ie. concatinate them vertically)
'''
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis = 0)

'''
Given a df with columns ['city', 'month', 'temperature']
Pivot the data so that row = temps for a specific month and each city is a separate column
'''
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    res = weather.pivot(index='month', columns='city', values='temperature')
    return res

'''
Given a df with columns ['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4']
reshape it so that each row represents sales data for a product in a specific quarter 
(currently it is sales data for a product in each quarter)
'''
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # id_vars = ['product'] keeps the product column in tact
    # value_vars = [...] means we are taking the data from these columns and 
    #       reshaping it into two new columns 
    # var_name='quarter' creates a new column named quarter and each entry is the 
    #       column from which the sales data for the sales column in the new df was
    #       taken from in the old df
    # value_name='sales' creates a new column which will store the actual sales values
    #       (previously stored in q1, q2, q3, q4 columns)
    report = report.melt(id_vars = ['product'], 
    value_vars = ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], 
    var_name = 'quarter', value_name='sales')
    return report

'''
select the names of animals with weight oer 100 lbs, sorted in decreasing order
'''
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    heavy_animals = animals[animals['weight'] > 100]
    sorted_heavy_animals = heavy_animals.sort_values(by ='weight', ascending=False)
    return sorted_heavy_animals[['name']] # double brackets ensure result 
                                          # is a df and not a series