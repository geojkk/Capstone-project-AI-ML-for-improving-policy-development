# Black-Box Optimisation (BBO) Capstone Project

## NON-TECHNICAL EXPLANATION OF YOUR PROJECT

This project explores how to find the best solutions to problems where the underlying system is unknown. Instead of having access to equations or rules that describe how a system behaves, I can only submit inputs and observe the resulting output. The goal is to learn from previous observations and make increasingly better decisions about what to test next.

This type of optimisation is common in real-world machine learning, where experiments can be time-consuming or expensive. Examples include tuning AI models, improving system performance and optimising engineering processes. Throughout the project, I used statistical models to balance experimentation with refinement, gradually improving results while learning more about the underlying search space.

---

## REPOSITORY STRUCTURE

This repository has been organised to support transparency, reproducibility and ease of navigation.

```text
├── data/
│   ├── raw/
│   └── processed/
│
├── queries/
│
├── results/
│
├── src/
│
├── notebooks/
│
├── docs/
│   ├── datasheet.md
│   └── model_card.md
│
├── LICENSE
└── README.md
```

### Folder Overview

- **data/** – Query history and function evaluation data.
- **queries/** – Submitted optimisation queries organised by round.
- **results/** – Returned function evaluations and performance tracking.
- **src/** – Core optimisation code and reusable modules.
- **notebooks/** – Exploratory analysis and modelling experiments.
- **docs/** – Supporting documentation, including the Datasheet and Model Card.

This repository captures the complete lifecycle of the project, from early exploration through to the final optimisation strategy.

---

## DATA

The dataset consists of the query history and function evaluation results generated throughout the BBO challenge.

Each observation contains:

- An input vector containing numerical values normalised between `0` and `1`.
- A corresponding scalar output representing the performance of that input.
- The optimisation round in which the query was submitted.

The data was generated through iterative interaction with the capstone project portal. Early rounds focused on broad exploration of the search space, while later rounds increasingly relied on model-guided optimisation.

The dataset is characterised by:

- Limited observations relative to the size of the search space.
- Functions ranging from lower-dimensional to higher-dimensional optimisation problems.
- Sparse coverage, particularly in higher dimensions.
- Sequential data collection, where each new query depends on previous observations.

Because of these characteristics, the dataset is best suited to optimisation and decision-making under uncertainty rather than conventional predictive modelling.

---

## MODEL

The primary model used throughout the project was a **Gaussian Process (GP) surrogate model**.

Gaussian Processes were chosen because they are particularly effective in optimisation problems where:

- Data is limited.
- Evaluations are expensive.
- Uncertainty estimation is important.

Unlike many predictive models, a GP provides both:

1. A predicted mean (expected performance).
2. A predictive uncertainty estimate.

To determine which point to evaluate next, I used the **Expected Improvement (EI)** acquisition function. Expected Improvement balances two competing objectives:

- **Exploration** – testing areas where the model is uncertain.
- **Exploitation** – refining areas already predicted to perform well.

As the project progressed, I enhanced the approach through a **bootstrap ensemble**. Rather than fitting a single GP, multiple GPs were trained using bootstrap samples of the available data. Predictions and Expected Improvement scores were averaged across the ensemble, improving robustness and reducing sensitivity to noise.

Alternative models considered included:

- Linear Regression
- Logistic Regression
- Support Vector Machines (SVMs)
- Neural Network Surrogate Models

However, Gaussian Processes consistently provided the strongest balance of interpretability, uncertainty estimation and optimisation performance given the available data.

---

## HYPERPARAMETER OPTIMISATION

Several important hyperparameters influenced the behaviour and performance of the optimisation process.

### Gaussian Process Parameters

#### Kernel Selection

The main kernels evaluated were:

- Matérn Kernel
- Radial Basis Function (RBF) Kernel

The Matérn kernel generally provided the most reliable performance because it allowed moderate irregularity in the response surface while remaining stable.

#### Length-Scale

Length-scale controls how quickly the model assumes the function changes across the search space.

I used:

- Automatic length-scale initialisation.
- Data-driven length-scale bounds.
- Multiple optimisation restarts.

This improved model stability and reduced poor fits caused by inappropriate initial settings.

#### Noise Parameter (Alpha)

A small non-zero alpha value was used to:

- Improve numerical stability.
- Reduce sensitivity to noisy observations.
- Improve optimisation robustness.

### Expected Improvement Parameters

The exploration parameter (ξ) controlled the balance between exploration and exploitation:

- Lower values encouraged exploitation.
- Higher values encouraged exploration.

As the challenge progressed, I gradually shifted toward a more exploitative strategy while retaining some exploratory behaviour.

### Ensemble Parameters

The most significant improvement came from introducing a bootstrap ensemble.

Key parameters included:

- Number of bootstrap models.
- Bootstrap sample size.
- Random seed control.

Increasing the ensemble size improved stability but increased computational cost.

### Candidate Generation

Candidate points were generated using:

- Sobol sampling.
- Large candidate pools.

This provided broad and efficient coverage of the search space before candidate ranking using Expected Improvement.

---

## RESULTS

The best results were achieved through the combination of:

1. Gaussian Process surrogate modelling.
2. Expected Improvement acquisition.
3. Bootstrap ensemble averaging.
4. Sobol candidate sampling.

### Key Findings

- High-performing points frequently formed identifiable clusters.
- Exploration was most important during early rounds.
- Exploitation became more effective as more observations accumulated.
- Ensemble modelling significantly improved stability and robustness.
- Higher-dimensional functions proved significantly more challenging than lower-dimensional functions.

### Strategy Evolution

| Phase | Focus |
|---------|---------|
| Early Rounds | Broad exploration |
| Middle Rounds | Model-guided optimisation |
| Later Rounds | Ensemble-based optimisation |
| Final Rounds | Cluster refinement and exploitation |

One of the most important lessons was that uncertainty estimation often mattered as much as the predicted objective value itself. Simply selecting the highest predicted point was not always the best decision; balancing prediction quality with uncertainty produced more reliable long-term improvements.

### Key Lessons Learned

- Effective optimisation requires balancing exploration and exploitation.
- Ensemble methods can improve stability when data is limited.
- High-performing solutions often emerge within clusters.
- Robust decision-making is often more valuable than aggressive optimisation.
- Good documentation and reproducibility are essential components of ML projects.


## CONTACT DETAILS

**Jose Kurian**

Email: <jkkvlog@gmail.com>

---

## LICENCE

This project was completed as part of the Black-Box Optimisation (BBO) Capstone Project.

Unless otherwise stated, the contents of this repository are released under the MIT Licence.

---

## ACKNOWLEDGEMENTS

This work was completed as part of the Emeritus Black-Box Optimisation (BBO) Capstone Project and demonstrates the application of Bayesian Optimisation, uncertainty-aware modelling and decision-making under limited evaluation budgets.

The project provided valuable experience in surrogate modelling, optimisation under uncertainty, hyperparameter tuning and reproducible machine learning workflows.
