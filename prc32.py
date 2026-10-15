import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

while True:
    print("\n===== API MANAGEMENT SYSTEM =====")
    print("1. Get all posts")
    print("2. Get a single post")
    print("3. Create a new post")
    print("4. Update a post")
    print("5. Delete a post")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()

            for post in posts[:5]:
                print("\nPost ID:", post["id"])
                print("Title:", post["title"])
                print("Body:", post["body"])

    elif choice == "2":
        post_id = input("Enter post ID: ")

        response = requests.get(url + "/" + post_id)

        if response.status_code == 200:
            post = response.json()

            print("ID:", post["id"])
            print("Title:", post["title"])
            print("Body:", post["body"])
        else:
            print("Post not found!")

    elif choice == "3":
        title = input("Enter title: ")
        body = input("Enter body: ")

        new_post = {
            "title": title,
            "body": body,
            "userId": 1
        }

        response = requests.post(url, json=new_post)

        print("Status Code:", response.status_code)
        print("Created Post:")
        print(response.json())

    elif choice == "4":
        post_id = input("Enter post ID to update: ")

        title = input("Enter new title: ")
        body = input("Enter new body: ")

        updated_post = {
            "title": title,
            "body": body,
            "userId": 1
        }

        response = requests.put(
            url + "/" + post_id,
            json=updated_post
        )

        if response.status_code == 200:
            print("Post Updated Successfully!")
            print(response.json())
        else:
            print("Update failed!")

    elif choice == "5":
        post_id = input("Enter post ID to delete: ")

        response = requests.delete(url + "/" + post_id)

        if response.status_code == 200:
            print("Post Deleted Successfully!")
        else:
            print("Delete failed!")

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice! Try again.")