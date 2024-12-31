import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind

def test_risk_province(data):
    contingency_table = pd.crosstab(data['Province'], data['Risk'])
    chi2, p, _, _ = chi2_contingency(contingency_table)
    return p

def test_margin_zipcode(data):
    group_a = data[data['ZipCode'] == 'GroupA']['Margin']
    group_b = data[data['ZipCode'] == 'GroupB']['Margin']
    t_stat, p = ttest_ind(group_a, group_b)
    return p

def main(file_path):
    data = pd.read_csv(file_path)
    
    p_risk_province = test_risk_province(data)
    print(f"Province Risk Difference P-value: {p_risk_province}")
    
    p_margin_zipcode = test_margin_zipcode(data)
    print(f"Margin Difference Between ZipCodes P-value: {p_margin_zipcode}")

if __name__ == "__main__":
    main("data/processed/processed_data.csv")
