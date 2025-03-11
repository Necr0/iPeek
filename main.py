from instagrapi import Client
import instagrapi.exceptions
import time
from constants import id
import pyfiglet

print(pyfiglet.figlet_format("iPeek", font="slant"))

cl = Client()

type_query = input(f"1. Login\n2. No login [DEPRECATED]\nEnter the number of the option you want: ")

if type_query == "1":
    try:
        if not cl.login_by_sessionid(id.SESSIONID):
            print(f"[{time.strftime('%H:%M:%S')}] Login failed with Session ID, logging with username and password...")
            if not cl.login(id.USERNAME, id.PASSWORD):
                print(f"[{time.strftime('%H:%M:%S')}] Login failed. Check username and password.")
        print(f"[{time.strftime('%H:%M:%S')}] Login successful.")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Login Error: " + e)

    id.SESSIONID = cl.sessionid
    print(f"[{time.strftime('%H:%M:%S')}] Updated Session ID")

    query = input("Enter the username of the account you want to search: ")

    try:
        user = cl.user_info_by_username_v1(query)
        print(f"Username: {user.username}")
        print(f"Full name: {user.full_name}")
        print(f"Biography: {user.biography}")
        print(f"Follower count: {user.follower_count}")
        print(f"Following count: {user.following_count}")
        print(f"Media count: {user.media_count}")
        print(f"Private: {user.is_private}")
        print(f"Public email: {user.public_email}")
        print(f"Phone number: {user.public_phone_number}")
        print(f"Profile picture: \033]8;;{user.profile_pic_url}\033\\Click here\033]8;;\033\\")

    except instagrapi.exceptions.UserNotFound:
        print(f"[{time.strftime('%H:%M:%S')}] User not found.")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Error: " + e)

    input("Press enter to exit...")

elif type_query == "2":
    query = input("Enter the username of the account you want to search: ")

    try:
        user = cl.user_info_by_username_gql(query)
        print(f"Username: {user.username}")
        print(f"Full name: {user.full_name}")
        print(f"Biography: {user.biography}")
        print(f"Follower count: {user.follower_count}")
        print(f"Following count: {user.following_count}")    
        print(f"Media count: {user.media_count}")
        print(f"Private: {user.is_private}")
        print(f"Public email: {user.public_email}")
        print(f"Phone number: {user.public_phone_number}")
        print(f"Profile picture: \033]8;;{user.profile_pic_url}\033\\Click here\033]8;;\033\\")

    except instagrapi.exceptions.UserNotFound:
        print(f"[{time.strftime('%H:%M:%S')}] User not found.")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Error: " + e)

    input("Press enter to exit...")