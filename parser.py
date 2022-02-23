# TODO: 1)target_followers --> add output in file
#       2)

import instaloader
inst = instaloader.Instaloader()


# Input targer nickname
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

print(f"{target} have {privacy},{verify},{business} account.")
if business_check is True:
    business_name = profile.business_category_name
    print(f"Business name: {business_name}")


# Auth in Instagram
'''
username = input("Login: ")
inst.interactive_login(username)
'''


def down_avatar(target):  # Download Profile_picture (no auth)
    inst.download_profile(target, profile_pic_only=True,)


def down_posts(target):
    for post in profile.get_posts():
        instaloader.Instaloader(
            save_metadata=False).download_post(post, target=target)


def target_followers():  # View target followers (auth)
    followers = profile.get_followers()
    for follower in followers:
        print(follower)


# def down_posts(target):
#   inst.download_post(~~~~~~~~~~)


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
# target_followers()
#down_posts(target)
