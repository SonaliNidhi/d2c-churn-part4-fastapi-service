# Monitoring Plan

## Objective

Monitor model performance, API reliability, and business impact after deployment.

---

## Data Drift Monitoring

Track the distribution of:

* recency_days
* frequency_180d
* monetary_180d
* ticket_count_90d
* sessions_30d

Compare incoming production data against training data monthly.

### Alert Threshold

Trigger investigation if any major feature distribution shifts by more than 20%.

---

## Prediction Distribution Monitoring

Track:

* Average churn probability
* Percentage of low-risk customers
* Percentage of medium-risk customers
* Percentage of high-risk customers

Unexpected changes may indicate model degradation or changing customer behavior.

---

## Business Outcome Monitoring

Track:

* Retention campaign conversion rate
* Churn reduction rate
* Revenue retained
* Campaign ROI
* Retention offer acceptance rate

These metrics validate whether model-driven interventions are generating business value.

---

## API Monitoring

Track:

* Total request volume
* Average response time
* API uptime
* 4xx client errors
* 5xx server errors

Alert engineering teams if error rates exceed acceptable thresholds.

---

## Retraining Triggers

Schedule monthly model reviews.

Immediate retraining should be considered if:

* ROC-AUC decreases by more than 5%
* Significant data drift is detected
* Customer behavior changes materially
* Business KPIs deteriorate
* New data becomes available

---

## Escalation Process

1. Investigate data quality issues.
2. Review feature drift.
3. Review prediction distributions.
4. Retrain and validate model.
5. Deploy updated model after approval.
