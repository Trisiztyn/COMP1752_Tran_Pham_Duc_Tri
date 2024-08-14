import tkinter as tk
import video_library as lib  # Import the video library module

class UpdateVideo:
    def __init__(self, window):
        # Set the window dimensions and title
        window.geometry("600x300")
        window.title("Video Update Tool")

        # Set the background color of the window to a neutral tone
        window.configure(bg="#F0F0F0")

        # Create a label for entering the video ID
        video_id_lbl = tk.Label(window, text="Video ID:", bg="#C0C0C0")
        video_id_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="E")

        # Create an entry field for the video ID
        self.video_id_entry = tk.Entry(window, width=10)
        self.video_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create a label for entering the new rating
        rating_lbl = tk.Label(window, text="New Rating:", bg="#FFC080")
        rating_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="E")

        # Create an entry field for the new rating
        self.rating_entry = tk.Entry(window, width=10)
        self.rating_entry.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # Create a button to update the video information
        update_video_btn = tk.Button(window, text="Update Video Info", command=self.update_video_clicked, bg="#FFA07A")
        update_video_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Create a status label to display success or error messages
        self.status_lbl = tk.Label(window, text="", font=("Cousine", 12), bg="#964B00")
        self.status_lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def update_video_clicked(self):
        # Retrieve the video ID and new rating from the entry fields
        video_id = self.video_id_entry.get()
        try:
            new_rating = int(self.rating_entry.get())
        except ValueError:
            self.status_lbl.configure(text="Invalid rating value")
            return

        # Update the video library item if the video ID is valid
        if video_id in lib.catalog:
            item = lib.catalog[video_id]
            item.rating = new_rating
            self.status_lbl.configure(text=f"Video '{item.name}' updated successfully! Rating: {new_rating}, Plays: {item.play_count}")
        else:
            self.status_lbl.configure(text="Invalid video ID")

        # Clear the entry fields
        self.video_id_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)

if __name__ == "__main__":
    window = tk.Tk()
    UpdateVideo(window)
    window.mainloop()