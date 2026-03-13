# kush patel
# homework 1 task 2:

def browser_simulation():
    # initialize stack and current page 
    backward_stack = []
    forward_stack = []

    current_page = "https://www.google.com"
    print("\n")
    print("Available commands: \nvisit <url>, back, forward")
    print("Type 'quit' to exit the browser simulator.\n")

# main loop for the browser simiulation 
    while True:
        try: 
            # print the current page and prompt the user for a command
            print(f"Current page: {current_page}")
            command = input("Enter a command: " ).strip()
        except EOFError:
            break
        if command.lower() == "quit":
            break

        elif command.lower().startswith("visit"):
            # split the command into parts and check if the there is a url to visit and if not then print and error message 
            parts = command.split()
            if len(parts) != 2:
                print("Ignored, Enter a URL to visit.")
                continue
            # url is considered the second part of the command 
            url = parts[1]
            # append the current page to the backward stack for the back command and clear the forward stack 
            backward_stack.append(current_page)
            current_page = url
            forward_stack.clear()
            print(f"Visited: {current_page}")
        
        elif command.lower() == "back":
            # if no backward page then print anerror message and if there is then append the current page to the forward stack and pop the backward stack to the current page
            if not backward_stack:
                print("Ignored, No previous page to go back to.")
            else: 
                forward_stack.append(current_page)
                current_page = backward_stack.pop()
                print(f"Back to: {current_page}")
        # if no forward page then print an error message and if there is then append the current page to the backward stack and pop the forward stack to the current page
        elif command.lower() == "forward":
            if not forward_stack:
                print("Ignored, No forward page available.")
            else:
                backward_stack.append(current_page)
                current_page = forward_stack.pop()
                print(f"Forward to: {current_page}")
        else: 
            #  if the command is not valid then print and error message but keep the user in teh loop to try again.
            print("Ignored, Invalid command. Please try again with a valid command.")

# driver code:
if __name__ == "__main__":
    browser_simulation()
    print("Browser simulation completed.")



