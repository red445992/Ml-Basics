## Model Card: COMPAS Recidivism Prediction
# Model Details

1. Model Type: Logistic Regression (baseline)

2. Purpose: Predict whether a defendant will recidivate within two years based on features such as age, sex, prior offenses, and charge degree.

3. Dataset: COMPAS dataset from ProPublica (criminal justice data).

# Intended Use
1. This model is intended for educational purposes to demonstrate fairness and bias challenges in machine learning.

2. Not intended for real-world criminal justice decision making.

# Features Used
1. Age
2. Sex (encoded)
3. Prior offenses count (priors_count)
4. Charge degree (encoded)

# Evaluation Metrics
1. Accuracy
2. Precision
3. Recall

# Ethical Considerations
    The COMPAS algorithm and this model highlight concerns of algorithmic bias, especially across racial groups.
    The model may reflect or amplify biases present in historical criminal justice data.
    It is critical to analyze and mitigate unfair outcomes before considering deployment.

# Bias and Fairness Analysis
    Performance metrics were evaluated separately across race and gender groups.
    Differences in accuracy, false positive rates, and false negative rates were examined to identify potential bias.
    This project emphasizes the importance of transparency and fairness in predictive modeling.

# Limitations
    1. The model is a simple baseline and does not capture all factors influencing recidivism.
    2. Historical data contains biases; model predictions can perpetuate these.
    3. The model should not be used for making legal or parole decisions.

# How to Use
    1. Load and preprocess COMPAS dataset.

    2. Train logistic regression on selected features.

    3. Evaluate performance overall and by subgroups.

    4. Use findings to inform discussions on fairness in ML.