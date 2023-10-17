import json

def store_user(username, password, file):
  try:
    with open(file, 'r') as f:
      data = json.load(f)
  except (FileNotFoundError, json.decoder.JSONDecodeError):
    data = {}

  if any(user_data.get("username") == username for user_data in data.values()):
    print(f"Username {username} is already taken. Choose a different username.")
    return

  user_number = "User" + str(len(data) + 1)
  data[user_number] = {"username": username, "password": password}

  with open(file, 'w') as f:
    json.dump(data, f, indent=2)

  print(f"User {username} successfully registered.")

def show_users(file):
  try:
    with open(file, 'r') as f:
      data = json.load(f)

    print("Registered Users:")
    for username, user_data in data.items():
      print(f"Username: {username}, Password: {user_data['password']}")
  except (FileNotFoundError, json.decoder.JSONDecodeError):
    print("No users registered.")

def login_user(username, password, file):
  try:
    with open(file, 'r') as f:
      data = json.load(f)

    if data and username in data and data[username].get('password') == password:
      print("Login successful.")
    else:
      print("Incorrect username or password.")
  except (FileNotFoundError, json.decoder.JSONDecodeError):
    print("No users registered.")

# Register users
store_user('user1', 'password1', 'users.json')
store_user('user2', 'password2', 'users.json')

# Display information
show_users('users.json')

# Attempt to log in
login_user('user1', 'password1', 'users.json')
login_user('user3', 'password3', 'users.json')











