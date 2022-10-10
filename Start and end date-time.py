import pandas as pd
def transpose_format():
    df = pd.read_csv("Start and end date-time.csv")
    df.set_index("Line Item",inplace=True)
    df = df.T
    df.index = pd.PeriodIndex(df.index, freq="Q-DEC")
    df["Start Date"] = df.index.start_time
    df["End Date"] = df.index.end_time
    print(df)
transpose_format()