import pandas as pd
from ydata_profiling import ProfileReport
df = pd.read_csv("/Users/admin/PycharmProjects/nov_automation_2025/day2_07112025/Titanic-Dataset.csv")
profile = ProfileReport(df, title="Data Profiling Report")
profile.to_file("report.html")

