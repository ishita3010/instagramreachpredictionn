import requests
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
import pickle
import numpy as np


# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

class ReachPredictionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Instagram Reach Users Prediction")

        # Set window size and position
        window_width = 600
        window_height = 400
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Set window background color
        self.window.configure(bg="#f2f2f2")

        # Create a style object
        style = ttk.Style()
        style.configure("TLabel", background="#248aa4", font=("Arial", 16))
        style.configure("TEntry", font=("Arial", 16))
        style.configure("TButton", font=("Arial", 16), background="#FFB1FF", foreground="white")

        # Create the input labels and entry fields
        label_likes = ttk.Label(self.window, text="Likes:")
        label_likes.pack()

        self.entry_likes = ttk.Entry(self.window)
        self.entry_likes.pack(pady=5)

        label_saves = ttk.Label(self.window, text="Saves:")
        label_saves.pack()
        self.entry_saves = ttk.Entry(self.window)
        self.entry_saves.pack(pady=5)

        label_comments = ttk.Label(self.window, text="Comments:")
        label_comments.pack()
        self.entry_comments = ttk.Entry(self.window)
        self.entry_comments.pack(pady=5)

        label_shares = ttk.Label(self.window, text="Shares:")
        label_shares.pack()
        self.entry_shares = ttk.Entry(self.window)
        self.entry_shares.pack(pady=5)

        label_profile_visits = ttk.Label(self.window, text="Profile Visits:")
        label_profile_visits.pack()
        self.entry_profile_visits = ttk.Entry(self.window)
        self.entry_profile_visits.pack(pady=5)

        label_follows = ttk.Label(self.window, text="Follows:")
        label_follows.pack()
        self.entry_follows = ttk.Entry(self.window)
        self.entry_follows.pack(pady=5)

        # Create the predict button
        predict_button = ttk.Button(self.window, text="Predict Reach", command=self.predict_reach)
        predict_button.pack(pady=10)

        # Create the result label
        self.result_label = ttk.Label(self.window, text="", font=("Arial", 16), background="#f2f2f2")
        self.result_label.pack()

    def predict_reach(self):
        # Get the input values
        likes = float(self.entry_likes.get())
        saves = float(self.entry_saves.get())
        comments = float(self.entry_comments.get())
        shares = float(self.entry_shares.get())
        profile_visits = float(self.entry_profile_visits.get())
        follows = float(self.entry_follows.get())

        # Perform the reach prediction
        features = np.array([[likes, saves, comments, shares, profile_visits, follows]])
        prediction = model.predict(features)

        # Display the prediction result
        self.result_label.configure(text=f"Estimated Reach: {prediction[0]}")

    def quit_app(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to quit?"):
            self.window.destroy()


# Create the main window
window = Tk()
app = ReachPredictionApp(window)
window.protocol("WM_DELETE_WINDOW", app.quit_app)
window.mainloop()
