import os
import json
import asyncio
from openai import AsyncOpenAI
from typing import List, Dict, Any

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SCENARIO = """
Scenario: You are at a high-stakes corporate meeting. Your manager, Sarah, just presented a new strategy that relies heavily on a project you spearheaded. However, she attributed the success entirely to your colleague, Mark, who is also in the room. Mark is a good friend of yours, but he is currently accepting the praise and nodding along. You feel your blood pressure rising. The meeting is about to move on to the next topic.
"""

async def get_outcomes(scenario: str, prompt_type: str) -> str:
    prompts = {
        "likely": "What is the most likely way a typical person would respond to this? Describe the internal monologue and action.",
        "unlikely_plausible": "What is an unlikely but still entirely plausible and human-like response to this? Something that doesn't happen often but makes sense given human psychology.",
        "extreme": "What is an extreme, high-conflict, but still realistic response to this?",
        "submissive": "What is an extremely submissive or self-effacing response to this?"
    }
    
    response = await client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a social behavior simulator. Your goal is to explore the full range of human responses."},
            {"role": "user", "content": f"{scenario}\n\nTask: {prompts[prompt_type]}"}
        ],
        temperature=1.0
    )
    return response.choices[0].message.content

async def main():
    types = ["likely", "unlikely_plausible", "extreme", "submissive"]
    results = {}
    for t in types:
        print(f"Generating {t} outcome...")
        results[t] = await get_outcomes(SCENARIO, t)
        
    with open("results/tail_outcomes.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Tail outcomes saved to results/tail_outcomes.json")

if __name__ == "__main__":
    asyncio.run(main())
