from store import SnippetStore
from AI_client import query
import argparse

parser = argparse.ArgumentParser()
store = SnippetStore()

parser.add_argument("command", choices=["add", "list", "delete", "query", "permissions"])
parser.add_argument("value", nargs = "?")
parser.add_argument("extra", nargs="?")  # for the second value permissions

args = parser.parse_args()

if args.command == "add":
    store.add(args.value)
    print(f"✓ Snippet added")

elif args.command == "list":
    snippets = store.list_all()
    if not snippets:
        print("No snippets yet. Use: python pocket.py add \"your context\"")
    else:
        for s in snippets:
            print(f"[{s['keyID']}] ({s['permission']}) {s['text']}")

elif args.command == "delete":
    store.delete(int(args.value))
    exists = any(ID.get("keyID") == args.value for ID in store.list_all())
    if exists:
        print(f"❌ Snippet deleted")
        pass
    else: print(f"Wrong ID or Snippet does not exist")


elif args.command == "query":
    public = [s for s in store.list_all() if s["permission"] == "public"]
    result = query(args.value, public)
    print(result["choices"][0]["message"]["content"])

elif args.command == "permissions":
    store.set_permission(int(args.value), args.extra)
    print(f"{args.value} permission set to {args.extra}")

