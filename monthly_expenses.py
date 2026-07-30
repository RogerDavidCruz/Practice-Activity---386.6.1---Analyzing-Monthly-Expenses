import pandas as pd
import matplotlib.pyplot as plt

# Sample monthly expense data
data = {
    "Expense Category": [
        "Rent",
        "Groceries",
        "Internet",
        "Transportation",
        "Entertainment"
    ],
    "Amount Spent": [1200, 450, 75, 180, 220]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Create a light color palette
colors = plt.cm.Pastel1(range(len(df)))

# Create the figure
plt.figure(figsize=(8, 5))

# Create horizontal bar chart
plt.barh(
    df["Expense Category"],
    df["Amount Spent"],
    color=colors,
    height=0.6
)

# Add chart title and labels
plt.title("Monthly Expenses Distribution")
plt.xlabel("Amount Spent ($)")
plt.ylabel("Expense Categories")

# Add a light grid
plt.grid(axis="x", linestyle="--", alpha=0.4)

# Display chart
plt.show()