
# 📊 Statistical Evaluation and Outlier Detection in Machine Learning

Understanding your dataset statistically is a key step in the machine learning process. This guide provides a quick overview of basic statistical metrics and how to handle outliers effectively.

---

## 🔎 1. Basic Statistical Evaluation

Before training your model, analyze the **features** (inputs) and **labels** (targets) using the following:

### ✅ Common Statistics to Calculate:
- **Mean and Median**:
  - Mean: Average value.
  - Median: Middle value (more robust to outliers).

- **Standard Deviation**:
  - Measures data spread around the mean.

- **Percentiles/Quartiles**:
  - **0th percentile**: Minimum value.
  - **25th percentile (Q1)**: Lower quartile.
  - **50th percentile (Q2)**: Median.
  - **75th percentile (Q3)**: Upper quartile.
  - **100th percentile**: Maximum value.

These metrics help you understand data distribution.

---

## ⚠️ 2. Outlier Detection

Outliers are values that deviate significantly from the rest of the dataset.

### 🔍 How to Detect Outliers:
- Check **asymmetry in percentiles**:
  - If `(Q1 - Q0)` is much smaller or larger than `(Q4 - Q3)`, potential outliers exist.

Example:
```
Q1 - Q0 = 5
Q4 - Q3 = 50
```

Indicates an outlier in the upper range.

---

## 🧹 3. Handling Outliers

### Option A: Mistake Outliers
- **Cause**: Human/sensor error.
- **Action**: Delete the data point.

### Option B: Legitimate Outliers
- **Cause**: Valid extreme value.
- **Actions**:
  - ✅ Keep: If model needs to predict on such edge cases.
  - ❌ Remove or transform: If these do not reflect your model’s objective.

  Techniques like **clipping** can be used to limit extreme values.

---

## 🚨 Caution

> **Do not rely only on basic statistics.**
Visual inspection and domain knowledge are essential to detect hidden anomalies.

---

## ✅ Summary

| Step             | What to Do                                         |
|------------------|----------------------------------------------------|
| Evaluate Stats   | Mean, Median, Std, Quartiles                      |
| Find Outliers    | Check percentile ranges (Q0–Q1 vs. Q3–Q4)         |
| Handle Outliers  | Delete, keep, or clip based on model's need       |
| Be Careful       | Always visualize & understand domain context      |
