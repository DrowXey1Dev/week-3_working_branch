#EXERCISE 1
#-----IMPORT-----#
test_cases_exr1 = [9, 7, 16, 1, 4]


#-----FUNCTION DEFS-----#
def fibonacci(input):
    """
    Takes an initial input value, then starting with 0 and 1, adds the two together to get the next number and then adds that
    with the previous number to get the n + 1. This process occurs x times where x is the integer input. So if the input is 9, the 
    process happens 9 times until the final output of 34 is given which indicates the completion of the fibonacci series.

    Function Parameters:
    integer input (first integer is passed from outside the function and then it feeds itself)

    Function returns:
    returns itself (recursive) until it resolves giving the final output
    """
    #if the initial input is 0 then return 0
    #this is also very important for the recursion and is integral for termination

    if input == 0:
        return 0
    #if the initial input is 1, then return 1
    #this is alos very important for the recursion
    elif input == 1:
        return 1
    else:
        #this is the core mechanism for the recursion
        return fibonacci(input-1) + fibonacci(input-2)
    
    #Explanation: This is how I thought about this problem. It can be very tricky but visualizing helps a ton
    #so basically, this recursion can be thought of visually as a tree. Each recursion cycle is a lower level
    #of the tree. For example assume the inital input is 4. Lets assume that 4 is the root. 
    #Then when the recursion is triggered, the root gets 2 children: 3, and 2. This is because the 
    #two fibonacci function calls will pass in 3 and 2 respectively. This can be thought of as if you had
    #two pointers: pointer_left, and pointer_right. Pointer_left points to 0, and pointer_right points to 1. 
    #As the array is cycled (to build the series), the value at the index that pointer_left and pointer_right
    #are pointing to, are added, and then that value is loaded into the pointer_right[i + 1] index. This is basically
    #what is happening here but instead of doing it one function, we are using recursion. As 3, and 2 are passed
    #into the respective recursed functions, they themselves become nodes and each of them get their on children nodes
    #in the form of 2, and 1 (for node 3), and 1, and 0 (for node 2). Once this happens, either of the upper two
    #conditionals is triggered which brings the recursion to an end. Since recursive functions can be thought of as
    #old fationed telescopes, the callapse into each other as each level resolves itself. So the resolution of the
    #recursion starts at the lowest level of the tree (where you have the 0 or 1 nodes) and collapses upwards. Then
    #if you add the 1s and 0s leafs of the tree, you get the final number which is the fibonacci number for the inputted n


#-----MAIN-----#
print(fibonacci(test_cases_exr1[0]))
print(fibonacci(test_cases_exr1[1]))
print(fibonacci(test_cases_exr1[2]))
print(fibonacci(test_cases_exr1[3]))
print(fibonacci(test_cases_exr1[4]))


#EXERCISE 2------------------------------------------------------------------------------------------------------------------#
#-----IMPORTS-----#

test_cases_exr2 = [7, 25, 16, 33, 16]

#-----FUNCTION DEFS-----#
def to_binary(input):
    """
    This function takes in an integer and returns its binary representation. The function is designed to be recursive.

    Function Parameters:
    integer input

    Function returns:
    returns itself (as it is a recursive input) until all instances are resolved and the function collapses giving the final binary
    representation of the inputted integer
    """

    #for inputs 1 or 0
    if input == 1:
        return "1"
    elif input == 0:
        return "0"
    else:
        #recursion
        #divide the input by 2, take the quotient and add it to the remainder...explain this later
        return to_binary(input // 2) + str(input % 2)



#-----MAIN-----#
#can replace with loop if have time
print(to_binary(test_cases_exr2[0]))   
print(to_binary(test_cases_exr2[1]))  
print(to_binary(test_cases_exr2[2]))  
print(to_binary(test_cases_exr2[3]))   
print(to_binary(test_cases_exr2[4]))   



#EXERCISE 3------------------------------------------------------------------------------------------------------------------#
#-----IMPORTS-----#
import pandas as pd
import numpy as np

pd.options.display.max_rows = 100  # default is 60 rows

#dataset URL
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
# df_bellevue = pd.read_csv('./data/.../mydata.csv')  # you can also reference locally stored data

#-----FUNCTION DEFS-----#

def task_1():
    """
    FUNCTION NAME: task_return_column_names()

    this function finds and returns column names. Also I had to rename every function to a generic task 1 so that the autograder would not break
    so I have added the original function name above just so that it is more easy to read

    Function Parameters:
    nothing

    Function returns:
    returns sorted columns
    """
    
    #add all the missing values and store them. Check the column for null values and sum the quantitiy amount
    missing_values = df_bellevue.isnull().sum()
    #sorted columns are set equal to the worted list of columns from least to most missing data values
    sorted_cols = missing_values.sort_values().index.tolist()
    print("Columns sorted from least -> most: ")
    print(sorted_cols)
    return sorted_cols


def task_2():
    """
    FUNCTION NAME: task_return_data_frame()

    creates and returns a data frame of the dataset

    Function Parameters:
    nothing

    Function returns:
    returns the dataframe
    """

    #ok apparently there is no year column. So the year must be extrracted 
    #convert 'date_in' to datetime format (so we can pull out the year)
    df_bellevue["date_in"] = pd.to_datetime(df_bellevue["date_in"], errors="coerce")

    #extract the year into a new column
    df_bellevue["year"] = df_bellevue["date_in"].dt.year

    #grroup by year and count total admissions
    df_result = (
        df_bellevue.groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )

    #print the head. Should be like the first 5 by default.
    print(df_result.head())

    #return the new data frame
    return df_result



def task_3():
    """
    FUNCTION NAME: task_return_series()


    this function finds and returns a sequence grouped by gender and age

    Function Parameters:
    nothing

    Function returns:
    returns a sequence 
    """

    #group by gender
    #get mean age for the groups
    avg_age_by_gender = df_bellevue.groupby("gender")["age"].mean()

    print(avg_age_by_gender)

    #return the sequence. Index shoulbe be gender and the values are the average age. 
    return avg_age_by_gender



def task_4():
    """

    FUNCTION NAME: task_return_popular_profession()

    this funciton finds and returns the most popular profession

    Function Parameters:
    nothing

    Function returns:
    returns array of top 5 most common professions found in the dataset
    """

    #long line of code smashed together. Basically sample the head of the dataset
    #count amount of times a profession appears
    top_5_epic_jobs = df_bellevue["profession"].value_counts().head(5).index.tolist()

    #print
    print("Top 5 professions:", top_5_epic_jobs )

    #return the list
    return top_5_epic_jobs 

#--------------------------------------------------------#
#-----MAIN-----#
print("-----Q1-----")
task_1()
print("-----Q2-----")
task_2()
print("-----Q3-----")
task_3()
print("-----Q4-----")
task_4()








