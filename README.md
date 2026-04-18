# Conversion Rate Optimization — A/B Testing

A statistically rigorous A/B experiment to evaluate whether a new product feature (Version B) significantly improves user conversion rate over the baseline (Version A).

---

## Problem Statement

Product teams often launch features without knowing if they truly move the needle. This project answers: *"Is the higher conversion rate in Version B real, or just random chance?"* — using proper statistical testing before recommending a rollout.

---

## Tech Stack

`Python` `Pandas` `SciPy` `Matplotlib` `Seaborn`

---

## Methodology

1. **Experiment Design** — Defined control (Version A) and treatment (Version B) groups
2. **Data Collection** — Analyzed 200+ user interaction records
3. **Statistical Testing** — Two-sample t-test with defined significance threshold (α = 0.05)
4. **Metrics Calculated**:
   - Conversion rates per variant
   - Uplift (relative % change)
   - p-value for statistical significance
   - Confidence intervals

---

## Key Finding

> Version B showed a higher raw conversion rate — but the result was **not statistically significant** (p-value > 0.05). The recommendation was to **collect more data before deployment**, avoiding a premature and potentially costly rollout.

---

## Project Structure
AB-Testing-Project/
├── ab_testing.py       # Main analysis script
├── data/               # User interaction dataset
├── results/            # Output: charts, summary stats
└── README.md

---

## How to Run

```bash
pip install pandas scipy matplotlib seaborn
python ab_testing.py
```

---

## Skills Demonstrated

- Experiment design and hypothesis formulation
- Statistical significance testing (t-test)
- p-value interpretation and business translation
- Data-driven product recommendation