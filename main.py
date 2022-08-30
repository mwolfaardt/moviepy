from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ImageClip, ColorClip, concatenate_videoclips
clip1 = VideoFileClip("20220816 - August Meetup.mp4")
clip2 = clip1.subclip("00:16:10.00", "00:16:50.00")
# txtclip = TextClip("Power Apps Community Meetup - August 2022", fontsize = 75, color = 'black')
# txtclip = txtclip.set_pos('center').set_duration(10)
# clip2 = CompositeVideoClip([clip2, txtclip])
# clip2.write_videofile("two.mp4")

#splashscreen = ImageClip('AugMeetup.png', duration = 5)
#finalvideo = CompositeVideoClip([splashscreen, clip2])
#finalvideo.write_videofile("two.mp4")
image_clip = ImageClip("AugMeetup.png")
text_clip = TextClip(txt="August 2022".upper(),
                     size=(.8*image_clip.size[0], 0),
                     font="The Hand",
                     color="white")
text_clip = text_clip.set_position('center')

im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)),
                       color=(0, 255, 255))
                       
color_clip = color_clip.set_opacity(.6)
clip_to_overlay = CompositeVideoClip([color_clip, text_clip])
clip_to_overlay = clip_to_overlay.set_position('center')
final_clip = CompositeVideoClip([image_clip, clip_to_overlay])
#final_clip.save_frame("out.png")
final_clip = final_clip.set_duration(5)

finalvideo = CompositeVideoClip([final_clip, clip2.set_start(5)], size=(1920,1080))
finalvideo.write_videofile("two.mp4")