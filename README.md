# Pocket — Personal Context Manager CLI

A CLI tool that stores personal context snippets and uses them to give personalized AI answers.

## Setup

1. Clone or download the project

2. Install Python 3.x

3. Create a `config.py` file in the project folder:

   API_KEY = "your-groq-api-key"

   Get a free key at: console.groq.com


4. Open a terminal and cd into the project folder:
   cd Pocket_CLI


## Commands

# Add a context snippet
py pocket.py add "We use React and TypeScript"

# List all snippets
py pocket.py list

# Delete a snippet by ID
py pocket.py delete 0

# Set a snippet to public or private
py pocket.py permissions 0 private

# Query the AI using your context
py pocket.py query "How should I structure my API calls?"

## Notes
- Public snippets are sent to the AI as context
- Private snippets are stored but never sent to the AI
- config.py is not included — you must create it yourself with your own API key
