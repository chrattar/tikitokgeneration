from moviepy.editor import ImageSequenceClip
import os

# Folder containing the frames
frame_folder = "frames"

# Get the list of frame file paths
frame_files = [os.path.join(frame_folder, f) for f in sorted(os.listdir(frame_folder)) if f.endswith(".png")]

# Create a video clip from the images
clip = ImageSequenceClip(frame_files, fps=30)

# Write the video to a file
clip.write_videofile("output.mp4", codec="libx264")
