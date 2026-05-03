import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def analyze():
    df = pd.read_csv("results/simulation_results.csv")
    
    # Set the style
    sns.set_theme(style="whitegrid")
    
    # 1. Distribution of Categories by Persona
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x="persona", hue="category")
    plt.title("Distribution of Action Categories by Persona")
    plt.legend(title="Action Category", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig("figures/action_distribution.png")
    
    # 2. Scatter Plot of Directness vs Social Harmony
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="directness", y="social_harmony", hue="persona", style="persona", s=100, alpha=0.7)
    plt.title("Multiverse Manifold: Directness vs Social Harmony")
    plt.savefig("figures/multiverse_manifold.png")
    
    # 3. Aggression vs Strategic Delay
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="aggression", y="strategic_delay", hue="persona", s=100, alpha=0.7)
    plt.title("Multiverse Manifold: Aggression vs Strategic Delay")
    plt.savefig("figures/aggression_vs_delay.png")

    # 4. Entropy calculation (Diversity of outcomes)
    def calculate_entropy(series):
        counts = series.value_counts()
        probs = counts / len(series)
        return -np.sum(probs * np.log2(probs))

    entropy_results = df.groupby("persona")["category"].apply(calculate_entropy)
    print("\nBehavioral Entropy (Outcome Diversity) by Persona:")
    print(entropy_results)
    
    # 5. Summary Statistics
    summary = df.groupby("persona")[["directness", "aggression", "social_harmony", "strategic_delay"]].mean()
    print("\nAverage Factor Scores by Persona:")
    print(summary)
    
    # Save entropy results to a file
    entropy_results.to_csv("results/entropy_results.csv")
    summary.to_csv("results/summary_statistics.csv")

if __name__ == "__main__":
    analyze()
