from requests import get
from requests.auth import HTTPBasicAuth

password = "password"

leet_chars = {"a": {"@"}, "s": {"5"}, "o": {"0"}}

permutations = [""] 

for char in password:
    temp: list[str] = []
    options = []

    if not char.isalpha():
        options.append(char)
    else:
        options.append(char.lower())
        options.append(char.upper())
        if char in leet_chars:
            for value in leet_chars.get(char):
                options.append(value)

    for word in permutations:
        for option in options:
            temp.append(word + option)

    permutations = temp


for password in permutations:
    basic = HTTPBasicAuth(username="John", password=password)
    response = get(
        "http://recruitment.warpdevelopment.co.za/api/authenticate", auth=basic
    )
    print(response.text)
    if response.status_code == 200:
        break
