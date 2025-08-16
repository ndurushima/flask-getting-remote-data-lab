import requests
import json

class GetRequester:

    def __init__(self, url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"):
        self.url = url

    def get_response_body(self, search_term):
        people = self.load_json()
        term = search_term.strip().lower()

        match = next((p for p in people if term in p.get('name', '').lower()), None)

        name = match.get('name', 'Unknown')
        occupation = match.get('occupation', 'Unknown')
        return f"Employee Name: {name}\nOccupation: {occupation}"

    def load_json(self):
        resp = requests.get(self.url)
        resp.raise_for_status()
        return json.loads(resp.text)
    
if __name__ == "__main__":
    search_term = input("Enter an employee name: ")
    result = GetRequester().get_response_body(search_term)
    print("Search Result:\n")
    print(result)