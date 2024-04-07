import tkinter as tk

def handle_input(event=None):
    chat_history.configure(state=tk.NORMAL)  # Enable editing to add text
    chat_history.insert(tk.END, "You: " + entry.get() + "\n")  # Add user input to chat history
    chat_history.configure(state=tk.DISABLED)  # Disable editing after adding text
    entry.delete(0, tk.END)  # Clear the input field

# Create a Tkinter root window
root = tk.Tk()
root.geometry("400x600") 
root.configure(bg="light gray") 

# Create a Text widget to display chat history
chat_history = tk.Text(root, height=30, width=40, state=tk.DISABLED)
chat_history.pack(side=tk.TOP, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(side=tk.BOTTOM, pady=10)

submit_button = tk.Button(root, text="Submit", command=handle_input)
submit_button.pack(side=tk.BOTTOM, pady=5)

# Bind the <Return> key event to the handle_input() function
entry.bind("<Return>", handle_input)

# Keep the window open
root.mainloop()
