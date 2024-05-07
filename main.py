import tls_client
import requests
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

init()


session = tls_client.Session(

    client_identifier="chrome112",

    random_tls_extension_order=True

)

proxy = "" # FILL THIS  USER:PASS@IP:PORT ( WE ARE USING PROXIES TO AVOID RATE LIMIT ALSO FOR CAPTCHA )
api_key = "" # FCAP API KEY | you can get it from .gg/fcap

#////////////////////////////////////////////////////////////////////////////#



print(f'''
{Fore.LIGHTCYAN_EX}



            ░█████╗░██████╗░██████╗░███████╗██████╗░
            ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
            ███████║██║░░██║██║░░██║█████╗░░██████╔╝
            ██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗
            ██║░░██║██████╔╝██████╔╝███████╗██║░░██║
            ╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
            github.com/Exploited7



''')

user = input(f"{Fore.RESET}[{Fore.LIGHTBLUE_EX}INFO{Fore.RESET}] Enter Username To Add :  ")




def solveCaptcha(rqdata):
    try:
        if api_key == "" or api_key == None:
            print("Please add your FCAP api Key in the code .")
            return None
        headers = {
            'content-type': 'application/json',
            "authorization": api_key,
        }
        payload = {
            "sitekey":"a9b5fb07-92ff-493f-86fe-352a2803b3df",
            "host":"https://discord.com",
            "proxy": proxy,  
            "rqdata":rqdata
        }

        result = requests.post("https://api.fcaptcha.lol/api/createTask", headers=headers, json=payload)
        task_id = result.json()["task"]["task_id"]
        payload = {"task_id": task_id}
        while True:
            result = requests.get(f"https://api.fcaptcha.lol/api/getTaskData", headers=headers, json=payload)
            data = result.json()
            if data["task"]["state"] == "processing":
                continue
           
            capkey = data["task"]["captcha_key"]
            return capkey
    except Exception as e:
        print(F'{Fore.RESET}[{Fore.LIGHTRED_EX}FAILED{Fore.RESET}] {Fore.LIGHTBLUE_EX} Failed to solve ')
        return None

def sendFriend(token, user):
    try:


        
        headers = {
                'authority': 'discord.com',                
                'Authorization': token,
                'Cookie': '__dcfduid=f79a8b70f86511eea3ac5543e51156ec; __sdcfduid=f79a8b71f86511eea3ac5543e51156ec4a8a17ce9dab680fdf43763805212efc87fb1ce0dc8f1f297dc4c9b42d699765; _ga=GA1.1.1933564394.1712943226; OptanonConsent=isIABGlobal=false&datestamp=Fri+Apr+12+2024+19%3A33%3A47+GMT%2B0200+(Eastern+European+Standard+Time)&version=6.33.0&hosts=; _ga_YL03HBJY7E=GS1.1.1712943225.1.0.1712943232.0.0.0; __cfruid=9d8247042f51c8e3f87ad23406df0c5188426e70-1715019047; _cfuvid=.cEUQRcCnqdisFzvLoXINyVieT7jpvdCQjSibBbxaNc-1715019047584-0.0.1.1-604800000; cf_clearance=atXQAnjsUsc.bL9PHSmFkHGQnsYr8MSFuqHl36cwnVY-1715019201-1.0.1.1-DWJsXrcVBznvxDETLtKVnqDKMQ7n5X4BNxrrSn8VemLYDfKiPCpMCnbHOncxMR6wDhHSfLMFphGGU41_GL2pKw; locale=en-US; _ga_5CWMJQ1S0X=GS1.1.1715026789.3.1.1715026920.0.0.0',
                'Origin': 'https://discord.com',
                'Priority': 'u=1, i',
                'Referer': 'https://discord.com/channels/@me',
                'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==',
                'X-Debug-Options': 'bugReporterEnabled',
                'X-Discord-Locale': 'en-US',
                'X-Discord-Timezone': 'Africa/Cairo',
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tL2NoYW5uZWxzL0BtZSIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTA5OTgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0='
            }

        Fget = session.get('https://discord.com/api/v9/users/@me',headers=headers)

        if Fget.status_code == 200 or Fget.status_code == 204:
            userID = int(Fget.json()['id'])
            Sget = session.get(f'https://discord.com/api/v9/users/{userID}/profile?with_mutual_guilds=true&with_mutual_friends=true&with_mutual_friends_count=false',headers=headers)
            
            username = Sget.json()['user']['username']
            
            response = session.post("https://discord.com/api/v9/users/@me/relationships",headers=headers,json={
                'discriminator': None,
                'username': user
            })
            if response.status_code == 200 or response.status_code == 204 :
                    print(F"{Fore.RESET}[{Fore.LIGHTGREEN_EX}SUCCESS{Fore.RESET}] {Fore.LIGHTBLUE_EX} Added , {Fore.LIGHTBLACK_EX} Username = {username} ")
            elif response.status_code == 400:
                print(f"{Fore.RESET}[{Fore.LIGHTRED_EX}CAPTCHA{Fore.RESET}] {Fore.LIGHTBLUE_EX} Captcha Required , {Fore.LIGHTBLACK_EX} Username = {username}")
                capkey = solveCaptcha(response.json()['captcha_rqdata'])
                headers['X-Captcha-Key'] = capkey
                headers['X-Captcha-Rqtoken'] = response.json()['captcha_rqtoken']
                response2 = session.post("https://discord.com/api/v9/users/@me/relationships",headers=headers,json={
                    'discriminator': None,
                    'username': user
                })
                if response2.status_code == 204 or response2.status_code == 200 :
                    print(F"{Fore.RESET}[{Fore.LIGHTGREEN_EX}SUCCESS{Fore.RESET}] {Fore.LIGHTBLUE_EX} Added , {Fore.LIGHTBLACK_EX} Username = {username} ")
                else:
                    print(F'{Fore.RESET}[{Fore.LIGHTRED_EX}FAILED{Fore.RESET}] {Fore.LIGHTBLUE_EX} Adding failed after solving captcha, with status code : ',{response2.status_code})
            elif response.status_code == 429:
                print("RateLimit !")
            elif response.status_code == 401 : 
                    print(F'{Fore.RESET}[{Fore.LIGHTRED_EX}FAILED{Fore.RESET}] {Fore.LIGHTBLUE_EX} incorrect token. ',{response.status_code})
        elif Fget.status_code == 401 :
            print(F'{Fore.RESET}[{Fore.LIGHTRED_EX}FAILED{Fore.RESET}] {Fore.LIGHTBLUE_EX} incorrect token. ')
        else:
            print()
    except Exception as e :
        print("hi")

def process_tokens(tokens_file):
    with open(tokens_file, 'r') as file:
        tokens = file.readlines()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for token in tokens:
            token = token.strip()  
            executor.submit(sendFriend, token, user)

if __name__ == "__main__":
    tokens_file = "tokens.txt"  
    process_tokens(tokens_file)
