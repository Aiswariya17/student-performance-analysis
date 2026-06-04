import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_excel(r"C:\Users\acer\OneDrive\Documents\student data.csv.xlsx")

# Average Marks
df["Average_Marks"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
) / 3

print("First 5 Records")
print(df.head())

print("\nSubject Wise Average")
print(df[["Maths","Science","English"]].mean())
print()

#pass or fail
df["Result"]=df["Average_Marks"].apply(lambda x: "pass" if x>= 70 else "Fail")
print(df["Result"].value_counts())
print()

#fail students
fail_students=df[df["Result"]=="Fail"]
print("Fail Students:")
print(fail_students[["Name", "Average_Marks"]])

# Bar Chart
df[["Maths","Science","English"]].mean().plot(kind="bar")
plt.title("Subject Wise Average Marks")
plt.show()

# Attendance vs Marks
sns.scatterplot(
    x="Attendance",
    y="Average_Marks",
    data=df
)
plt.title("Attendance vs Average Marks")
plt.show()
# Study Hours vs Marks
sns.scatterplot(
    x="Study_Hours",
    y="Average_Marks",
    data=df
)
plt.title("Study Hours vs Average Marks")
plt.show()

# Performance Category
df["Category"] = pd.cut(
    df["Average_Marks"],
    bins=[0,50,75,100],
    labels=["Poor","Average","Excellent"]
)

df["Category"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Performance Category")
plt.show()

# Top Students
print("\nTop 10 Students")
print(
    df.sort_values(
        by="Average_Marks",
        ascending=False
    ).head(10)
)






