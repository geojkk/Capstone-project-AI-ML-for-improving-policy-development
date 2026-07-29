# Model Card

## Model Description

**Input:**
- Historical query points for each black-box function.
- Corresponding scalar function evaluations.
- Search space bounded to `[0, 1]^d`.
- Function-specific dimensionality and previous round results.

**Output:**
- Recommended next query point for each function.
- Candidate rankings based on acquisition scores.
- Summary files containing selected points, model settings and performance indicators.

**Model Architecture:**
- The approach uses Bayesian Optimisation with a Gaussian Process surrogate model.
- A bootstrap ensemble of Gaussian Process models is used to improve robustness in a low-data setting.
- The active strategy uses:
  - Matérn kernel
  - Automatic length-scale estimation
  - Expected Improvement acquisition function
  - Sobol sampling to generate a large global candidate pool
  - Optional `asinh` transformation for outputs with large numerical ranges
- The final query is selected by ranking candidate points using ensemble Expected Improvement.

## Performance
- The primary performance metric is the function output value returned by the BBO platform.
- Supporting metrics include:
  - Expected Improvement
  - Predicted mean
  - Predicted uncertainty
  - Improvement compared with previous rounds
- Overall performance shows:
  - Stronger gains in earlier rounds as the search space was explored.
  - More incremental gains in later rounds as the model refined known promising regions.
  - Better performance where functions had clearer structure.
  - Lower confidence in noisy or higher-dimensional functions due to limited observations.
- Performance was analysed using the accumulated query history and generated result summaries across the eight functions.

## Limitations
- The approach is limited by the small number of observations per function.
- Gaussian Processes may struggle with highly irregular, noisy or high-dimensional functions.
- Later queries may become concentrated around promising areas, increasing the risk of local optima.
- Model behaviour is sensitive to hyperparameters such as kernel choice, length-scale bounds, exploration parameter and noise level.
- The ensemble improves robustness but increases computational cost.

## Trade-offs
- **Exploration vs exploitation:** Expected Improvement balances testing uncertain regions against refining known high-performing regions.
- **Robustness vs computational cost:** Bootstrap ensembles reduce instability but require fitting multiple GP models.
- **Accuracy vs interpretability:** GP-based Bayesian Optimisation is more interpretable than many deep learning alternatives, but it may be less flexible for complex high-dimensional functions.
- **Automation vs transparency:** Automatic length-scale estimation and output transformation improve stability, but require clear documentation so others can understand the modelling choices.
