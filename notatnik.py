class user:
    def __init__(self, name, surname, location, posts):
        self.name=name
        self.surname=surname
        self.location=location
        self.posts=posts

user_1=user(name="Kinga", surname="Kłos", location="Kozienice", posts="100")
user_2=user(name="Magdalena", surname="Malinowska", location="Siemiatycze", posts="200")

print(user_1.name, user_1.surname, user_1.location, user_1.posts)
print(user_2.name, user_2.surname, user_2.location, user_2.posts)

def get_coordinates(self)->list:
    import requests
    from bs4 import BeautifulSoup
    adres url: str = f'https://pl.wikipedia.org/wiki/self.location)'
    response_html =BeautifulSoup(requests.get(adres_url))
