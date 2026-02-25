class RiskEngine:
    def __init__(self):
        # Risk thresholds configuration
        self.large_tx_threshold = 10000
        self.flagged_threshold = 2

    def calculate_risk(self, metrics):
        score = 0
        report = []

        # High transaction volume
        if metrics["tx_count"] > 50:
            score += 20
            report.append("High transaction frequency detected.")

        # Large transaction anomaly
        if metrics["max_amount"] > self.large_tx_threshold:
            score += 30
            report.append("Unusually large transaction detected.")

        # High deviation suggests inconsistent behavior
        if metrics["std_amount"] > 5000:
            score += 20
            report.append("High variance in transaction amounts.")

        # Interaction with flagged wallets
        if metrics["flagged_interactions"] >= self.flagged_threshold:
            score += 30
            report.append("Multiple interactions with flagged wallets.")

        # Cap score at 100
        score = min(score, 100)

        if score == 0:
            report.append("No significant risk indicators found.")

        return score, report
