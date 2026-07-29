# Datasheet for BBO Capstone Dataset

## Motivation
- The dataset was created to support a Black-Box Optimisation (BBO) task, where the objective is to identify high-performing inputs for eight unknown functions using only query-response data.
- It was developed by Jose Kurian as part of an AI/ML capstone project for educational and research purposes.
- The dataset supports experimentation with model-guided optimisation strategies, including Gaussian Processes, Expected Improvement and ensemble methods.
- A key purpose is to make the optimisation process transparent, reproducible and easy to review.

## Composition
- Each instance represents a query vector and its corresponding function output.
- The dataset contains:
  - Eight black-box functions: F1-F8
  - Sequential query history across project rounds
  - Input vectors normalised to `[0, 1]^d`
  - Function outputs as scalar numerical values
  - Processed NumPy arrays and generated query/result files
- Input dimensionality varies by function, ranging from low-dimensional to higher-dimensional search spaces.
- No missing values were observed in the collected query-response records.
- The dataset contains only synthetic numerical optimisation data. It does not include personal, confidential or sensitive information.

## Collection process
- Data was acquired through repeated interaction with the BBO platform.
- For each round:
  1. One query was submitted for each function.
  2. The platform returned a scalar output.
  3. The result was added to the historical dataset.
  4. The updated data informed the next query.
- The sampling strategy evolved over time:
  - Early rounds: broad exploration and random/heuristic sampling.
  - Middle rounds: Gaussian Process-based Bayesian optimisation.
  - Later rounds: bootstrap GP ensemble, Expected Improvement and Sobol candidate sampling.
- Data was collected sequentially across the capstone project rounds.

## Preprocessing/cleaning/labelling
- Preprocessing included:
  - Input validation
  - Dimensionality checks
  - Ensuring inputs and outputs had matching rows
  - Automatic length-scale estimation for GP modelling
  - Optional `asinh` transformation where output values had a large numerical range
- No manual labelling was carried out. The returned function output acts as the optimisation target.
- Processed data, generated queries, result summaries and candidate rankings were saved to support reproducibility.
- Raw and processed data are organised separately in the project repository where available.

## Uses
- The dataset can be used for:
  - Black-box optimisation experiments
  - Bayesian optimisation research
  - Surrogate model evaluation
  - Exploration-versus-exploitation analysis
  - Reproducibility and transparency exercises
- Future users should be aware that the dataset is small and sequentially collected. Later observations may be biased towards regions that appeared promising in earlier rounds.
- The dataset should not be used for:
  - Medical decision-making
  - Financial decision-making
  - Safety-critical optimisation
  - Claims about real-world system performance without further validation
- Risks can be mitigated by clearly documenting assumptions, preserving query history and comparing results against alternative optimisation methods.

## Distribution
- The dataset is distributed through the BBO capstone project GitHub repository.
- It is intended for educational review, peer feedback and reproducibility of the capstone workflow.
- The dataset is subject to the licence and terms of use of the associated GitHub repository.

## Maintenance
- The dataset is maintained by the project author.
- Version control is managed through GitHub commits.
- The dataset may be updated if additional query rounds, results or documentation are added.
