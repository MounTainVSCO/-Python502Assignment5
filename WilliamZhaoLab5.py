
# Student Name: William Zhao
# Course: CIS 502 Applied Python Programming
# Lab # 5 - Functions, Passing Multiple Arguments
# Application: Frequency Distribution 
# Description: The program takes in a range of numbers
#              and creates a frequency distribution table
#              based on the list of values
# Version: Python 3.11
# Solution File: WilliamZhaoLab5.py
# Date: 03/03/23
##

from prettytable import PrettyTable

MIN_RANGE = 0
MAX_RANGE = 9

def validate_data(data_list):
    """
    Reads all the values in a given list and checks
    if they are integers in the given range 0-9 
    """
    try:
        for i in data_list:
            if i not in range(MIN_RANGE, MAX_RANGE+1):
                print("Invalid Input, not integer in [0, 9]")
                return []
    except:
        print("Please enter a valid integer list")
        return []
    
    return data_list

def freq_table(data_values):
    """
    Takes in a integer list of values and
    returns a dictionary with the frequency of 
    appearance for each value
    """
    data_values = validate_data(data_values)
    frequency_distribution = {}
    for i in data_values:
        if i not in frequency_distribution:
            frequency_distribution[i] = 1
        else:
            frequency_distribution[i] += 1

    return dict(sorted(frequency_distribution.items()))

def viz_table(dic_table):
    table = PrettyTable()
    table.field_names = ["Value", "Frequency"]

    for k, v in dic_table.items():
        table.add_row([k, v])
    
    return str(table)

if __name__ == "__main__":
    test_list = [3,1,1,5,3,1,2,2,3,5,3,5,4,4,6,7,6,7,5,7,8,3,8,2,3,4,1,5,6,7,99]
    big_data_inp = [3, 5, 2, 1, 7, 4, 0, 9, 3, 8, 6, 1, 2, 4, 0, 7, 8, 5, 6, 9]
    freq_dictionary = freq_table(test_list)
    print(viz_table(freq_dictionary))

    """
    Input: 3,1,1,5,3,1,2,2,3,5,3,5,4,4,6,7,6,7,5,7,8,3,8,2,3,4,1,5,6,7]
    +-------+-----------+
    | Value | Frequency |
    +-------+-----------+
    |   1   |     4     |
    |   2   |     3     |
    |   3   |     6     |
    |   4   |     3     |
    |   5   |     5     |
    |   6   |     3     |
    |   7   |     4     |
    |   8   |     2     |
    +-------+-----------+
    """

    """
    Input of big data topic:  [3, 5, 2, 1, 7, 4, 0, 9, 3, 8, 6, 
                            1, 2, 4, 0, 7, 8, 5, 6, 9]
    +-------+-----------+
    | Value | Frequency |
    +-------+-----------+
    |   0   |     2     |
    |   1   |     2     |
    |   2   |     2     |
    |   3   |     2     |
    |   4   |     2     |
    |   5   |     2     |
    |   6   |     2     |
    |   7   |     2     |
    |   8   |     2     |
    |   9   |     2     |
    +-------+-----------+
    """