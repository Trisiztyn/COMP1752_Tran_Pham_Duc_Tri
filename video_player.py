import tkinter as tk
from update_video import UpdateVideo
from create_video_list import GenerateVideoPlaylist
from check_videos import VideoChecker

def check_video_details_clicked():
    # Update the status label to indicate that the "Video Checker" button was clicked
    status_lbl.config(text="Checking videos...")
    # Create a new window for checking videos
    VideoChecker(tk.Toplevel(window))

def create_videos_clicked():
    # Update the status label to indicate that the "Generate Video Playlist" button was clicked
    status_lbl.config(text="Generating Video Playlist...")
    # Create a new window for creating a video list
    GenerateVideoPlaylist(tk.Toplevel(window))

def update_video_clicked():
    # Update the status label to indicate that the "Update Videos" button was clicked
    status_lbl.config(text="Updating videos...")
    # Create a new window for updating videos
    UpdateVideo(tk.Toplevel(window))

# Create the main window
window = tk.Tk()
window.geometry("420x100")
window.title("Video Manager")

# Create a label to display a header message
header_lbl = tk.Label(window, text="Choose an option by clicking a button below")
header_lbl.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create a button to check videos
check_videos_btn = tk.Button(window, text="Verify Videos", command=check_video_details_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

# Create a button to create a video list
create_video_list_btn = tk.Button(window, text="Generate Video List", command=create_videos_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

# Create a button to update videos
update_videos_btn = tk.Button(window, text="Refresh Videos", command=update_video_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

# Create a label to display the status of the application
status_lbl = tk.Label(window, text="", font=("Cousine", 12))
status_lbl.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Start the main event loop
window.mainloop()