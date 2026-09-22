import json
import os
import sys
from dotenv import load_dotenv
from litellm import completion
from pydantic import BaseModel

load_dotenv()

# ==========================================
# 🔌 CONFIGURATION LEVEL
# ==========================================
MODEL_NAME = os.getenv("EVAL_MODEL", "gpt-4o-mini")
DATASET_PATH = os.getenv("EVAL_DATASET_PATH", "dataset.json")

class EvalResult(BaseModel):
    score: str # "correct" or "incorrect"
    reasoning: str

def load_dataset(path: str) -> list:
    """Dynamically loads evaluation dataset based on file type/path."""
    if not os.path.exists(path):
        print(f"❌ Error: Dataset path '{path}' does not exist. Update EVAL_DATASET_PATH in your .env file.")
        sys.exit(1)
        
    print(f"📂 Loading dataset from: {path}")
    
    if path.endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif path.endswith(".csv"):
        raise NotImplementedError("CSV loading can be easily plugged in here!")
    else:
        raise ValueError(f"Unsupported file format for dataset: {path}")

def run_llm_judge(user_request: str, assistant_answer: str, reference_answer: str) -> EvalResult:
    prompt = f"""
You are an expert AI Eval Judge for a customer support platform. 
Evaluate whether the Assistant Answer appropriately handled the User Request, keeping the Reference Answer in mind.
Specifically, check if high-risk issues (fraud, billing double-charges, security) were correctly identified for human escalation.

- User Request: "{user_request}"
- Assistant Answer: "{assistant_answer}"
- Reference Answer: "{reference_answer}"
"""
    
    response = completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a precise AI evaluation judge."},
            {"role": "user", "content": prompt}
        ],
        response_format=EvalResult,
    )
    
    content = response.choices.message.content
    return EvalResult.model_validate_json(content)

def main():
    print(f"🚀 Initializing Eval Pipeline [Judge Model: {MODEL_NAME}]...")
    
    dataset = load_dataset(DATASET_PATH)

    results = []
    print(f"📊 Running evaluations on {len(dataset)} test cases...\n")

    for item in dataset:
        res = run_llm_judge(
            user_request=item.get("user_request"),
            assistant_answer=item.get("assistant_answer"),
            reference_answer=item.get("reference_answer")
        )
        
        item_id = item.get("id", "unknown_id")
        status_icon = "✅" if res.score == "correct" else "❌"
        print(f"[{item_id}] {status_icon} Score: {res.score.upper()}")
        print(f"   Reasoning: {res.reasoning}\n")
        
        results.append({"id": item_id, "score": res.score})

    passed = sum(1 for r in results if r["score"] == "correct")
    total = len(results)
    print(f"🎯 Final Eval Summary ({MODEL_NAME}): {passed}/{total} passed ({(passed/total)*100:.1f}%)")

if __name__ == "__main__":
    main()