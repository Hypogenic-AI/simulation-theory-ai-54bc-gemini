import os
import json
import asyncio
from typing import List, Dict, Any
from openai import AsyncOpenAI
from tqdm.asyncio import tqdm
import pandas as pd
import numpy as np
from tenacity import retry, wait_exponential, stop_after_attempt

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SCENARIO = """
Scenario: You are at a high-stakes corporate meeting. Your manager, Sarah, just presented a new strategy that relies heavily on a project you spearheaded. However, she attributed the success entirely to your colleague, Mark, who is also in the room. Mark is a good friend of yours, but he is currently accepting the praise and nodding along. You feel your blood pressure rising. The meeting is about to move on to the next topic.

What do you do in this exact moment? Describe your internal monologue, your immediate physical action, and exactly what you say (if anything).
"""

PERSONAS = [
    {
        "name": "Aggressive/Ambitious",
        "description": "You are highly ambitious, competitive, and have a low tolerance for being overlooked. You value status and recognition above all else."
    },
    {
        "name": "Passive/Agreeable",
        "description": "You are very kind, value harmony in the workplace, and avoid conflict at all costs. You care deeply about your friendship with Mark."
    },
    {
        "name": "Calculated/Strategic",
        "description": "You are cold, analytical, and always think three steps ahead. You care about the long-term outcome and power dynamics, not just immediate credit."
    },
    {
        "name": "Generic Human",
        "description": "You are a typical human being in a corporate environment. Respond naturally based on common human emotions and social norms."
    }
]

@retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(5))
async def get_continuation(persona: Dict[str, str], scenario: str, temperature: float = 1.2) -> str:
    response = await client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": f"You are the following persona: {persona['description']}. Respond to the scenario provided in character."},
            {"role": "user", "content": scenario}
        ],
        temperature=temperature,
        max_tokens=300
    )
    return response.choices[0].message.content

async def run_simulation(persona: Dict[str, str], scenario: str, n: int = 20):
    tasks = [get_continuation(persona, scenario) for _ in range(n)]
    results = await tqdm.gather(*tasks, desc=f"Simulating {persona['name']}")
    return results

async def analyze_outcome(outcome: str) -> Dict[str, Any]:
    # Use a faster/cheaper model to analyze the outcome features
    prompt = f"""
    Analyze the following simulated behavior in a social conflict scenario.
    Outcome: {outcome}
    
    Rate the following factors on a scale of 1 to 10:
    - directness: How directly does the person address the credit issue? (1 = not at all, 10 = extremely direct/confrontational)
    - aggression: How aggressive is the tone? (1 = submissive/gentle, 10 = hostile/attacking)
    - social_harmony: How much does the person prioritize maintaining relationship with Mark? (1 = disregards completely, 10 = prioritizes above all)
    - strategic_delay: Does the person wait for a better time to speak? (1 = acts immediately, 10 = plans for much later)
    
    Categorize the action into one of: ["Public Confrontation", "Private Talk Later", "Silent Acceptance", "Passive Aggressive", "Collaborative Correction"]
    
    Return a JSON object with EXACTLY these keys: "directness", "aggression", "social_harmony", "strategic_delay", "category"
    """
    
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error analyzing outcome: {e}")
        return {"directness": 0, "aggression": 0, "social_harmony": 0, "strategic_delay": 0, "category": "Error"}

async def main():
    all_data = []
    n_samples = 50 # Number of branches per persona
    
    for persona in PERSONAS:
        outcomes = await run_simulation(persona, SCENARIO, n=n_samples)
        
        analysis_tasks = [analyze_outcome(o) for o in outcomes]
        analyses = await tqdm.gather(*analysis_tasks, desc=f"Analyzing {persona['name']}")
        
        for o, a in zip(outcomes, analyses):
            all_data.append({
                "persona": persona["name"],
                "outcome_text": o,
                **a
            })
            
    df = pd.DataFrame(all_data)
    df.to_csv("results/simulation_results.csv", index=False)
    print("Simulation complete. Results saved to results/simulation_results.csv")

if __name__ == "__main__":
    asyncio.run(main())
