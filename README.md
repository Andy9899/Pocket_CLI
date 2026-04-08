# Pocket_CLI
“Pocket is a CLI tool that stores your personal or company context and automatically prepends relevant snippets to AI queries for personalized answers.”

# Installation
git clone <your-repo-url>
cd Pocket_CLI
pip install -r requirements.txt
export GROQ_API_KEY=your_key_here
Usage

#Run the CLI:
python pocket.py <command> <value> [extra]
Commands
add — Add a snippet:
python pocket.py add "My company uses React and TypeScript"

list — List all snippets:
python pocket.py list

delete — Delete a snippet by ID:
python pocket.py delete 1

query — Query AI with relevant snippets:
python pocket.py query "How should I structure my API calls?"

permissions — Set snippet permissions (public/private):
python pocket.py permissions 1 private
**IF PRIVATE THE AI WILL NOT BE ABLE TO ACCESS YOUR INFORMATION FOR THAT KEYID**

Example Flow
python pocket.py add "Our API rate limit is 1000 req/min"
python pocket.py add "Frontend uses TypeScript"
python pocket.py query "How should I handle API errors?"
# Returns AI response with relevant snippets automatically included
