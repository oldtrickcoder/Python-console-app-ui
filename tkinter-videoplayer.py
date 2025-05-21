import tkinter as tk
from tkinter import filedialog, messagebox
import vlc
import os
import sys

# --- VLC Path Configuration ---
# IMPORTANT: Adjust this path to your actual VLC installation directory
# Example for Windows: r'C:\Program Files\VideoLAN\VLC'
# Example for 32-bit VLC on 64-bit Windows: r'C:\Program Files (x86)\VideoLAN\VLC'
# For macOS or Linux, python-vlc often finds VLC automatically if it's in standard locations.
# If you get FileNotFoundError, uncomment and adjust the path below:
vlc_path = r'C:\Program Files\VideoLAN\VLC'

# --- Ensure VLC DLLs are found (crucial for Python 3.8+ on Windows) ---
if sys.platform.startswith('win'):
    if os.path.exists(vlc_path):
        if hasattr(os, 'add_dll_directory'):
            os.add_dll_directory(vlc_path)
    else:
        messagebox.showerror("VLC Error", f"VLC installation not found at '{vlc_path}'.\n"
                                         "Please install VLC Media Player (ensure 64-bit for 64-bit Python) "
                                         "or adjust the 'vlc_path' variable in the script.")
        sys.exit(1) # Exit if VLC path is incorrect

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom VLC Player with Fullscreen")
        self.root.geometry("800x600") # Initial window size
        self.root.minsize(400, 300) # Minimum window size

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.is_fullscreen = False # Track fullscreen state

        # --- Video Frame (where VLC will embed its output) ---
        self.video_frame = tk.Frame(self.root, bg="black", bd=2, relief="sunken")
        self.video_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.video_frame.update_idletasks() # Ensures the widget has a valid window ID

        # Get the window handle (ID) for VLC to embed the video
        if sys.platform.startswith('win'): # For Windows
            self.player.set_hwnd(self.video_frame.winfo_id())
            print(f"Windows handle (HWND) for video_frame: {self.video_frame.winfo_id()}")
        elif sys.platform.startswith('linux'): # For Linux (X11)
            self.player.set_xwindow(self.video_frame.winfo_id())
            print(f"XWindow ID for video_frame: {self.video_frame.winfo_id()}")
        elif sys.platform.startswith('darwin'): # For macOS
            # macOS embedding is complex. Often easier to let VLC open its own window.
            print("Embedding VLC on macOS is complex and might not work directly with winfo_id().")
            print("VLC might open its own window for video display on macOS.")
            # For basic functionality, you might just skip setting the window handle
            # and VLC will create its own window which can then be put into fullscreen.
            # self.player.set_agl_context(self.video_frame.winfo_id()) # This needs more setup
        else:
            print(f"Unsupported platform for embedding: {sys.platform}. VLC might open its own window.")

        # --- Controls Frame ---
        self.controls_frame = tk.Frame(self.root, bd=2, relief="groove")
        self.controls_frame.pack(fill=tk.X, padx=5, pady=5)

        # Buttons (Open, Play/Pause, Stop, Mute, Fullscreen)
        self.open_button = tk.Button(self.controls_frame, text="Open Video", command=self.open_file)
        self.open_button.grid(row=0, column=0, padx=5, pady=5)

        self.play_pause_button = tk.Button(self.controls_frame, text="Play", command=self.toggle_play_pause)
        self.play_pause_button.grid(row=0, column=1, padx=5, pady=5)

        self.stop_button = tk.Button(self.controls_frame, text="Stop", command=self.stop_video)
        self.stop_button.grid(row=0, column=2, padx=5, pady=5)

        self.volume_slider = tk.Scale(self.controls_frame, from_=0, to=100, orient="horizontal",
                                       label="Vol", command=self.set_volume, length=100)
        self.volume_slider.set(70)
        self.player.audio_set_volume(70)
        self.volume_slider.grid(row=0, column=3, padx=5, pady=5)

        self.mute_button = tk.Button(self.controls_frame, text="Mute", command=self.toggle_mute)
        self.mute_button.grid(row=0, column=4, padx=5, pady=5)

        self.fullscreen_button = tk.Button(self.controls_frame, text="Fullscreen", command=self._toggle_fullscreen_ui)
        self.fullscreen_button.grid(row=0, column=5, padx=5, pady=5)

        # Progress Slider
        self.progress_slider = tk.Scale(self.controls_frame, from_=0, to=1000, orient="horizontal",
                                        command=self.set_position_from_slider,
                                        length=300, showvalue=0)
        self.progress_slider.grid(row=1, column=0, columnspan=5, sticky="ew", padx=5, pady=5)
        self.progress_slider.bind("<ButtonRelease-1>", self.on_progress_slider_release)

        # Time Label
        self.time_label = tk.Label(self.controls_frame, text="00:00 / 00:00")
        self.time_label.grid(row=1, column=5, padx=5, pady=5)

        # Variables to manage state
        self.media_loaded = False
        self.duration_ms = 0

        # Start periodic updates
        self.update_id = None
        self.update_playback_status()

        # Bind Escape key for fullscreen exit
        self.root.bind("<Escape>", self.exit_fullscreen_key)

        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov *.wmv"),
                       ("All Files", "*.*")]
        )
        if file_path:
            self.stop_video()
            media = self.instance.media_new(file_path)
            self.player.set_media(media)
            self.media_loaded = True
            self.play_video()
            self.root.title(f"Custom VLC Player - {os.path.basename(file_path)}")
            self.root.after(500, self._update_duration_and_slider) # Give VLC time to load metadata

    def _update_duration_and_slider(self):
        self.duration_ms = self.player.get_length()
        if self.duration_ms > 0:
            self.progress_slider.config(to=self.duration_ms // 1000)
        else:
            self.progress_slider.config(to=1000) # Fallback

    def play_video(self):
        if self.media_loaded:
            self.player.play()
            self.play_pause_button.config(text="Pause")

    def pause_video(self):
        self.player.pause()
        self.play_pause_button.config(text="Play")

    def toggle_play_pause(self):
        if self.player.is_playing():
            self.pause_video()
        else:
            self.play_video()

    def stop_video(self):
        self.player.stop()
        self.media_loaded = False
        self.play_pause_button.config(text="Play")
        self.progress_slider.set(0)
        self.time_label.config(text="00:00 / 00:00")
        self.root.title("Custom VLC Player with Fullscreen")

    def set_volume(self, val):
        volume = int(val)
        self.player.audio_set_volume(volume)

    def toggle_mute(self):
        is_muted = self.player.audio_get_mute()
        self.player.audio_set_mute(not is_muted)
        self.mute_button.config(text="Unmute" if not is_muted else "Mute")

    def set_position_from_slider(self, val):
        pass # Actual seek handled on release

    def on_progress_slider_release(self, event):
        if self.media_loaded:
            seek_time_sec = int(self.progress_slider.get())
            self.player.set_time(seek_time_sec * 1000)

    # --- Fullscreen Logic ---
    def _toggle_fullscreen_ui(self):
        """
        Manages both VLC's internal fullscreen and Tkinter's window state.
        Called by the Fullscreen button.
        """
        self.is_fullscreen = not self.is_fullscreen

        # Toggle Tkinter window fullscreen attributes
        self.root.attributes('-fullscreen', self.is_fullscreen)
        self.root.overrideredirect(self.is_fullscreen) # Hide title bar, etc.

        # Toggle visibility of controls frame
        if self.is_fullscreen:
            self.controls_frame.pack_forget() # Hide controls
        else:
            self.controls_frame.pack(fill=tk.X, padx=5, pady=5) # Show controls again

        # Tell VLC player to toggle its fullscreen state
        # This will make the video itself fill the embedded window
        self.player.toggle_fullscreen()

    def exit_fullscreen_key(self, event):
        """
        Handles exiting fullscreen when Escape key is pressed.
        """
        if self.is_fullscreen:
            self._toggle_fullscreen_ui() # Use the same toggle logic

    def update_playback_status(self):
        # Only update if a media is loaded and not at the end
        if self.media_loaded and self.player.get_state() not in (vlc.State.Ended, vlc.State.Stopped):
            current_time_ms = self.player.get_time()
            total_duration_ms = self.player.get_length()

            if total_duration_ms > 0 and self.duration_ms != total_duration_ms:
                self.duration_ms = total_duration_ms
                self._update_duration_and_slider()

            if current_time_ms != -1 and total_duration_ms > 0:
                current_time_sec = current_time_ms // 1000
                total_duration_sec = total_duration_ms // 1000

                minutes_current = current_time_sec // 60
                seconds_current = current_time_sec % 60
                minutes_total = total_duration_sec // 60
                seconds_total = total_duration_sec % 60
                self.time_label.config(text=f"{minutes_current:02}:{seconds_current:02} / {minutes_total:02}:{seconds_total:02}")

                if not self.progress_slider.grab_current(): # Update slider only if not being dragged
                    self.progress_slider.set(current_time_sec)
            else:
                self.time_label.config(text="--:-- / --:--")
        elif self.media_loaded and self.player.get_state() == vlc.State.Ended:
            self.stop_video() # Reset UI when video ends

        self.update_id = self.root.after(1000, self.update_playback_status)

    def on_closing(self):
        if self.update_id:
            self.root.after_cancel(self.update_id)
        
        self.stop_video()
        self.player.release()
        self.instance.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()