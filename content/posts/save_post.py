import os
import sys

def get_next_file_number(directory):
    """
    Get the next file number based on existing .md files in the directory.
    """
    files = os.listdir(directory)
    md_files = [f for f in files if f.endswith('.md') and f[:-3].isdigit()]
    if not md_files:
        return 1  # If no .md files are found, start with 1.md
    numbers = [int(f[:-3]) for f in md_files]
    return max(numbers) + 1

def save_new_post(directory, content):
    """
    Save the new post content in a new file with the next number.
    """
    next_number = get_next_file_number(directory)
    new_filename = f"{next_number}.md"
    new_filepath = os.path.join(directory, new_filename)
    
    with open(new_filepath, 'w') as file:
        file.write(content)
    
    print(f"New blog post saved as {new_filename}")

if __name__ == "__main__":
    # Directory where the blog posts are stored
    directory = '/Users/NPatriciello/Work/nat.onthewifi.net/content/posts'
    
    # Read the new blog post content from stdin
    new_post_content = sys.stdin.read()
    
    # Save the new post
    save_new_post(directory, new_post_content)

