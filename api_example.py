import requests

def get_user_data(user_id):
    """Get user data from JSONPlaceholder API"""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

def create_post(title, body, user_id):
    """Create a new post using JSONPlaceholder API"""
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(url, json=data)
    
    if response.status_code == 201:
        return response.json()
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    # Example GET request
    print("Getting user data...")
    user = get_user_data(1)
    print(f"User: {user['name']}")
    
    # Example POST request
    print("\nCreating a post...")
    new_post = create_post(
        "Learning APIs",
        "This is a test post about learning to use HTTP APIs with Python",
        1
    )
    print(f"Created post with ID: {new_post['id']}")
