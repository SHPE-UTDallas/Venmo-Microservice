from venmo_api import Client


def main():
    # Get venmo username and password from the user
    username = input('Please enter your venmo username: ')
    password = input('Please enter your venmo password: ')

    # Use the venmo api client to get an access token for the user
    access_token = Client.get_access_token(username=username, password=password)

    print(f'\n\nAdd this line to your .env file:\nVENMO_ACCESS_TOKEN={access_token}')


if __name__ == '__main__':
    main()
