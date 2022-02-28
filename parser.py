# TODO: 1)target_followers --> add output in file +
#       2)
import colorama
from colorama import Fore, Style
from termcolor import cprint, colored
import instaloader
from time import sleep
inst = instaloader.Instaloader()
colorama.init()
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


id = inst.check_profile_id(target)
profile = instaloader.Profile.from_username(inst.context, target)

# Check block
private_check = profile.is_private
verify_check = profile.is_verified
business_check = profile.is_business_account
verify = "VERIFIED" if verify_check is True else "UNVERIFIED"
privacy = "PRIVATE" if private_check is True else "UNPRIVATE"
business = "BUSINESS" if business_check is True else "FREE"

print(f"""{colored(target, 'red')} have {colored(privacy, 'red')}
      {colored(verify, 'red')}, {colored(business, 'red')} account.""")
if business_check is True:
    business_name = profile.business_category_name
    print(f"Business name: {colored(business_name,'red')}")
print(Fore.GREEN + Style.BRIGHT)


# Auth in Instagram
def auth():
    username = input("Login: ")
    inst.interactive_login(username)

def down_story():
    inst.get_stories(id)
    inst.download_stories()
    for story in inst.get_stories():  # story is a Story object
        for item in story.get_items():  # item is a StoryItem object
            inst.download_storyitem(item, ':stories')
def down_avatar(target):  # Download Profile_picture (no auth)
    inst.download_profile(target, profile_pic_only=True,)


def down_posts(target):
    for post in profile.get_posts():
        instaloader.Instaloader(
            save_metadata=False).download_post(post, target=target)


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
        print(Fore.GREEN)
        print("""
Menu:
1)With authorization in Instagram
2)Without authorization on Instagram
0)Exit
              """)

        general_choise = input("Input number:").lower()

        if general_choise == "1":
            auth_pick()
        elif general_choise == "2":
            noauth_pick()
        elif general_choise == "0" or "exit" or "quit":
            exit("Bye!")
        else:
            print(Fore.RED + "Wrong input!"+Fore.GREEN)
            sleep(1)
            general_choise()
    except(ValueError, TypeError):
        print(Fore.RED + "Error!"+Fore.GREEN)
        sleep(1)
        general_pick()


def auth_pick():
    pass
    print("auth_pick")


def noauth_pick():
    print("noauth_pick")


'''general_pick()'''
# inst.dirname_pattern()




# down_avatar(target)
# down_posts(target)
# target_followers()
# down_posts(target)
# down_posts(target)
