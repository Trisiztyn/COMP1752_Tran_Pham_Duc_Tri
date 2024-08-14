import tkinter as tk
import tkinter.scrolledtext as tkst


import video_library as lib 
import font_manager as fonts 


def update_text_area(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class VideoChecker():
    def __init__(self, window):
        window.geometry("720x350")
        window.title("Video Checker")

        catalog_btn = tk.Button(window, text="Display Catalog", command=self.display_catalog_clicked)
        catalog_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video ID")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_field = tk.Entry(window, width=3)
        self.input_field.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video Details", command=self.check_video_details_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.catalog_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.catalog_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_details_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_details_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Cousine", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.display_catalog_clicked()

    def check_video_details_clicked(self):
        key = self.input_field.get()
        title = lib.retrieve_title(key)
        if title is not None:
            director = lib.retrieve_director(key)
            rating = lib.retrieve_rating(key)
            play_count = lib.retrieve_play_count(key)
            video_info = f"{title}\n{director}\nrating: {rating}\nplays: {play_count}"
            update_text_area(self.video_details_txt, video_info)
        else:
            update_text_area(self.video_details_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video Details button was clicked!")

    def display_catalog_clicked(self):
        catalog_list = lib.display_catalog()
        update_text_area(self.catalog_txt, catalog_list)
        self.status_lbl.configure(text="Display Catalog button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    VideoChecker(window)     # open the VideoChecker GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc