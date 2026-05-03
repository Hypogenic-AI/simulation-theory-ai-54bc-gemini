# Paper Outline: A Theory of Simulation in Large Language Models

## 1. Title & Abstract
- **Title**: A Theory of Simulation in Large Language Models: Multiversal Branching and the Superset of Human Behavior
- **Abstract**: 
    - Context: LLMs are increasingly used as agents in social simulations.
    - Gap: Current evaluations focus on point-estimate accuracy (most likely behavior) rather than the full distribution of possibilities.
    - Approach: We propose a "Multiverse Branching" framework to explore the outcome manifold of LLMs across social scenarios.
    - Results: GPT-4o generates diverse, plausible outcomes (entropy > 0) but shows mode collapse for generic personas. Explicit prompting can traverse the "tails" of human behavior.
    - Significance: Establishes LLMs as "multiverse simulators" capable of capturing underlying behavioral factors.

## 2. Introduction
- **Hook**: LLMs as "simulators" rather than just next-token predictors.
- **Problem**: Need for a theoretical framework to use LLMs for predicting *what could happen* in social systems.
- **Gap**: Lack of distributional analysis of LLM behavior in social dilemmas.
- **Contribution**:
    - Propose a Manifold-based Theory of Simulation for LLMs.
    - Empirical demonstration of multiverse branching in social conflict.
    - Evidence of cultural and persona-based grounding in simulated outcomes.
    - Characterization of "mode collapse" in generic human simulations.

## 3. Related Work
- **LLMs as Simulators**: Reynolds & McDonell (2021), Shanahan et al. (2023).
- **Generative Agents**: Park et al. (2023), Piao et al. (2025).
- **Economic & Social Simulation**: Horton (2023) "Homo Silicus".
- **Positioning**: We extend these by focusing on the *distribution* and *tails* of outcomes rather than just mean behavior.

## 4. Methodology: Multiverse Branching
- **Formal Framework**: 
    - LLM as a manifold $\mathcal{M}$ of human-documented behavior.
    - Conditioning $c$ (personas, scenarios) as a projection $P_c: \mathcal{M} \to \mathcal{P}(O)$.
- **Experiment 1: Distributional Baseline**:
    - Scenarios: "Mistaken Credit" social dilemma.
    - Personas: Aggressive, Passive, Strategic, Generic.
    - Sampling: 50 parallel continuations ($T>0$).
- **Experiment 2: Tail Exploration**:
    - Conditioned prompting for "Likely", "Extreme", "Submissive" outcomes.
- **Experiment 3: Cultural Grounding**:
    - Comparison of Japanese Salaryman vs. NYC Tech Founder.

## 5. Results
- **Evidence Mapping**:
    - Table 1: Distributional metrics (Directness, Harmony, Entropy) for Exp 1.
    - Figure 1: Entropy of different personas (Strategic vs. Generic).
    - Figure 2: Manifold projection showing shift from Japanese to NYC behavior.
- **Key Findings**:
    - Generic persona has lowest entropy (0.14) due to alignment-induced mode collapse.
    - Strategic persona has highest entropy (1.01).
    - Cultural personas shift factor scores (Directness, Harmony) significantly.

## 6. Discussion: Toward a Theory of Simulation
- **The LLM as a Superset**: It represents the space of all documented possibilities.
- **Alignment Bias**: How safety training creates "central tendency" and mode collapse.
- **Simulation Fidelity**: Fidelity comes from capturing latent factors (ambition, culture) rather than just surface text.
- **Limitations**: Model-specific manifolds, sample size constraints.

## 7. Conclusion
- **Summary**: LLMs are effective multiversal simulators when properly conditioned.
- **Future Work**: Black swan generation in economic systems, metrics for simulation fidelity.

## Visuals Plan
- **Table 1**: Exp 1 Results (Directness, Social Harmony, Category Entropy).
- **Figure 1**: Bar chart of Entropy across personas.
- **Figure 2**: Scatter plot of Directness vs. Social Harmony (Manifold Projection).
- **Example Listing**: Specific "tail" outcomes (e.g., the humorous Oscar joke).
