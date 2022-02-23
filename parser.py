import instaloader


target = input("Enter target username:")
inst = instaloader.Instaloader()
#inst.download_profile(username,profile_pic=True,download_stories=True,)
id = inst.check_profile_id(target)
#inst.dirname_pattern()
username = input("Login: ")

#inst.two_factor_login(two_factor_code)

inst.interactive_login(username)

#inst.get_stories(id)
#inst.download_stories()
'''
for story in inst.get_stories():
    # story is a Story object
    for item in story.get_items():
        # item is a StoryItem object
        inst.download_storyitem(item, ':stories')
'''

