import pandas as pd

def summarize_data(file_path):
    """Summarizes data with descriptive statistics and info."""
    data = pd.read_csv(file_path)
    print("Descriptive Statistics:")
    print(data.describe())
    print("\nData Information:")
    print(data.info())
    print("\nMissing Values:")
    print(data.isnull().sum())

if __name__ == "__main__":
    summarize_data("data/raw/data.csv")
