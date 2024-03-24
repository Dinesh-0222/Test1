from queue import LifoQueue
backward_history=LifoQueue()
forward_history=LifoQueue()
current_pages = None
#Visit function
NoOfVisits = int(input("Enter the number of url visit: "))
print("Enter URLs to visit: ")
for i in range(NoOfVisits):
          url = input("URL: ")
          print(f"Visiting....{url}")
          backward_history.put(current_pages)
          current_pages = url
#display
print(f"Current_page : {current_pages}")
#go backward
while input("Do you want to go back? (yes/no): ").lower() =='yes':
          if not backward_history.empty():
                    forward_history.put(current_pages)
                    current_pages = backward_history.get()
                    print(f"Going back to.......{current_pages}")
          else:
                    print("No previous page available")
#go forward
while input("Do you want to go forward: (yes/no): ").lower() =="yes":
          if not forward_history.empty():
                    backward_history.put(current_pages)
                    current_pages =forward_history.get(current_pages)
                    print(f"Going forward to.......{current_pages}")
          else:
                    print("No forward page available")
                    