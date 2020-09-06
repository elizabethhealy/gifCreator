import os
import imageio
import subprocess
from typing import List, Union
import random



#Pulled code below from pygifsicle -- a wraper for gifsicle
################################################################################


def gifsicle(sources: Union[List[str], str], destination: str = None, 
optimize: bool = False, colors: int = 256, options: List[str] = None):
    """Apply gifsickle with given options to image at given paths.
    Parameters
    -----------------
    sources:Union[List[str], str],
        Path or paths to gif(s) image(s) to optimize.
    destination:str=None
        Path where to save updated gif. By default the old image is overwrited.
    optimize:bool=False,
        Boolean flag to add the option to optimize image.
    colors:int=256,
        Integer value representing the number of colors to use. Must be a power of 2.
    options:List[str]=None
        List of options.
    Raises
    ------------------
    ValueError:
        If given source path does not exist.
    ValueError:
        If given source path is not a gif image.
    ValueError:
        If given destination path is not a gif image.
    References
    ------------------
    You can learn more about gifsicle at the project home page:
    https://www.lcdf.org/gifsicle/
    """
    if isinstance(sources, str):
        sources = [sources]
    if any([not os.path.exists(source) for source in sources]):
        raise ValueError("Given source path does not exists.")
    if any([not source.endswith(".gif") for source in sources]):
        raise ValueError("Given source path is not a gif image.")
    if destination is None:
        destination = sources[0]
    if not destination.endswith(".gif"):
        raise ValueError("Given destination path is not a gif image.")
    if options is None:
        options = []
    if optimize and "--optimize" not in options:
        options.append("--optimize")
    subprocess.call(["gifsicle", *options, *sources, "--colors",
                     str(colors), "--output", destination])


def optimize(source: str, *args, **kwargs):
    """Optimize given gif.
    Parameters
    -----------------
    source:str,
        Path to gif image to optimize.
    """
    gifsicle(source, *args, **kwargs, optimize=True)

################################################################################


def pics2gif(dir_path, out_name, out_path, duration, img_type):
  """
  Convert set of pictures to gif
  ------------------------------
  dir_path: str
    path to directory where images are stored -- only looks at png

  out_name: str
    name of output file -- without .gif

  out_path: str
    location where gif will be output

  duration: str
    duration of single iteration of gif

  img_type: str
    type of images used to make gif

  """
  pics = []

  for pic_name in os.listdir(dir_path):
    if pic_name.endswith(img_type):
      p_path = os.path.join(dir_path,pic_name)
      pic = imageio.imread(p_path)
      pics.append(pic)


  out_name = out_name + ".gif"
  out_path = os.path.join(out_path,out_name)
  imageio.mimsave(out_path,pics,duration=float(duration)/len(pics))
  optimize_gif(out_path=out_path)



def vid2gif(vid_path, out_name, out_path, duration, start, end, choppy = 1):
  """
  Convert video to gif
  ------------------------------
  vid_path: str
    path to video -- must be mp4

  out_name: str
    name of output file -- without .gif

  out_path: str
    location where gif will be output
    
  duration: str
    duration of single iteration of gif

  start: str
    start time of gif

  end: str
    end time of gif

  choppy: str
    how choppy the gif will be -- lower input -> more choppy

  """
  out_name = out_name + ".gif"
  out_path = os.path.join(out_path,out_name)


  reader = imageio.get_reader(vid_path)
  fps = reader.get_meta_data()['fps']
  start_frame = int(fps*float(start))
  end_frame = int(fps*float(end))

  #writer = imageio.get_writer(out_path, fps=fps)
  pics = []
  for i,im in enumerate(reader):
    if(start_frame<=i and i<=end_frame):
      if(random.uniform(0,1)<=choppy):
        pics.append(im)
    #writer.append_data(im)
  
  #writer.close()
  imageio.mimsave(out_path,pics,duration=float(duration)/len(pics))
  optimize_gif(out_path=out_path)




def optimize_gif(out_path):
  """
  optimize the gif -- usually cuts size in half
  """
  optimize(out_path)

