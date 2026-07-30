# PA 386.6.1 – Analyzing Monthly Expenses

## Overview

This project demonstrates how to visualize monthly expenses using Python, Pandas, and Matplotlib. Sample expense data is stored in a Pandas DataFrame and displayed as a horizontal bar chart. The visualization compares the amount spent across different expense categories while demonstrating basic data visualization techniques.

## Learning Objectives

By completing this practice activity, you will learn how to:

* Create a Pandas DataFrame from a Python dictionary.
* Visualize data using Matplotlib.
* Create a horizontal bar chart with `plt.barh()`.
* Customize chart colors using a Matplotlib color palette.
* Add chart titles and axis labels.
* Improve chart readability with grid lines.

## Technologies Used

* Python 3
* Pandas
* Matplotlib
* uv (Python package and project manager)

## Project Structure

```text
PA-386.6.1-Analyzing-Monthly-Expenses/
│
├── monthly_expenses.py
├── README.md
├── pyproject.toml
└── uv.lock
```

## Project Setup

### Create a New Project

```bash
uv init PA-386.6.1-Analyzing-Monthly-Expenses
cd PA-386.6.1-Analyzing-Monthly-Expenses
```

### Activate the Virtual Environment (Windows)

**Git Bash**

```bash
source .venv/Scripts/activate
```

**PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### Install Required Libraries

For this assignment:

```bash
uv add pandas
uv add matplotlib
```

Common libraries used throughout the course:

```bash
uv add pandas
uv add matplotlib
uv add numpy
uv add mysql-connector-python
```

> **Note:** Only **Pandas** and **Matplotlib** are required for this project.

## Running the Program

Run the program from the project directory:

```bash
uv run monthly_expenses.py
```

## Program Description

The program performs the following steps:

1. Imports the Pandas and Matplotlib libraries.
2. Creates sample monthly expense data using a Python dictionary.
3. Loads the data into a Pandas DataFrame.
4. Creates a horizontal bar chart using `plt.barh()`.
5. Applies the **Pastel1** color palette to give each bar a different color.
6. Sets the figure size for better readability.
7. Adds a chart title and axis labels.
8. Displays a light grid along the x-axis.
9. Displays the completed visualization.

## Sample Data

| Expense Category | Amount Spent ($) |
| ---------------- | ---------------: |
| Rent             |             1200 |
| Groceries        |              450 |
| Internet         |               75 |
| Transportation   |              180 |
| Entertainment    |              220 |

## Expected Output

The program generates a horizontal bar chart titled **Monthly Expenses Distribution** that includes:

* Expense categories displayed on the y-axis.
* Amount spent displayed on the x-axis.
* Color-coded horizontal bars.
* Chart title and axis labels.
* A light x-axis grid for improved readability.

## Bonus Enhancement

As part of the bonus portion of the assignment, this project uses Matplotlib's **Pastel1** color palette to automatically assign a different pastel color to each expense category. This improves the chart's visual appearance while making each bar easier to distinguish.

## Concepts Demonstrated

* Python dictionaries
* Pandas DataFrames
* Data visualization with Matplotlib
* Horizontal bar charts (`plt.barh()`)
* Figure sizing
* Color palettes
* Grid customization
* Chart titles and axis labels

## Author

**Roger Cruz**

## Assignment

**PA – Practice Activity – 386.6.1 – Analyzing Monthly Expenses**
