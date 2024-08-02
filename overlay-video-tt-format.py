from moviepy.editor import VideoFileClip, clips_array

# Cretae grid of 4 clips, rename as required.
clip1 = VideoFileClip("./mergefolder/video1.mp4").resize((540, 960))
clip2 = VideoFileClip("video2.mp4").resize((540, 960))
clip3 = VideoFileClip("video3.mp4").resize((540, 960))
clip4 = VideoFileClip("video4.mp4").resize((540, 960))

# Create the 2x2 grid
final_clip = clips_array([[clip1, clip2], [clip3, clip4]])

# Set tiktok res.
final_clip = final_clip.resize((1080, 1920))

# Write the result to a file
final_clip.write_videofile("output_grid.mp4", codec="libx264", fps=24)
