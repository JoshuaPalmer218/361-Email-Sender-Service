import requests


def test():
    url = "http://127.0.0.1:8070/send_email"
    data = {
        "subject": "Hello World",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "receiver_email": "joshguy678@gmail.com"
    }
    response = requests.post(url, json=data)
    print(response.text)


if __name__ == '__main__':
    test()
