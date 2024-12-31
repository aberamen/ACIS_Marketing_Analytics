import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_univariate(file_path, output_dir="reports/plots/"):
    """Plots histograms and bar charts for univariate analysis."""
    data = pd.read_csv(file_path)
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = data.select_dtypes(include=['object']).columns

    for col in numeric_cols:
        plt.figure()
        sns.histplot(data[col], kde=True, bins=30)
        plt.title(f"Distribution of {col}")
        plt.savefig(f"{output_dir}{col}_histogram.png")
        plt.close()

    for col in categorical_cols:
        plt.figure()
        data[col].value_counts().plot(kind='bar')
        plt.title(f"Count of {col}")
        plt.savefig(f"{output_dir}{col}_bar.png")
        plt.close()

if __name__ == "__main__":
    plot_univariate("data/raw/data.csv")
