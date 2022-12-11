import os
import threading
import time
import pystyle
import requests

from colorama import Fore
from itertools import cycle


class Misc:
    def __init__(self):
        pass

    def get_cookie():
        with open('data/cookies.txt', 'r') as f:
            cookies = [line.strip('\n') for line in f]
        return cookies
     
    cookie = get_cookie()
    ilit_cookies = cycle(cookie)




class aio:
    def __init__(self):
        self.session = requests.Session()

    def get_id(self, username):
        try:
            headers = {'authority': 'i.instagram.com','accept': '*/*','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL','x-ig-app-id': '936619743392459',}
            params = {'username': username,}
            r = self.session.get('https://i.instagram.com/api/v1/users/web_profile_info/', params=params, headers=headers)
            return r.text.split('"id":"')[2].split('"')[0]
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} User does not exist")

            
    def get_post(self, post_id):
        try:
            headers = {'authority': 'www.instagram.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-GB,en;q=0.9','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',}
            response = self.session.get(f'https://www.instagram.com/p/{post_id}/', headers=headers).text
            return response.split('postPage_')[1].split('"')[0]
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Post does not exist")

    def follow(self, user_id):
        try:
            cookie = next(Misc.ilit_cookies)
            headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','cookie': f'sessionid={cookie}','origin': 'https://www.instagram.com','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL','x-requested-with': 'XMLHttpRequest',}

            r = self.session.post(f'https://www.instagram.com/web/friendships/{user_id}/follow/', headers=headers)
            if r.status_code == 200:
                print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Successfully Followed")
            else:
                print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")

    def unfollow(self, user_id):
        try:
            cookie = next(Misc.ilit_cookies)
            headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','cookie': f'sessionid={cookie}','origin': 'https://www.instagram.com','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL','x-requested-with': 'XMLHttpRequest',}

            r = self.session.post(f'https://www.instagram.com/web/friendships/{user_id}/unfollow/', headers=headers)
            if r.status_code == 200:
                print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Successfully Unfollowed")
            else:
                print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")

    def like(self, postID):
        try:
            cookie = next(Misc.ilit_cookies)
            headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'en-GB,en;q=0.9','content-type': 'application/x-www-form-urlencoded','cookie': f'sessionid={cookie}','origin': 'https://www.instagram.com','referer': f'https://www.instagram.com/p/{postID}/','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-csrftoken': 'eB8F8DBi9fUrycehIas063lomgcrfwLS','x-requested-with': 'XMLHttpRequest',}
            
            r = self.session.post(f'https://www.instagram.com/web/likes/{postID}/like/', headers=headers)
            if r.status_code == 200:
                print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Successfully Liked Post")
            else:
                print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")
    
    def comment(self, postID, message):
        try:
            cookie = next(Misc.ilit_cookies)
            headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'en-GB,en;q=0.9','cookie': f'sessionid={cookie}','origin': 'https://www.instagram.com','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','viewport-width': '1083','x-asbd-id': '198387','x-csrftoken': 'kebImKHMQVjftn79AU80A0pqW4ugYOfA','x-requested-with': 'XMLHttpRequest',}
            data = {'comment_text': message, 'replied_to_comment_id': '',}

            r = requests.post(f'https://www.instagram.com/web/comments/{postID}/add/', headers=headers, data=data)
            if r.status_code == 200:
                print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Successfully Added Comment")
            else:
                print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")
            
class menu:
    def __init__(self):
        pass

    def main(self):
        os.system('cls')
        os.system(f'title Instagram Aio ^| Developed by: github.com/Hazza3100')
        pystyle.Write.Print("""
            ██╗███╗ ██╗ ██████╗████████╗  █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    █████╗ ██╗ █████╗ 
            ██║████╗ ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    ██╔══██╗██║██╔══██╗
            ██║██╔██╗██║╚█████╗    ██║   ███████║██║  ██╗ ██████╔╝███████║██╔████╔██║    ███████║██║██║  ██║
            ██║██║╚████║ ╚═══██╗   ██║   ██╔══██║██║  ╚██╗██╔══██╗██╔══██║██║╚██╔╝██║    ██╔══██║██║██║  ██║
            ██║██║ ╚███║██████╔╝   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║    ██║  ██║██║╚█████╔╝
            ╚═╝╚═╝ ╚══╝╚═════╝     ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝ ╚════╝""", pystyle.Colors.purple_to_blue, interval=0)
        
        print("")
        print("")

        print(f'                                     {Fore.RED}[{Fore.RESET} {Fore.BLUE}1{Fore.RESET} {Fore.RED}]{Fore.RESET} Follow Module  {Fore.RED} [{Fore.RESET} {Fore.BLUE}2{Fore.RESET} {Fore.RED}]{Fore.RESET} Unfollow Module')
        print(f'                                     {Fore.RED}[{Fore.RESET} {Fore.BLUE}3{Fore.RESET} {Fore.RED}]{Fore.RESET} Like Module    {Fore.RED} [{Fore.RESET} {Fore.BLUE}4{Fore.RESET} {Fore.RED}]{Fore.RESET} Comment Spammer')


        print("")
        print("")
        print("")
        choice = int(input(f"{Fore.GREEN} [ {Fore.CYAN}?{Fore.GREEN} ] Enter Choice {Fore.GREEN}> {Fore.WHITE}"))  


        if choice == 1:
            username = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Username {Fore.CYAN}> {Fore.WHITE}")
            threads = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Number of follows {Fore.CYAN}> {Fore.WHITE}")
            user_id = aio.get_id(username)

            for i in range(int(threads)):
                threading.Thread(target=aio().follow, args=(user_id,)).start()

        if choice == 2:
            username = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Username {Fore.CYAN}> {Fore.WHITE}")
            threads = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Number of unfollows {Fore.CYAN}> {Fore.WHITE}")
            user_id = aio.get_id(username)

            for i in range(int(threads)):
                threading.Thread(target=aio().unfollow, args=(user_id,)).start()

        if choice == 3:
            postID = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Post ID {Fore.CYAN}> {Fore.WHITE}")
            threads = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Number of Likes {Fore.CYAN}> {Fore.WHITE}")
            post_ID = aio.get_post(postID)
            for i in range(int(threads)):
                threading.Thread(target=aio().like, args=(post_ID,)).start()

        if choice == 4:
            postID = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Post ID {Fore.CYAN}> {Fore.WHITE}")
            message = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Message {Fore.CYAN}> {Fore.WHITE}")
            threads = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Number of comments {Fore.CYAN}> {Fore.WHITE}")
            post_ID = aio.get_post(postID)

            for i in range(int(threads)):
                threading.Thread(target=aio().comment, args=(post_ID, message,)).start()
        



x = menu()
x.main()
