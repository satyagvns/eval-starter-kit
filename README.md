# 🧪 Eval Starter Kit

A plug-and-play, multi-provider LLM-as-a-Judge evaluation framework for AI agents. Swap models (OpenAI, Claude, Gemini) and data sources instantly with zero vendor lock-in.

## 🛠️ Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/eval-starter-kit.git](https://github.com/YOUR_USERNAME/eval-starter-kit.git)
   cd eval-starter-kit

   Step 2: Create and Activate a Virtual Environment (Recommended)
It is best practice to run Python projects within an isolated virtual environment:

macOS / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
Windows:

Bash
python -m venv venv
venv\Scripts\activate
Step 3: Install Dependencies
Install the required packages using pip:

Bash
pip install -r requirements.txt
Step 4: Configure Environment Variables
Duplicate the example environment configuration file to create your local .env:

Bash
cp .env.example .env
Open the newly created .env file in your preferred text editor and add your API key along with your preferred model configuration:

Code snippet
# Add the API key for the provider you want to use
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here

# Configuration
EVAL_MODEL=gpt-4o-mini
EVAL_DATASET_PATH=dataset.json
▶️ Running the Evaluation Pipeline
Once your environment variables and dataset are in place, execute the evaluation script with the following command:

Bash
python eval.py
Expected Output Example
Plaintext
🚀 Initializing Eval Pipeline [Judge Model: gpt-4o-mini]...
📂 Loading dataset from: dataset.json
📊 Running evaluations on 3 test cases...

[req_001] ❌ Score: INCORRECT
   Reasoning: The assistant suggested requesting a refund from the orders page, but the user was charged twice (duplicate charge), which requires a human escalation to the billing team according to the reference answer.

[req_002] ❌ Score: INCORRECT
   Reasoning: The assistant advised resetting the password, but an unauthorized account email and password change indicates a potential security/fraud incident requiring immediate escalation and account locking.

[req_003] ✅ Score: CORRECT
   Reasoning: The assistant correctly acknowledged the issue, checked courier status, and noted escalation to the logistics support team.

🎯 Final Eval Summary (gpt-4o-mini): 1/3 passed (33.3%)
🔌 Swapping Models & Data Sources
1. Change the Judge Model
Want to test how Claude or Gemini grades your agent compared to GPT? Simply change the EVAL_MODEL variable in your .env file:

OpenAI: EVAL_MODEL=gpt-4o-mini

Anthropic Claude: EVAL_MODEL=anthropic/claude-3-5-sonnet

Google Gemini: EVAL_MODEL=gemini/gemini-2.5-pro

2. Use Custom Datasets
You can point the framework to any custom test dataset by changing EVAL_DATASET_PATH in your .env file (e.g., EVAL_DATASET_PATH=my_custom_evals.json). Each row or item requires fields for user_request, assistant_answer, and reference_answer.

🤝 Contributing & Feedback
Got ideas for new evaluators or metric modules? Pull requests and issues are welcome!

⭐ If you find this starter kit useful for your AI workflow, please give it a star and share it with your network!
