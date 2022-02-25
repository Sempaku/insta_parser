# TODO: 1)target_followers --> add output in file +
#       2)
import colorama
from colorama import Fore, Style, Back
from termcolor import cprint, colored
import instaloader
inst = instaloader.Instaloader()
colorama.init()
logo = """
  ___           _            ____
 |_ _|_ __  ___| |_ __ _    |  _ \ __ _ _ __ ___  ___ _ __
  | || '_ \/ __| __/ _` |   | |_) / _` | '__/ __|/ _ \ '__|
  | || | | \__ \ || (_| |   |  __/ (_| | |  \__ \  __/ |
 |___|_| |_|___/\__\__,_|   |_|   \__,_|_|  |___/\___|_|
"""

cprint(logo, 'cyan')

# Input targer nickname
print(Fore.BLUE + Style.BRIGHT)
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

print(f"{colored(target,'red')} have {colored(privacy,'red')},{colored(verify,'red')},{colored(business,'red')} account.")
if business_check is True:
    business_name = profile.business_category_name
    print(f"Business name: {colored(business_name,'red')}")
print(Fore.BLUE + Style.BRIGHT)


# Auth in Instagram

username = input("Login: ")
inst.interactive_login(username)


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
<<<<<<< HEAD
        print(follower)



=======
        fol = str(follower)
        print(Fore.LIGHTGREEN_EX + fol[8:-1])
        f.write('\n' + fol[8:-1] + '\n')
    f.close()
>>>>>>> be1a8cb18a3421da79c091b27946a4c00ee53cdc


# inst.dirname_pattern()


# inst.get_stories(id)
# inst.download_stories()
# for story in inst.get_stories():
#    # story is a Story object
#    for item in story.get_items():
#        # item is a StoryItem object
#        inst.download_storyitem(item, ':stories')
#
# down_avatar(target)
# down_posts(target)
target_followers()
# down_posts(target)
