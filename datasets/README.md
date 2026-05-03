# Downloaded Datasets

This directory contains samples and instructions for datasets used in the simulation theory research.

## Dataset 1: PersonaHub
- **Source**: [proj-persona/PersonaHub](https://huggingface.co/datasets/proj-persona/PersonaHub)
- **Size**: Full dataset is large; 100 samples saved in `datasets/PersonaHub/samples.json`.
- **Use Case**: Seeding simulations with diverse human-like personas to test the "superset of outcomes".

**Download Instructions:**
```python
from datasets import load_dataset
ds = load_dataset("proj-persona/PersonaHub", "instruction")
```

## Dataset 2: Reddit Confessions
- **Source**: [SocialGrep/one-million-reddit-confessions](https://huggingface.co/datasets/SocialGrep/one-million-reddit-confessions)
- **Size**: 100 samples saved in `datasets/reddit_confessions/samples.json`.
- **Use Case**: Providing realistic "human behavior" starting points or ground truth for behavior modeling.

**Download Instructions:**
```python
from datasets import load_dataset
ds = load_dataset("SocialGrep/one-million-reddit-confessions")
```

## Git Policy
Large data files are excluded via `.gitignore`. Only samples and documentation are tracked.
