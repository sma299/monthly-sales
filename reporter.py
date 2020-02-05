# reporter.py

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("READING GRADEBOOK CSV FILE...")

#creating a filepath!
import pandas


#if CSV file in same directory as this Python script:
csv_filepath = "data/gradebook.csv"

#csv_filepath = os.path.join(os.path.dirname(_file_), "data", "monthly_sales.csv")


#csv_filepath = "/path/to/jeter_stats.csv"
grades = pandas.read_csv(csv_filepath)
print("GRADES:", type(grades))

print(grades.head())

grades_col = grades["final_grades"]
print("GRADES COLUMN", type(grades_col))

avg_grade = grades_col.mean()
print("AVG GRADE:", avg_grade)

or index, row in grades.iterrows():
    print(index)
    print(row["final_grade"])
    prin("---")