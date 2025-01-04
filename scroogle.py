import scratchattach as scratch
import os

# List of Scratch usernames
usernames = [
    "griffpatch", "Will_Wam", "WazzoTV", "ceebee", "griffpatch_tutor", "ScratchCat*", 
    "Hobson-TV", "Dhilly", "-BoyMcBoy-", "sharkyshar", "FunnyAnimatorJimTV", 
    "atomicmagicnumber", "theChAOTiC", "huntedskelly", "Scratchteam*", "ipzy", 
    "Rosyda", "yunnie2005", "kevin_eleven_1234", "Sterlon", "PotatoAnimator", 
    "TNTsquirrel", "scratchU8", "-Cinematic-", "Silvershimmer43", "JWhandle", 
    "7Sofa", "moss-shadow", "GoldenEagleStudios", "berricake", "MJM3", "FUZZIE-WEASEL", 
    "ToadfanSchool", "potatobear616", "CrystalKeeper7", "TurboKitten", "nednilclan", 
    "awesomeal82", "World_Languages", "Astro947", "-TheGreenNinja-", "MistCat", 
    "-SkyStar-", "Wildflight", "bear123bear456", "StratfordJames", "speakvisually", 
    "TimMcCool", "Coltroc", "Leilani", "-Rocket-", "cartoonnetwork", "Blazeheart", 
    "Paddle2see*", "ivypool2", "warframe", "Lionclaw", "_MistyLight_", "FUNUT", 
    "creeperkizi", "ThePancakeMan", "D_i_a_v_l_o", "Brad-Games", "Moonpaw12345", 
    "WO997", "DarkLava", "ExperienceSea", "nekopyon", "RedCuzImAwesome", "SharkyPup", 
    "RememberNovember", "alphabetica", "ScratchStang", "Pickle-Productions", "-AmberKitti", 
    "kewl999", "x__0", "pandakun", "jackol1234567", "-PhantomAnimations-", "Artisticat", 
    "bubble103", "lightblue012", "0014049", "cutupuss", "scmbl*", "RacingHans", 
    "Za-Chary*", "PetalsSilversteam", "Canarysong", "ScratchDesignStudio", "AnaniAnime", 
    "xamuil2", "Yllie", "FaceOs", "amee-", "QuaXX", "gobo", "Eloctrasyd"
]

# Output files
titles_file = "project_titles.txt"
ids_file = "project_ids.txt"
usernames_file = "usernames.txt"
loves_file = "loves.txt"

# Clear existing files
for file in [titles_file, ids_file, usernames_file, loves_file]:
    open(file, "w").close()

# To store all projects
projects_data = []

# Function to fetch projects for a user
def get_user_projects(username):
    try:
        # Create a User object
        user = scratch.get_user(username)

        # Fetch projects from the user's profile
        projects = user.projects()

        # Add each project's data to the list
        for project in projects:
            projects_data.append({
                "username": username,
                "title": project.title,
                "id": project.id,
                "loves": project.loves
            })

    except Exception as e:
        print(f"Error fetching projects for {username}: {e}")

# Fetch projects for all users
for username in usernames:
    print(f"Fetching projects for {username}...")
    get_user_projects(username)

# Sort all project data by loves
projects_data.sort(key=lambda x: x["loves"], reverse=True)

# Write sorted data to respective files
with open(titles_file, "w") as titles, open(ids_file, "w") as ids, open(usernames_file, "w") as usernames, open(loves_file, "w") as loves:
    for project in projects_data:
        titles.write(f"{project['title']}\n")
        ids.write(f"{project['id']}\n")
        usernames.write(f"{project['username']}\n")
        loves.write(f"{project['loves']}\n")

print(f"Project titles saved to {titles_file}")
print(f"Project IDs saved to {ids_file}")
print(f"Usernames saved to {usernames_file}")
print(f"Loves data saved to {loves_file}")
