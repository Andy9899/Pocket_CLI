import urllib.request
import json
from config import API_KEY
import urllib.error

#GROK
def query(question, snippets):
    # 1. build a context string from snippets
    texts = []
    for entry in snippets:
        texts.append(entry["text"])
    contextStr = "\n".join(texts)

    # 2. build the prompt
    message = (f"Here is some context about me\n"
               f"{contextStr}\n"
               f"Question: {question}"
               )

    # 3. call the API
    requestBody = {
        "model": "llama-3.1-8b-instant",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": message}]
    }
    converted_requestBody = json.dumps(requestBody).encode("utf-8")

        #building request
    built_request = urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",
                           data = converted_requestBody,
                           headers = {
                           "Content-Type": "application/json",
                           "Authorization": f"Bearer {API_KEY}",
                           "User-Agent": "pocket-cli/1.0"
                           }
    )

        #convert to python and return

    try:
        with urllib.request.urlopen(built_request) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        print(e.read().decode())