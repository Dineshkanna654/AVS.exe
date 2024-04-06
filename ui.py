import tkinter as tk

def handle_input(event=None):  # Modified to accept an event argument
    input_text = entry.get()
    chat_history.insert(tk.END, "You: " + input_text + "\n")  # Add user input to chat history
    entry.delete(0, tk.END)  # Clear the input field

# Create a Tkinter root window
root = tk.Tk()
root.geometry("400x600") 
root.configure(bg="light gray") 

# Create a Text widget to display chat history
chat_history = tk.Text(root, height=2, width=2)
chat_history.pack(side=tk.TOP, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(side=tk.BOTTOM, pady=10)

submit_button = tk.Button(root, text="Submit", command=handle_input)
submit_button.pack(side=tk.BOTTOM, pady=5)

# Bind the <Return> key event to the handle_input() function
entry.bind("<Return>", handle_input)

# Keep the window open
root.mainloop()
