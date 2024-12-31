import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_bivariate(file_path, output_dir="reports/plots/"):
    """Plots scatter plots and correlations for bivariate analysis."""
    data = pd.read_csv(file_path)

    plt.figure()
    sns.scatterplot(x='TotalPremium', y='TotalClaims', data=data)
    plt.title("Total Premium vs. Total Claims")
    plt.savefig(f"{output_dir}premium_vs_claims_scatter.png")
    plt.close()

    plt.figure()
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.savefig(f"{output_dir}correlation_matrix.png")
    plt.close()

if __name__ == "__main__":
    plot_bivariate("data/raw/data.csv")
