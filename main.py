users:list= [
    {'name': 'Julia', 'location': 'Ząbki', 'paste': 10},
    {'name': 'Julia', 'location': 'Sokółka', 'paste': 20},
    {'name': 'Klaudia', 'location': 'Warszawa', 'paste': 15},
    {'name': 'Marcin', 'location': 'Grudziądz', 'paste': 1000},
    {'name': 'Mateusz', 'location': 'Lublin', 'paste': 100},
]




def get_user_info(users_data)->None:
    for user in users_data:
        print(f'Twój znajomy  {user["name"]} z miejscowości {user["paste"]}')

print(f'Witaj {users[0]["name"]}')
get_user_info(users[1:])