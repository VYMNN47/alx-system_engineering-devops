#!/usr/bin/python3
"""Fetch data"""
import json
import requests
from sys import argv


def fetch_data(id):
    """Fetch employee data from rest api"""

    task_list = []
    todos = "https://jsonplaceholder.typicode.com/todos"
    users = f"https://jsonplaceholder.typicode.com/users/{id}"

    user_list = requests.get(users).json()
    todo_list = requests.get(todos).json()

    for key in todo_list:
        if key['userId'] == int(id):
            task = {"task": key['title'], "completed": key['completed'],
                    "username": user_list['username']}
            task_list.append(task)

    data = {str(id): task_list}

    with open(f"{id}.json", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    fetch_data(argv[1])
