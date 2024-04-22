#!/usr/bin/python3
"""Fetch data"""
import csv
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
            task_list.append([str(id), user_list['username'],
                             str(key['completed']), key['title']])

    with open(f"{id}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for row in task_list:
            writer.writerow(row)


if __name__ == "__main__":
    fetch_data(argv[1])
