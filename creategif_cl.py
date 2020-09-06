from creategif import *

def run_pic2gif():
  """
  Running conversion of images to gif
  Accepts user input: image directory, image type, output name, 
                      output location, and gif length
  """
  print("Images must already be in order in directory")
  im_dir = input("Image directory path: ").strip()
  print("")
  img_type = '.'+input("Image file extension (ex. png, jpg ...): ").strip().lower()
  print("")
  out_name = input("Gif name (not including extension): ").strip()
  print("")
  out_path = input("Where would you like to save the gif? ").strip()
  print("")
  duration = input("How long would you like a single iteration of your gif to be?(seconds): ").strip()
  print("")
  pics2gif(dir_path=im_dir, out_name=out_name, 
  out_path=out_path, duration = duration, img_type=img_type)
  print("YOUR GIF IS HAS BEEN CREATED!")



def run_vid2gif():
  """
  Running conversion of video to gif
  Accepts uder input: video location, gif start time, gif end time, choppiness, 
                      output name, output location, output length
  """
  vid_path = input("Video path: ").strip()
  print("")
  start = input("Start time: ").strip()
  print("")
  end = input("End time: ").strip()
  print("")
  ##FIX THE PHRASING OF THIS!
  print("How choppy would you like your gif to be? 0 -> very choppy, 1 -> not choppy")
  choppy = float(input("Input number between 0 and 1: ").strip())
  print("")
  out_name = input("Gif name (not including extension): ").strip()
  print("")
  out_path = input("Where would you like to save the gif? ").strip()
  print("")
  duration = input("How long would you like a single iteration of your gif to be?(seconds): ").strip()
  print("")
  vid2gif(vid_path=vid_path, out_name=out_name, out_path=out_path,
  duration=duration, start=start, end=end, choppy=choppy)
  print("YOUR GIF IS HAS BEEN CREATED!")


###Execute program

print("")
print("------------------------------------------------")
print("Welcome to gifCreator -- a program that converts a set "+
"of images (png) or a video to a gif!")
print("------------------------------------------------")
print("")
while True:
  option = input("Convert pics2gif or vid2gif? ['p'/'v']: ")
  print("")
  if option == "p":
    run_pic2gif()
    break
  elif option == "v":
    run_vid2gif()
    break
  print("Not an option")
