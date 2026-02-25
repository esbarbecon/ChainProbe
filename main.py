from analyzer import TransactionAnalyzer
from risk_engine import RiskEngine
import json

def main():
    # Load transaction data from sample file
    with open("sample_data.json", "r") as f:
        transactions = json.load(f)

    analyzer = TransactionAnalyzer(transactions)
    risk_engine = RiskEngine()

    # Extract wallet metrics
    metrics = analyzer.extract_metrics()

    # Calculate risk score
    score, report = risk_engine.calculate_risk(metrics)

    print("\n=== BlockSentinel Risk Report ===")
    print(f"Wallet Risk Score: {score}/100\n")

    for line in report:
        print("-", line)


if __name__ == "__main__":
    main()
