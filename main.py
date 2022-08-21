import os
import threading
import requests
import pystyle
from pystyle import *

from itertools import cycle

Title = print("""

██╗███╗ ██╗ ██████╗████████╗ █████╗  ██████╗ ██████╗  █████╗  ███╗   ███╗        
██║████╗ ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║        
██║██╔██╗██║╚█████╗    ██║   ███████║██║  ██╗ ██████╔╝███████║██╔████╔██║        
██║██║╚████║ ╚═══██╗   ██║   ██╔══██║██║  ╚██╗██╔══██╗██╔══██║██║╚██╔╝██║        
██║██║ ╚███║██████╔╝   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║        
╚═╝╚═╝ ╚══╝╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚═╝        

 █████╗ ██╗ █████╗ 
██╔══██╗██║██╔══██╗
███████║██║██║  ██║
██╔══██║██║██║  ██║
██║  ██║██║╚█████╔╝
╚═╝  ╚═╝╚═╝ ╚════╝  """)


class Fore:
    BLACK     = "\033[30m"
    RED       = "\033[31m"
    GREEN     = "\033[32m"
    YELLOW    = "\033[33m"
    BLUE      = "\033[34m"
    MAGENTA   = "\033[35m"
    CYAN      = "\033[36m"
    WHITE     = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET     = "\033[0m"


class Choose_Cookie():

    def get_cookie():
        with open('input/cookies.txt', 'r') as f:
            cookies = [line.strip('\n') for line in f]
        return cookies
    cookie = get_cookie()
    cookies2 = cycle(cookie)
    print(cookies2)

class Convert():

    
    def get_like_id(post_id):

        headers = {
            'authority': 'www.instagram.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }

        r = requests.get(f'https://www.instagram.com/p/{post_id}/', headers=headers)
        data = r.text
        get_data = data.split('postPage_')[1]
        id = get_data.split('"')[0]
        return id


    def get_user_id(username):
        
        headers = {
            'authority': 'i.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.9',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'x-csrftoken': 'eB8F8DBi9fUrycehIas063lomgcrfwLS',
            'x-ig-app-id': '936619743392459',
        }

        params = {
            'username': username,
        }

        r = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/', params=params, headers=headers)
        data = r.text
        get_id = data.split('"id":')[1]
        id = get_id.split('"')[1]
        return id




class Follow():
    sem = threading.Semaphore(200)

    def follow(username):

        with Follow.sem:

            cookie = next(Choose_Cookie.cookies2)
            
            user_id = Convert.get_user_id(username)

            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'sessionid={cookie}',
                'origin': 'https://www.instagram.com',
                'referer': f'https://www.instagram.com/{username}/',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                'x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL',
                'x-requested-with': 'XMLHttpRequest',
            }

            r = requests.post(f'https://www.instagram.com/web/friendships/{user_id}/follow/', headers=headers)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[+] Followed{Fore.RESET} {username}\n")
            else:
                print(f"{Fore.RED}Error{Fore.RESET}\n")


    def unfollow(username):

        with Follow.sem:

            cookie = next(Choose_Cookie.cookies2)

            user_id = Convert.get_user_id(username)

            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'sessionid={cookie}',
                'origin': 'https://www.instagram.com',
                'referer': f'https://www.instagram.com/{username}/',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                'x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL',
                'x-requested-with': 'XMLHttpRequest',
            }

            r = requests.post(f'https://www.instagram.com/web/friendships/{user_id}/unfollow/', headers=headers)
            print(r.status_code)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[+] Unfollowed{Fore.RESET} {username}\n")
            else:
                print(f"{Fore.RED}Error{Fore.RESET}\n")



class Misc():

    def Like(post_id):

        cookie = next(Choose_Cookie.cookies2)

        like_id = Convert.get_like_id(post_id)

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'sessionid={cookie}',
            'origin': 'https://www.instagram.com',
            'referer': f'https://www.instagram.com/p/{post_id}/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'x-csrftoken': 'eB8F8DBi9fUrycehIas063lomgcrfwLS',
            'x-requested-with': 'XMLHttpRequest',
            }
            
        r = requests.post(f'https://www.instagram.com/web/likes/{like_id}/like/', headers=headers)
        if r.status_code == 200:
            print(f"{Fore.GREEN}[+] Liked{Fore.RESET} {post_id}\n")
        else:
            print(f"{Fore.RED}Error{Fore.RESET}\n")

    def comment(post_id, message):

        cookie = next(Choose_Cookie.cookies2)

        comment_id = Convert.get_like_id(post_id)

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.9',
            'cookie': cookie,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/p/B-448qKlHbz/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'viewport-width': '1083',
            'x-asbd-id': '198387',
            'x-csrftoken': 'kebImKHMQVjftn79AU80A0pqW4ugYOfA',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'comment_text': message,
            'replied_to_comment_id': '',
        }

        r = requests.post(f'https://www.instagram.com/web/comments/{comment_id}/add/', headers=headers, data=data)
        print(r.text)
        if r.status_code == 200:
            print(f"{Fore.GREEN}[+] Commented{Fore.RESET} {message}\n")
        else:
            print(f"{Fore.RED}Error{Fore.RESET}\n")



os.system('cls')
def menu():
    os.system(f'title Instagram Aio ^| Made by: Hazza ^| Version: v1')
    pystyle.Write.Print("""
                        ██╗███╗ ██╗ ██████╗████████╗  █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗        
                        ██║████╗ ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║        
                        ██║██╔██╗██║╚█████╗    ██║   ███████║██║  ██╗ ██████╔╝███████║██╔████╔██║        
                        ██║██║╚████║ ╚═══██╗   ██║   ██╔══██║██║  ╚██╗██╔══██╗██╔══██║██║╚██╔╝██║        
                        ██║██║ ╚███║██████╔╝   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║        
                        ╚═╝╚═╝ ╚══╝╚═════╝     ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        

                        █████╗ ██╗ █████╗ 
                        ██╔══██╗██║██╔══██╗
                        ███████║██║██║  ██║
                        ██╔══██║██║██║  ██║
                        ██║  ██║██║╚█████╔╝
                        ╚═╝  ╚═╝╚═╝ ╚════╝ """, pystyle.Colors.purple_to_blue, interval=0)



    print("")
    print("")
    print("")


    # print(f'                                            {Fore.RED}[{Fore.RESET} {Fore.BLUE}0{Fore.RESET} {Fore.RED}]{Fore.RESET} Account Generator')
    print(f'                                            {Fore.RED}[{Fore.RESET} {Fore.BLUE}1{Fore.RESET} {Fore.RED}]{Fore.RESET} Follow Bot')
    print(f'                                            {Fore.RED}[{Fore.RESET} {Fore.BLUE}2{Fore.RESET} {Fore.RED}]{Fore.RESET} Unfollow Bot')
    print(f'                                            {Fore.RED}[{Fore.RESET} {Fore.BLUE}3{Fore.RESET} {Fore.RED}]{Fore.RESET} Like Bot')
    print(f'                                            {Fore.RED}[{Fore.RESET} {Fore.BLUE}4{Fore.RESET} {Fore.RED}]{Fore.RESET} Comment Spammer')


    print("")
    print("")
    print("")


    choice = int(input(f"{Fore.GREEN} [{Fore.CYAN}?{Fore.GREEN}] Enter Choice {Fore.GREEN}> {Fore.WHITE}"))

    if choice == 1:
        username = input("Enter username > ")
        threads = input("Amount of follows > ")
        for i in range(int(threads)):
            threading.Thread(target=Follow.follow, args=(username,)).start()

    if choice == 2:
        username = input("Enter username > ")
        threads = input("Amount of follows > ")
        for i in range(int(threads)):
            threading.Thread(target=Follow.unfollow, args=(username,)).start()

    if choice == 3:
        post_id = input("Enter Post ID > ")
        threads = input("Amount of likes > ")
        for i in range(int(threads)):
            threading.Thread(target=Misc.Like, args=(post_id,)).start()

    if choice == 4:
        post_id = input("Enter Post ID > ")
        message = input("Enter message to spam > ")
        threads = input("Amount of comments > ")
        for i in range(int(threads)):
            threading.Thread(target=Misc.comment, args=(post_id, message,)).start()

menu()
