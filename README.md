# D2C Pricing Strategy Decision Framework

Pricing decision framework for comparing subscription price points across conversion, retention, LTV, CAC payback, and revenue.

<!-- FOUNDER_OS_STANDARD_README -->

## The founder problem

D2C founders often debate pricing from intuition. The operating problem is knowing which price point improves conversion, retention, LTV, payback, and revenue without hiding the trade-offs.

## What this repo does

- generates subscription data
- calculates unit economics
- creates retention, LTV, and revenue visuals
- summarizes pricing recommendation

## What a founder gets in 10 minutes

- pricing strategy summary CSV
- retention curve
- LTV comparison chart
- revenue comparison chart
- decision writeup

## Before and after

Before:

- pricing debate based on anecdotes
- conversion and retention separated
- no payback view
- hard-to-explain recommendation

After:

- modeled pricing trade-off
- unit economics view
- visual comparison
- founder-ready recommendation

## Who this is for

- D2C founders
- growth operators
- pricing analysts
- Founder's Office candidates
- startup generalists

## Quick start

- Run `pip install -r requirements.txt`.
- Run `python3 data/generate_dataset.py`.
- Run `python3 analysis/unit_economics.py`.
- Run `python3 visuals/plots.py`.
- Open `pricing_strategy_summary.csv` first.

## How to fork and use this for your company

1. Click Fork.
2. Rename the repo if needed.
3. Replace `data/subscription_data.csv` with your experiment or modeled data.
4. Update assumptions in `analysis/unit_economics.py`.
5. Regenerate visuals.
6. Keep customer-level data out of public forks.

### Non-technical path

- Replace one CSV: `data/subscription_data.csv`.
- Run three commands.
- Read one output first: `pricing_strategy_summary.csv`.
- Use charts only after checking assumptions.

## Input format

- customer or cohort ID
- price point
- conversion
- retention
- revenue
- CAC
- subscription duration
- segment

The default sample data and examples are synthetic, anonymized, or template-only unless the repo explicitly documents a public source. Keep private customer, prospect, employee, investor, borrower, merchant, payment, or company data out of public forks.

## Output files

- `pricing_strategy_summary.csv`: decision summary
- `retention_curve.png`: retention visual
- `ltv_comparison.png`: LTV visual
- `revenue_comparison.png`: revenue visual

## Example founder workflow

- Monday: define pricing question.
- Tuesday: update data or assumptions.
- Wednesday: run unit economics.
- Thursday: inspect visuals and trade-offs.
- Friday: decide test, rollout, or no change.

## Customization guide

Customize these before using the repo for a real company:

- price points
- CAC
- retention assumptions
- segments
- success criteria
- visual style

## Where this fits in the Founder OS

This is a strategy decision module. Pair it with `startup-metrics-playbook` for metric definitions and `edtech-saas-financial-model` for broader financial impact.

## Why this matters

This is not a chart exercise. It is a founder decision packet for pricing trade-offs.

## Roadmap

- scenario config file
- Google Sheets output
- confidence interval notes
- subscription cohort import
- pricing memo template

## Contributing

Practical improvements are welcome when they make the workflow easier to fork, run, or adapt. Keep changes focused on the operating workflow and avoid adding private data or mandatory paid dependencies.

## License

MIT License. See [LICENSE](LICENSE).

## Built by

Built by Shubham Singh, a founder-facing operator focused on RevOps, GTM systems, startup metrics, AI workflows, and operating systems for early-stage teams.

## Use this in your company

Fork it, replace the sample inputs with your company context, and run the workflow. Start with the main output listed in the Quick Start section. Keep private data out of public forks.

## If you are a Founder's Office candidate

Use this repo to understand how a founder-facing operator turns messy inputs into decisions, cadence, and execution artifacts. Fork it, adapt it to a real company example, and write a short case note explaining what changed.

---

## Detailed implementation notes

The founder-facing guide above is the fastest path. The original repo-specific notes are preserved below for deeper implementation context.

## Problem This Solves

D2C founders often debate pricing from intuition: lower price for growth, higher price for premium positioning. The actual problem is knowing which price point improves conversion, retention, LTV, CAC payback, and revenue at the same time.

## How It Helps

- Simulates subscription behavior across two price points and compares conversion, retention, revenue, LTV, ARPU, and CAC payback.
- Turns a pricing debate into a forkable decision framework with charts and a clear recommendation.
- Gives founders a starting model for validating price cuts, tiering, and pricing A/B tests before changing production pricing.

## When To Fork This

- Fork this if you run a D2C, subscription, fitness, wellness, creator, or consumer SaaS business and need a pricing decision model.
- Fork it when your team is debating growth pricing vs premium positioning without cohort-level evidence.
- Replace the synthetic assumptions with your own funnel, retention, CAC, ARPU, and cohort data.

## Use This In Your Company

This repo is designed to be forked into an internal company workflow. Fork it, replace the sample inputs with your company context, and keep only the parts that match your operating cadence. No permission request or sales call is needed before using it; the repo is the handoff. Check the license if you plan to redistribute your version.

- Use it as a pricing decision model for D2C, subscription, wellness, creator, or consumer SaaS products.
- Keep the comparison logic: price point -> conversion -> retention -> LTV -> revenue -> CAC payback.
- Replace synthetic assumptions with your funnel, cohort, price, and retention data.

## Minimum Edits To Make It Yours

Change these first:

| Edit | Where | Why |
|---|---|---|
| Replace subscription or order data. | `data/subscription_data.csv` | Makes LTV, retention, and pricing outputs reflect your actual customers. |
| Update price points and plan names. | `analysis/unit_economics.py` | Aligns the scenarios with the packages your D2C brand can actually sell. |
| Tune retention and churn assumptions. | `analysis/unit_economics.py` | Pricing decisions are sensitive to repeat purchase behavior. |
| Regenerate charts and summary outputs. | `visuals/plots.py` and `pricing_strategy_summary.csv` | Keeps the executive view consistent with the edited assumptions. |

You can leave the model structure, comparison charts, and unit-economics framing alone on the first fork. Change assumptions first; add new pricing mechanics only after the base scenarios make sense.

## Executive Summary (1-Slide)

- Decision: Reduce pricing from ₹999 → ₹699
- Why:
 - Conversion increases materially at lower price
 - Retention improves slightly, indicating better product-market fit at this price point
 - LTV increases despite lower ARPU due to higher retention
 - Total revenue is maximized at ₹699
- Impact:
 - Faster user acquisition
 - Stronger top-line growth
 - Improved unit economics (LTV > CAC, faster payback)
- Risks:
 - Potential brand dilution (premium perception)
 - Attracting lower-intent users
- Mitigation:
 - Introduce tiered pricing (Basic vs Premium)
 - Run controlled A/B experiments before full rollout
 - Monitor cohort retention and LTV closely

---

## Key Results Snapshot

- Conversion Rate:
 - ₹699: ~9.1%
 - ₹999: ~4.4%

- LTV:
 - ₹699: ~₹362
 - ₹999: ~₹260

- Revenue:
 - ₹699 outperforms ₹999 by ~40%+

Conclusion: Lower pricing improves both growth and unit economics.

---

## Business Context

The company is a D2C fitness subscription platform offering personalized workout and diet plans. The current pricing is ₹999/month.

However, the business is facing:
- Low conversion from free to paid users
- High early-stage churn
- Increasing competition from lower-priced alternatives

This raises the need to evaluate whether pricing is a key constraint to growth.

---

## Objective

To determine whether reducing subscription pricing improves customer lifetime value (LTV), conversion rates, and overall revenue without compromising unit economics.

---

## Core Question

Should the company reduce its subscription pricing to improve growth and retention?

---

## Approach

The problem was broken down into:

- Conversion impact
- Retention behavior
- Revenue generation
- Customer lifetime value (LTV)
- Unit economics (ARPU, CAC payback)

A simulated dataset was created to model user behavior across different pricing strategies.

---

## Dataset

Synthetic dataset generated using Python to simulate subscription behavior.

**Key Columns:**
- user_id
- month
- price
- converted
- churned
- retained
- acquisition_channel

---

## Key Insights

1. Conversion improves significantly at lower pricing
  Lower price reduces entry friction and increases paid user volume

2. Retention is higher for lower-priced users
  Users show slightly better stickiness at ₹699

3. LTV increases despite lower pricing
  Higher retention offsets the lower price point

4. Revenue is maximized at ₹699
  Increased volume drives higher total revenue

---

## Trade-Off Analysis

| Factor | ₹699 | ₹999 |
|--------|------|------|
| Conversion | High | Low |
| Retention | Moderate | Lower |
| LTV | Higher | Lower |
| Revenue | Higher | Lower |
| Positioning | Mass | Premium |

---

## Visual Analysis

### Retention Curve
Shows user retention trends over time across pricing strategies.

![Retention Curve](retention_curve.png)

### LTV Comparison
Compares customer lifetime value across pricing strategies.

![LTV Comparison](ltv_comparison.png)

### Revenue Comparison
Highlights total revenue impact by pricing strategy.

![Revenue Comparison](revenue_comparison.png)

---

## Business Impact

- Pricing optimization can increase revenue by ~40%+
- Improved conversion reduces CAC payback period
- Higher retention compounds long-term LTV growth

---

## Recommendation

The company should reduce pricing from ₹999 to ₹699.

This pricing strategy:
- Maximizes revenue
- Improves customer acquisition
- Enhances retention
- Strengthens overall unit economics

---

## Strategic Considerations

- Introduce tiered pricing to retain premium positioning
- Run A/B tests before full rollout
- Monitor retention cohorts closely
- Evaluate long-term LTV impact over a longer horizon

---

## What I Would Do Next as Founder's Office

1. Run Controlled Pricing Experiment
  - A/B test ₹999 vs ₹699 across cohorts
  - Measure conversion, 30-day retention, and LTV

2. Introduce Tiered Pricing
  - ₹499: Entry-level (limited features)
  - ₹699: Core plan (optimized for growth)
  - ₹999: Premium plan (advanced features, coaching, personalization)

3. Improve Onboarding Experience
  - Reduce early churn by improving first-session experience
  - Add guided onboarding and habit formation nudges

4. Cohort-Based Retention Analysis
  - Track retention by acquisition channel and pricing
  - Identify high-LTV segments

5. Optimize CAC Channels
  - Double down on high-performing channels (organic/referral)
  - Reduce spend on low-LTV cohorts

6. Build LTV Forecasting Model
  - Project long-term revenue under different pricing scenarios
  - Support future pricing and growth decisions

---

## Conclusion

Pricing is a critical growth lever.

A reduction to ₹699 improves both growth and unit economics, making it the optimal strategy for scaling the business.

---

## Tech Stack

- Python (Pandas, NumPy)
- Matplotlib
- Synthetic Data Simulation

---

## Project Structure

```
d2c-pricing-strategy-decision-framework/
│
├── data/
│  ├── generate_dataset.py
│  └── subscription_data.csv
│
├── analysis/
│  └── unit_economics.py
│
├── visuals/
│  └── plots.py
├── retention_curve.png
├── ltv_comparison.png
├── revenue_comparison.png
├── pricing_strategy_summary.csv
│
└── README.md
```

## How to Run

1. Generate dataset:

```bash
python3 data/generate_dataset.py
```

2. Run analysis:

```bash
python3 analysis/unit_economics.py
```

3. Generate visuals:

```bash
python3 visuals/plots.py
```
