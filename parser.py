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
#colorama.init()
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


def auth():  # Auth in Instagram
    auth_flag = True
    try:
        
        username = input(Fore.LIGHTGREEN_EX + "Login: ")
        inst.interactive_login(username)
        
    except:
        auth()

def down_story():  # Download stories (auth)
    inst.get_stories(id)
    inst.download_stories()
    for story in inst.get_stories():  # story is a Story object
        for item in story.get_items():  # item is a StoryItem object
            inst.download_storyitem(item, ':stories')


def down_avatar(target):  # Download profile picture (no auth)
    inst.download_profile(target, profile_pic_only=True,)


def down_posts(target):  # Download posts (no auth)
    for post in profile.get_posts():
        inst.download_post(post, target=target)


def target_followers():  # View target followers (auth)
    f = open(f'{target}_followers.txt', 'w+')
    followers = profile.get_followers()
    for follower in followers:
        fol = str(follower)
        print(Fore.LIGHTGREEN_EX + fol[8:-1])
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
            auth_pick(auth_flag)
        elif general_choise == "2":
            noauth_pick()
        elif general_choise == "3":
            auth()
            down_avatar(target)
            down_posts(target)
            down_story()
            target_followers()
            print("\nFinish\n")
            general_pick()
        elif general_choise == "0" or "exit" or "quit":
            exit("Bye!")
        else:
            print(Fore.RED + "Wrong input!"+Fore.GREEN)
            sleep(1)
            general_pick()
    except(ValueError, TypeError):
        print(Fore.RED + "Error!"+Fore.GREEN)
        print(Exception())
        sleep(1)
        general_pick()


def auth_pick(auth_flag):
    try:
        if auth_flag is False:
            auth_flag = True
            auth()
        else: pass
        print("""
 1)Download stories
 2)Download followers --> file
 99)Back
 0)Exit
        """)
        auth_choise = input("\nEnter number: ").lower()
        if auth_choise == "1":
            down_story()
            auth_pick()
        elif auth_choise == "2":
            target_followers()
            auth_pick()
        elif auth() == "99":
            general_pick()
            auth_pick()
        elif auth_choise == "0" or "exit" or "quit":
            exit("Bye!")
        else:
            print(Fore.RED + "Wrong input!" + Fore.GREEN)
            sleep(1)
            auth_pick()

    except(ValueError, TypeError):
        print(Fore.RED + "Error!" + Fore.GREEN)
        sleep(1)
        auth_pick()
        


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
            noauth_pick()
        elif noauth_choise == "0":
            exit("Bye!")
        else:
            print(Fore.RED + "Wrong input!" + Fore.GREEN)
            sleep(1)
            noauth_pick()
        
    except(ValueError,TypeError):
        print(Fore.RED + "Error!" + Fore.GREEN)
        sleep(1)
        noauth_pick()


general_pick()
