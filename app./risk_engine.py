
def risk_reason(customer):

    reasons = []

    if customer.recency_days > 90:
        reasons.append(
            "inactive customer"
        )

    if customer.ticket_count_90d > 3:
        reasons.append(
            "high complaint volume"
        )

    if customer.sessions_30d < 3:
        reasons.append(
            "low engagement"
        )

    if len(reasons) == 0:

        reasons.append(
            "normal behavior"
        )

    return ", ".join(reasons)
