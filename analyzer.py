from collections import defaultdict
import statistics

class TransactionAnalyzer:
    def __init__(self, transactions):
        # Store transaction list
        self.transactions = transactions

    def extract_metrics(self):
        # Extract wallet behavioral metrics
        amounts = [tx["amount"] for tx in self.transactions]
        timestamps = [tx["timestamp"] for tx in self.transactions]
        flagged_interactions = sum(1 for tx in self.transactions if tx["flagged"])

        metrics = {}

        # Total transactions
        metrics["tx_count"] = len(self.transactions)

        # Average transaction amount
        metrics["avg_amount"] = statistics.mean(amounts) if amounts else 0

        # Standard deviation for anomaly detection
        metrics["std_amount"] = statistics.stdev(amounts) if len(amounts) > 1 else 0

        # Maximum transaction value
        metrics["max_amount"] = max(amounts) if amounts else 0

        # Number of flagged interactions
        metrics["flagged_interactions"] = flagged_interactions

        return metrics
