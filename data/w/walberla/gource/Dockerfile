FROM ubuntu:16.10  
MAINTAINER Christian Godenschwager <christian.godenschwager@fau.de>  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
gource \  
ffmpeg \  
xvfb \  
xfonts-base \  
xfonts-75dpi \  
xfonts-100dpi \  
&& rm -rf /var/lib/apt/lists/*  
# xvfb-run -a -s "-screen 0 1920x1080x24" gource -1920x1080 -r 60 --start-date
"2016-03-16" -s 0.16 -o - | ffmpeg -r 60 -f image2pipe -vcodec ppm -i - -c:v
libx264 -preset slower -pix_fmt yuv420p -movflags +faststart -r 60 -profile:v
baseline -level 3.0 -crf 18 -y /out/test.mp4  

