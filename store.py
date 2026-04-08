import json
from pathlib import Path


class SnippetStore:
    def __init__(self):
        # hint: use pathlib to define where library.json lives
        self.file = Path(__file__).parent / 'library.json'

        snippets = self._load()
        self.next_id = max([s['keyID'] for s in snippets], default=-1) + 1
        self.permission = 'public'

    def add(self, text):
        # hint: load existing snippets, append a new one, save
        currentList = self.list_all()
        currentList.append({
            'keyID': self.next_id,
            'text': text,
            'permission': self.permission
        })
        self.next_id += 1
        self._save(currentList)

    def list_all(self):
        # hint: load and return all snippets
        return self._load()

    def delete(self, snippet_id):
        # hint: load, remove the one matching the id, save
        currentList = self.list_all()
        for entry in currentList:
            if entry['keyID'] == snippet_id:
                currentList.remove(entry)
        self._save(currentList)

    def _load(self):
        # hint: read library.json, return [] if it doesn't exist yet
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return []

    def _save(self, snippets):
        with open(self.file, 'w') as f:
            json.dump(snippets, f, indent = 4)

    def set_permission(self, snippet_ID, permission):
        currentList = self.list_all()
        for entry in currentList:
            if entry['keyID'] == snippet_ID:
                entry['permission'] = permission
        self._save(currentList)


