import pandas as pd

math_scores = pd.Series([78, 65, 89, 86, 55, 91],index=['Mary', 'John', 'Lisa', 'Adam', 'Anne', 'Bart'])

print(math_scores)

data = {
    "Matematyka":[4,5,6,7,8,9],
    "Fizyka":[10,11,12,13,14,15],
    "Chemia":[16,17,18,19,20,21],
    "Biologia":[22,23,24,25,26,27],
    "Geografia":[28,29,30,31,32,33],
    "Historia":[34,35,36,37,38,39]
}

students = ['Mary', 'John', 'Lisa', 'Adam', 'Anne', 'Bart']
grades_df = pd.DataFrame(data, index=students)
print(grades_df)

#opercje we/wy w pandas
#CSV
grades_df.to_csv("grades.csv",index=True)

grades_df2 = pd.read_csv("grades.csv")
print(grades_df2)

#JSON
grades_df.to_json("grades.json",orient="records",indent=2)

#XML
grades_df.to_xml("grades.xml",index=False)

#HTML
grades_df.to_html("grades.html",index=False)
