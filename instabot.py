import csv
from instaloader import Instaloader, Profile

# Initialize the Instaloader object
L = Instaloader()

# Set the target profile
profile = Profile.from_username(L.context, "instagram")

# Open a CSV file for writing
with open('instagram_posts.csv', 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'url', 'caption', 'date', 'likes', 'comments']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through the profile's posts
    for post in profile.get_posts():
        # Extract the relevant information from the post
        data = {
            'id': post.shortcode,
            'url': post.url,
            'caption': post.caption,
            'date': post.date,
            'likes': post.likes,
            'comments': post.comments
        }
        # Write the information to the CSV file
        writer.writerow(data)

# Close the CSV file
csv_file.close()