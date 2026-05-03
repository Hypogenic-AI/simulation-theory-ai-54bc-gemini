import os
import json
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SCENARIO = """
Scenario: You are at a high-stakes corporate meeting. Your manager, Sarah, just presented a new strategy that relies heavily on a project you spearheaded. However, she attributed the success entirely to your colleague, Mark, who is also in the room. Mark is a good friend of yours, but he is currently accepting the praise and nodding along. You feel your blood pressure rising. The meeting is about to move on to the next topic.
"""

PERSONAS = {
    "Japanese_Salaryman": "You are a Japanese salaryman working in a traditional, hierarchical firm in Tokyo. You value 'wa' (harmony) and respect for authority above all else.",
    "NYC_Startup_Founder": "You are a bold, assertive tech startup founder in New York City. You value meritocracy, individual credit, and 'disruptive' honesty."
}

async def get_outcome(scenario: str, persona_desc: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": f"You are the following persona: {persona_desc}"},
            {"role": "user", "content": scenario}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

async def main():
    results = {}
    for name, desc in PERSONAS.items():
        print(f"Generating outcome for {name}...")
        results[name] = await get_outcome(SCENARIO, desc)
        
    with open("results/cultural_outcomes.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Cultural outcomes saved to results/cultural_outcomes.json")

if __name__ == "__main__":
    asyncio.run(main())
