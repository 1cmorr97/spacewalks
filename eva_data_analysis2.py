import matplotlib.pyplot as plt
import pandas as pd

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
# set filepaths
input_file = open("./eva-data.json", "r", encoding="ascii")
output_file = open("./eva-data.csv", "w", encoding="utf-8")
graph_file = "./cumulative_eva_graph.png"

# read in data
eva_df = pd.read_json(input_file, convert_dates=["date"], encoding="ascii")
eva_df["eva"] = eva_df["eva"].astype(float)
eva_df.dropna(axis=0, subset=["duration", "date"], inplace=True)

# set up output file
eva_df.to_csv(output_file, index=False, encoding="utf-8")

# process data
eva_df.sort_values("date", inplace=True)
eva_df["duration_hours"] = (
    eva_df["duration"].str.split(":").apply(lambda x: int(x[0]) + int(x[1]) / 60)
)
eva_df["cumulative_time"] = eva_df["duration_hours"].cumsum()

# plotting
plt.plot(eva_df["date"], eva_df["cumulative_time"], "ko-")
plt.xlabel("Year")
plt.ylabel("Total time spent in space to date (hours)")
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
