class Repo:
    def __init__(self) -> None:
        pass
        

    def print_repo(self, data):
        for i in data:
            print(f"Repositry Name: {i['full_name']}")
            print(f"Clone Url: {i['clone_url']}")
            print(f"Private: {i['private']}")
            print(f"Watch Count: {i['watchers_count']}")
            print()
        