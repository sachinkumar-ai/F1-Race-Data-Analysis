import pandas as pd
import matplotlib.pyplot as plt

# Excel file read karna
df = pd.read_excel("f1_race_data.xlsx", engine="openpyxl")

# -------------------------------
# 1. Driver-wise total points
# -------------------------------
driver_points = df.groupby("Driver")["Points"].sum().sort_values(ascending=False)

print("\nDriver Championship Ranking:")
print(driver_points)

# Driver graph
plt.figure(figsize=(12, 6))
driver_points.plot(kind="bar")

plt.title("F1 Driver Championship Points")
plt.xlabel("Driver")
plt.ylabel("Total Points")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("driver_points.png", dpi=300, bbox_inches="tight")

plt.show()


# -------------------------------
# 2. Team-wise total points
# -------------------------------
team_points = df.groupby("Team")["Points"].sum().sort_values(ascending=False)

print("\nF1 Team Championship Points:")
print(team_points)

# Team graph
plt.figure(figsize=(12, 6))
team_points.plot(kind="bar")

plt.title("F1 Team Performance Analysis")
plt.xlabel("Team")
plt.ylabel("Total Points")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("team_points.png", dpi=300, bbox_inches="tight")

plt.show()

# -------------------------------
# 3. Top 5 Drivers
# -------------------------------

top_5_drivers = driver_points.head(5)

print("\nTop 5 Drivers:")
print(top_5_drivers)

# Top 5 Drivers graph
plt.figure(figsize=(10, 6))

top_5_drivers.plot(kind="bar")

plt.title("Top 5 F1 Drivers by Total Points")
plt.xlabel("Driver")
plt.ylabel("Total Points")
plt.xticks(rotation=30, ha="right")

plt.tight_layout()

# Save graph
plt.savefig("top_5_drivers.png", dpi=300, bbox_inches="tight")

plt.show()

# -------------------------------
# 5. F1 Performance Dashboard
# -------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# 1. Driver Points
driver_points.head(10).plot(
    kind="bar",
    ax=axes[0, 0],
    title="Top 10 Drivers by Points"
)
axes[0, 0].set_xlabel("Driver")
axes[0, 0].set_ylabel("Points")
axes[0, 0].tick_params(axis="x", rotation=45)

# 2. Team Points
team_points.plot(
    kind="bar",
    ax=axes[0, 1],
    title="Team Championship Points"
)
axes[0, 1].set_xlabel("Team")
axes[0, 1].set_ylabel("Points")
axes[0, 1].tick_params(axis="x", rotation=45)

# 3. Top 5 Drivers
top_5_drivers.plot(
    kind="bar",
    ax=axes[1, 0],
    title="Top 5 Drivers"
)
axes[1, 0].set_xlabel("Driver")
axes[1, 0].set_ylabel("Points")
axes[1, 0].tick_params(axis="x", rotation=30)

# 4. Average Finishing Position
avg_position = (
    df[df["Position"] != "DNF"]
    .assign(Position=lambda x: pd.to_numeric(x["Position"]))
    .groupby("Driver")["Position"]
    .mean()
    .sort_values()
    .head(10)
)

avg_position.plot(
    kind="bar",
    ax=axes[1, 1],
    title="Best Average Finishing Position"
)
axes[1, 1].set_xlabel("Driver")
axes[1, 1].set_ylabel("Average Position")
axes[1, 1].tick_params(axis="x", rotation=45)

plt.suptitle("F1 Race Data Analysis Dashboard", fontsize=18)

plt.tight_layout()

# Dashboard save
plt.savefig(
    "f1_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# -------------------------------
# 6. Race-wise Performance Analysis
# -------------------------------

race_points = df.groupby("Race")["Points"].sum().sort_values(ascending=False)

print("\nRace-wise Total Points:")
print(race_points)

plt.figure(figsize=(12, 6))

race_points.plot(kind="bar")

plt.title("Race-wise Total Points")
plt.xlabel("Race")
plt.ylabel("Total Points")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "race_wise_points.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# -------------------------------
# 6.3 Fastest Lap Analysis
# -------------------------------

fastest_laps = df[
    df["Fastest_Lap"].astype(str).str.strip().str.lower().isin(
        ["yes", "true", "1"]
    )
]

fastest_lap_count = (
    fastest_laps.groupby("Driver")
    .size()
    .sort_values(ascending=False)
)

print("\nFastest Lap Count by Driver:")
print(fastest_lap_count)

plt.figure(figsize=(12, 6))

fastest_lap_count.plot(kind="bar")

plt.title("Fastest Lap Achievements by Driver")
plt.xlabel("Driver")
plt.ylabel("Number of Fastest Laps")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "fastest_laps.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show() 

# -------------------------------
# 7. Key Project Insights
# -------------------------------

championship_leader = driver_points.idxmax()
highest_points = driver_points.max()

best_team = team_points.idxmax()
best_team_points = team_points.max()

most_fastest_laps_driver = fastest_lap_count.idxmax()
most_fastest_laps = fastest_lap_count.max()

best_average_driver = avg_position.idxmin()
best_average_position = avg_position.min()

total_races = df["Race"].nunique()
total_drivers = df["Driver"].nunique()
total_teams = df["Team"].nunique()
total_records = len(df)


# Print results in Terminal

print("\n==============================")
print("       F1 KEY INSIGHTS")
print("==============================")

print("\n1. Championship Leader:")
print("Driver:", championship_leader)
print("Total Points:", highest_points)

print("\n2. Highest Scoring Team:")
print("Team:", best_team)
print("Total Points:", best_team_points)

print("\n3. Most Fastest Laps:")
print("Driver:", most_fastest_laps_driver)
print("Fastest Laps:", most_fastest_laps)

print("\n4. Best Average Finishing Position:")
print("Driver:", best_average_driver)
print("Average Position:", round(best_average_position, 2))

print("\n5. Dataset Summary:")
print("Total Races:", total_races)
print("Total Drivers:", total_drivers)
print("Total Teams:", total_teams)
print("Total Records:", total_records)


# -------------------------------
# Save Key Insights as PNG
# -------------------------------

fig, ax = plt.subplots(figsize=(10, 7))

ax.axis("off")

insights_text = f"""
F1 RACE DATA ANALYSIS
KEY PROJECT INSIGHTS

 Championship Leader
{championship_leader} — {highest_points} Points

 Highest Scoring Team
{best_team} — {best_team_points} Points

⚡ Most Fastest Laps
{most_fastest_laps_driver} — {most_fastest_laps} Fastest Laps

 Best Average Finishing Position
{best_average_driver} — {best_average_position:.2f}

DATASET SUMMARY

Total Races: {total_races}
Total Drivers: {total_drivers}
Total Teams: {total_teams}
Total Records: {total_records}
"""

ax.text(
    0.5,
    0.5,
    insights_text,
    ha="center",
    va="center",
    fontsize=16
)

plt.tight_layout()

plt.savefig(
    "f1_key_insights.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# -------------------------------
# 8. Data Cleaning & Validation
# -------------------------------

print("\n==============================")
print("   DATA CLEANING & VALIDATION")
print("==============================")

# Check duplicate rows
duplicate_rows = df.duplicated().sum()

print("\n1. Duplicate Rows:", duplicate_rows)

if duplicate_rows == 0:
    print("No duplicate rows found.")
else:
    print("Duplicate rows found.")

# Check missing values

missing_values = df.isnull().sum()

print("\n2. Missing Values:")
print(missing_values)

if missing_values.sum() == 0:
    print("No missing values found.")
else:
    print("Missing values found.")


# Check data types

print("\n4. Data Types:")
print(df.dtypes)

print("\n==============================")
print("   VALIDATION COMPLETED")
print("==============================")

# -------------------------------
# 9. Professional F1 Dashboard
# -------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# 1. Top 10 Drivers
driver_points.head(10).plot(
    kind="bar",
    ax=axes[0, 0]
)

axes[0, 0].set_title("Top 10 Drivers by Points")
axes[0, 0].set_xlabel("Driver")
axes[0, 0].set_ylabel("Total Points")
axes[0, 0].tick_params(axis="x", rotation=45)


# 2. Team Championship
team_points.plot(
    kind="bar",
    ax=axes[0, 1]
)

axes[0, 1].set_title("Team Championship Points")
axes[0, 1].set_xlabel("Team")
axes[0, 1].set_ylabel("Total Points")
axes[0, 1].tick_params(axis="x", rotation=45)


# 3. Top 5 Drivers
top_5_drivers.plot(
    kind="bar",
    ax=axes[1, 0]
)

axes[1, 0].set_title("Top 5 Drivers")
axes[1, 0].set_xlabel("Driver")
axes[1, 0].set_ylabel("Total Points")
axes[1, 0].tick_params(axis="x", rotation=30)


# 4. Best Average Finishing Position
avg_position.head(10).plot(
    kind="bar",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Best Average Finishing Position")
axes[1, 1].set_xlabel("Driver")
axes[1, 1].set_ylabel("Average Position")
axes[1, 1].tick_params(axis="x", rotation=45)


# Main Dashboard Title
fig.suptitle(
    "F1 Race Data Analysis Dashboard",
    fontsize=20
)

plt.tight_layout()

# Save dashboard
plt.savefig(
    "f1_professional_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
