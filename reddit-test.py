import praw

reddit = praw.Reddit(
    client_id="<your client id>",
    client_secret="<your client secret>",
    user_agent="<your user agent>",
    username="<username>",
    password="<password>",
)


file_name = f"{reddit.user.me()}'s saved posts"
comments = []
submissions = []

with open(f"{file_name}.txt", "w+") as file:
    file.write("These are your saved posts/comments \n")

def add_to_file(file, thing_to_add):
    with open(f"{file}.txt", "a") as text_file:
        text_file.write(f"{thing_to_add}\n")

for item in reddit.user.me().saved(limit=15):
   
    is_comment = item.fullname[:2] == "t1"
    is_submission = item.fullname[:2] == "t3"

    item_url = "https://www.reddit.com" + item.permalink

    if(is_comment):
        comments.append(item_url)
    elif(is_submission):
        submissions.append(item_url)

add_to_file(file_name, "\nYour Saved Comments:")
for comment in comments:
    add_to_file(file_name, f"{comment}")

add_to_file(file_name, "\nYour Saved Posts:")
for submission in submissions:
    add_to_file(file_name, f"{submission}")
