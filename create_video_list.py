import tkinter as tk
import video_library as lib  # Import the video library module for access

class GenerateVideoPlaylist:
    def __init__(self, window):
        self.video_list = []  # Initialize an empty video list

        window.geometry("480x400")
        window.title("Video Playlist Generator")

        # Set the background color of the window to a soft gray
        window.configure(bg="#E5E5EA")

        # Label for entering video ID
        video_id_lbl = tk.Label(window, text="Video ID:", bg="#F7DC6F")
        video_id_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="E")

        # Entry for video ID
        self.video_id_entry = tk.Entry(window, width=10)
        self.video_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to add video to the playlist
        add_video_btn = tk.Button(window, text="Add to Playlist", command=self.add_video_clicked, bg="#FFC107")
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)

        # Text area to display the playlist
        self.playlist_display = tk.Text(window, height=10, width=50)
        self.playlist_display.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Button to play the playlist
        play_playlist_btn = tk.Button(window, text="Play Videos", command=self.play_playlist_clicked, bg="#8BC34A")
        play_playlist_btn.grid(row=2, column=2, padx=10, pady=10)

        # Button to reset the playlist
        reset_playlist_btn = tk.Button(window, text="Clear Playlist", command=self.reset_playlist_clicked, bg="#FF69B4")
        reset_playlist_btn.grid(row=2, column=1, padx=10, pady=10)

        # Status label to show success or error messages
        self.status_lbl = tk.Label(window, text="", font=("Cousine", 12), bg="#E5E5EA")
        self.status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def add_video_clicked(self):
        video_key = self.video_id_entry.get().zfill(2)  # Ensure the key is zero-padded to 2 digits
        
        if video_key in lib.catalog:
            video_name = lib.catalog[video_key].name
            self.video_list.append(video_name)
            self.update_playlist_display()
            self.status_lbl.configure(text=f"Video '{video_name}' added to playlist")
        else:
            self.status_lbl.configure(text=f"Invalid video ID: {video_key}")

        self.video_id_entry.delete(0, tk.END)

    def play_playlist_clicked(self):
        for video_name in self.video_list:
            for key, item in lib.catalog.items():
                if item.name == video_name:
                    lib.increment_play_count(key)

        self.status_lbl.configure(text="Playlist played (simulated). Play counts incremented.")

    def reset_playlist_clicked(self):
        self.video_list = []
        self.playlist_display.delete(1.0, tk.END)
        self.status_lbl.configure(text="Playlist cleared")

    def update_playlist_display(self):
        self.playlist_display.delete(1.0, tk.END)
        for video in self.video_list:
            self.playlist_display.insert(tk.END, f"{video}\n")


if __name__ == "__main__":
    window = tk.Tk()
    GenerateVideoPlaylist(window)
    window.mainloop()