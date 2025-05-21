import cv2

def play_video_in_terminal(video_path, width=80):
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise IOError("Error opening video stream or file")

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                height = int(frame.shape[0] * (width / frame.shape[1]) * 0.5)
                frame_resized = cv2.resize(frame, (width, height))
                
                ascii_frame = ""
                for row in frame_resized:
                    for pixel in row:
                        if pixel < 50:
                            ascii_frame += " "
                        elif pixel < 100:
                            ascii_frame += "."
                        elif pixel < 150:
                            ascii_frame += "*"
                        elif pixel < 200:
                             ascii_frame += "o"
                        else:
                            ascii_frame += "#"
                    ascii_frame += "\n"
                print(ascii_frame)
            else:
                break

        cap.release()
    except Exception as e:
         print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_path = './samplevideo.mp4'  # Replace with the actual path to your video file
    play_video_in_terminal(video_path)