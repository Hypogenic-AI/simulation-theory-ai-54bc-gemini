# Theory of Simulation in LLMs

This project investigates whether Large Language Models (LLMs) can simulate a superset of human behavioral outcomes by capturing underlying psychological and cultural factors.

## Key Findings
- **Multiverse Generators**: LLMs naturally generate diverse outcomes (multiversal branching) even with fixed personas and scenarios.
- **Factor Sensitivity**: Simulated behaviors shift predictably and significantly when persona traits (e.g., Aggressive, Strategic) or cultural contexts (e.g., Tokyo vs. NYC) are varied.
- **Superset Traversability**: LLMs can generate "long-tail" human behaviors (unlikely but plausible) when explicitly directed, confirming they contain a superset of behavioral possibilities beyond the "likely" mode.
- **Alignment Constraint**: "Generic" personas tend to suffer from mode collapse toward safe/collaborative outcomes, a result of alignment training (RLHF).

## Project Structure
- `src/`: Python scripts for simulation and analysis.
  - `multiverse_simulator.py`: Main branching simulation script.
  - `tail_simulator.py`: Explores the "tails" of the distribution.
  - `cultural_simulator.py`: Tests cultural factor sensitivity.
  - `analyze_results.py`: Visualizes data and calculates entropy.
- `results/`: CSVs and JSONs of simulated outcomes and scores.
- `figures/`: Visualizations of the behavioral manifold.
- `REPORT.md`: Full research report.

## How to Reproduce
1.  Install dependencies: `uv pip install -r pyproject.toml`
2.  Set `OPENAI_API_KEY`.
3.  Run simulations: `python src/multiverse_simulator.py`
4.  Run tail exploration: `python src/tail_simulator.py`
5.  Run analysis: `python src/analyze_results.py`

## Theory
We propose a **Manifold-based Theory of Simulation** where LLMs represent a high-dimensional space of human-like behaviors, and prompting acts as a projection onto specific behavioral sub-manifolds.
