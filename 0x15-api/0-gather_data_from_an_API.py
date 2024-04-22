#!/usr/bin/python3
"""Fetch data"""
import requests
from sys import argv


def fetch_data(id):
    """Fetch employee data from rest api"""
    max_task = 0
    done_task = 0
    task_list = []
    todos = "https://jsonplaceholder.typicode.com/todos"
    users = f"https://jsonplaceholder.typicode.com/users/{id}"

    user_list = requests.get(users).json()
    todo_list = requests.get(todos).json()

    for key in todo_list:
        if key['userId'] == int(id):
            max_task += 1
            if key['completed'] is True:
                task_list.append('\t ' + key['title'])
                done_task += 1

    print("Employee {} is done with task({}/{}):".format(user_list["name"],
                                                         done_task, max_task))
    print('\n'.join(task_list))


if __name__ == "__main__":
    fetch_data(argv[1])
