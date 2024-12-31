import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def detect_outliers(file_path, output_dir="reports/plots/"):
    """Detects and visualizes outliers using box plots."""
    data = pd.read_csv(file_path)
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

    for col in numeric_cols:
        plt.figure()
        sns.boxplot(x=data[col])
        plt.title(f"Outliers in {col}")
        plt.savefig(f"{output_dir}{col}_outliers.png")
        plt.close()

if __name__ == "__main__":
    detect_outliers("data/raw/data.csv")
