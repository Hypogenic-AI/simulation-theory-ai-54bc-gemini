# Literature Review: A Theory of Simulation in Large Language Models

## Research Area Overview
The field of "simulation" using Large Language Models (LLMs) has evolved from simple text generation to the conceptualization of LLMs as **multiverse generators** and **role-players**. This research area explores whether LLMs can faithfully simulate human behavior and whether they can generate a "superset" of possible outcomes based on underlying psychological and sociological factors.

## Key Papers

### 1. Multiversal views on language models (2021)
- **Authors**: Laria Reynolds, Kyle McDonell
- **Source**: arXiv: 2102.06391
- **Key Contribution**: Conceptualizes LLMs as "multiverse generators" rather than linear text predictors.
- **Methodology**: Introduces "interpretational multiplicity" (uncertainty of the present) and "dynamic multiplicity" (uncertainty of the future).
- **Relevance**: Directly addresses the research hypothesis about simulating a superset of possible outcomes.

### 2. Role-Play with Large Language Models (2023)
- **Authors**: Murray Shanahan, Kyle McDonell, Laria Reynolds
- **Source**: arXiv: 2305.16367
- **Key Contribution**: Argues that LLMs are "simulacra" in a "superposition" of possible characters.
- **Methodology**: Uses the metaphor of role-play to explain how LLMs exhibit complex behaviors without needing to be "true" agents.
- **Relevance**: Provides the theoretical bridge between probability distributions and simulated agency.

### 3. Generative Agents: Interactive Simulacra of Human Behavior (2023)
- **Authors**: Joon Sung Park, et al.
- **Source**: arXiv: 2304.03442
- **Key Contribution**: Demonstrated a society of agents ("Smallville") that exhibits emergent social behavior.
- **Methodology**: Architecture involving a "Memory Stream", "Reflection", and "Planning".
- **Relevance**: Practical implementation of simulation theory at scale.

### 4. Large Language Models as Simulated Economic Agents: Homo Silicus? (2023)
- **Authors**: John J. Horton
- **Source**: arXiv: 2303.07064
- **Key Contribution**: Explores LLMs as computational models of humans for social science.
- **Methodology**: Running classic economic experiments on LLM "personas".
- **Relevance**: Shows how LLMs capture "underlying factors" of human behavior (economic rationality, biases).

### 5. AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents (2025)
- **Authors**: Piao, Jinghua, et al.
- **Source**: arXiv: 2502.08691
- **Key Contribution**: A framework for large-scale (city-level) simulation of generative agents.
- **Relevance**: Represents the state-of-the-art in urban and social simulation using LLMs.

## Common Methodologies
- **Role-Playing/Persona Prompting**: Assigning specific "identities" to LLMs to control behavior.
- **Memory Architectures**: Using vector databases or "memory streams" to maintain consistency.
- **Multiverse Branching**: Sampling multiple continuations from a single prompt to explore different outcomes.
- **Reflection & Planning**: Higher-order cognitive loops where agents "think" about their own past behavior.

## Evaluation Metrics
- **Believability**: Human-centered evaluation of how "real" the simulation feels.
- **Consistency**: Maintaining the persona and history over time.
- **Alignment**: How closely the simulated behavior matches real-world human data (e.g., economic experiments).

## Gaps and Opportunities
- **Superset of Outcomes**: Most current work focuses on "believable" (likely) outcomes. There is a gap in exploring the "tails" of the distribution—what are the *possible but unlikely* outcomes that an LLM can simulate?
- **Theory of Simulation**: A formal mathematical theory of what it means for a probability distribution to be a "valid" simulator of a complex system (like human society).

## Recommendations for Our Experiment
- **Dataset**: Use `PersonaHub` to generate a diverse range of starting conditions.
- **Baseline**: Use the `Homo Silicus` framework to test if LLMs capture specific behavioral factors.
- **Experiment Design**: Implement a "Multiverse" branching experiment where the same initial scenario is rolled out 100+ times to observe the "superset of outcomes".
