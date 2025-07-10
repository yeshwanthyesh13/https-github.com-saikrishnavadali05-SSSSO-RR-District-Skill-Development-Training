import os
import json

# In-memory "databases"
users_db = {}
scores_db = {}
quiz_db = []

# Paths to JSON files
BASE_DIR = os.path.dirname(__file__)
users_path = os.path.join(BASE_DIR , "users.json")
scores_path = os.path.join(BASE_DIR , "scores.json")

# Load users
if os.path.exists(users_path):
    with open(users_path, "r") as f:
        users_db.update(json.load(f))

# Load scores
if os.path.exists(scores_path):
    with open(scores_path, "r") as f:
        scores_db.update(json.load(f))

# Save helpers (optional)

def save_users():
    with open(users_path, "w") as f:
        json.dump(users_db, f, indent=4)

def save_scores():
    with open(scores_path, "w") as f:
        json.dump(scores_db, f, indent=4)
