# TODO: 1) target_followers --> add output in file (+)
#       2) igtv
#       3) update
#       4) highlights
#       5) followees
#       6) bio (+)
#       7) check who followed in your account
#       8) full name (+)
#       9) create folder TARGETS and mv all targets in dir

from colorama import Fore, Style
from termcolor import cprint, colored
import instaloader
from time import sleep

auth_flag = False
inst = instaloader.Instaloader(save_metadata=False)

logo = """
  ___           _            ____
 |_ _|_ __  ___| |_ __ _    |  _ \ __ _ _ __ ___  ___ _ __
  | || '_ \/ __| __/ _` |   | |_) / _` | '__/ __|/ _ \ '__|
  | || | | \__ \ || (_| |   |  __/ (_| | |  \__ \  __/ |
 |___|_| |_|___/\__\__,_|   |_|   \__,_|_|  |___/\___|_|
"""  # noqa: W605

cprint(logo, 'cyan')


# Input targer nickname
print(Fore.GREEN + Style.BRIGHT)
target = input("Enter target username:")

# Profile
id = inst.check_profile_id(target)
profile = instaloader.Profile.from_username(inst.context, target)
full_name_target = profile.full_name
bio_target = profile.biography


# Check block
private_check = profile.is_private
verify_check = profile.is_verified
business_check = profile.is_business_account

verify = "VERIFIED" if verify_check is True else "UNVERIFIED"
privacy = "PRIVATE" if private_check is True else "UNPRIVATE"
business = "BUSINESS" if business_check is True else "FREE"

print(f"""\n{colored(target, 'red')} --> {colored(full_name_target,'red')} have
      {colored(privacy, 'red')},
      {colored(verify, 'red')},
      {colored(business, 'red')} account.""")
if business_check is True:
    business_name = profile.business_category_name
    print(f"Business name: {colored(business_name,'red')}")
if bio_target != "":
    print(f"Profile biography:\n{colored(bio_target,'red')}")
print(Fore.GREEN + Style.BRIGHT)

key = None
def auth():  # Auth in Instagra
    try:
        global key
        key = True
        username = input("Login: ")
        inst.interactive_login(username)
        return key
        
    except Exception as e:
        key = False
        print(f"Error --> {e}")
        return key
        auth()

def down_story():  # Download stories --> your profile followees (auth)
    inst.get_stories(id)
    inst.download_stories()
    for story in inst.get_stories():  # story is a Story object
        for item in story.get_items():  # item is a StoryItem object
            inst.download_storyitem(item, ':stories')


def down_avatar(target):  # Download profile picture (no auth)
    inst.download_profile(target, profile_pic_only=True,)

def down_target_stories(target):
    inst.download_profile(target, download_stories_only=True)

def down_posts(target):  # Download posts (no auth)
    for post in profile.get_posts():
        inst.download_post(post, target=target)


def target_followers():  # View target followers (auth)
    f = open(f'{target}_followers.txt', 'w+')
    followers = profile.get_followers()
    for follower in followers:
        fol = str(follower)
        print(Fore.CYAN + fol[8:-1] + Fore.GREEN)
        f.write('\n' + fol[8:-1] + '\n')
    f.close()


def general_pick():
    try:
        print(Fore.GREEN + """
 Menu:
 1)With authorization in Instagram
 2)Without authorization on Instagram
 3)All
 0)Exit
              """)

        general_choise = input("\nEnter number:").lower()
        if general_choise == "1":
            auth_pick(key)
        elif general_choise == "2":
            noauth_pick()
        elif general_choise == "3":
            auth()
            down_avatar(target)
            down_posts(target)
            down_target_stories(target)
            target_followers()
            print("\nFinish\n")
            general_pick()
        elif general_choise == "0":
            exit("Bye!")
        else:
            print(f"{Fore.RED}Wrong input!{Fore.GREEN}")
            sleep(1)
            general_pick()
    except Exception as e:
        print(f"{Fore.RED} Error! --> {e} {Fore.GREEN}")
        sleep(1)
        general_pick()


def auth_pick(key):
    try:
        if key is True:
            cprint("Auth is True",'blue')
            
        else: 
            auth()
        print("""
 1)Download stories your followes
 2)Download followers --> file
 3)Download target stories
 99)Back
 0)Exit
        """)
        auth_choise = input("\nEnter number: ").lower()
        if auth_choise == "1":
            down_story()
            auth_pick(key)
        elif auth_choise == "2":
            target_followers()
            auth_pick(key)
        elif auth_choise == "3":
            down_target_stories(target)
            auth_pick(key)
        elif auth_choise == "99":
            general_pick()
        elif auth_choise == "0":
            exit("Bye!")
        else:
            print(f"{Fore.RED}Wrong input!{Fore.GREEN}")
            sleep(1)
            auth_pick(key)

    except Exception as e:
        print(f"{Fore.RED}Error! --> {e}{Fore.GREEN}")
        sleep(1)
        general_pick()
        


def noauth_pick():
    try:
        print("""
 1)Download profile picture
 2)Download posts
 99)Back
 0)Exit
        """)
        noauth_choise = input("\nEnter number: ").lower()
        if noauth_choise == "1":
            down_avatar(target)
            noauth_pick()
        elif noauth_choise == "2":
            down_posts(target)
            noauth_pick()
        elif noauth_choise == "99":
            general_pick()
        elif noauth_choise == "0":
            exit("Bye!")
        else:
            print(f"{Fore.RED}Wrong input!{Fore.GREEN}")
            sleep(1)
            noauth_pick()
        
    except Exception as e:
        print(f"{Fore.RED}Error! --> {e}{Fore.GREEN}")
        sleep(1)
        noauth_pick()


general_pick()
