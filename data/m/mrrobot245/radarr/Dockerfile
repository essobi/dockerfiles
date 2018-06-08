FROM linuxserver/radarr:latest  
RUN apt-get update && apt-get -y install php wget php-curl && rm -rf
/var/lib/apt/lists/*  
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-
static.tar.xz && tar -xf ffmpeg-release-* && cp ffmpeg-*/ffprobe
/usr/local/bin/ && cp ffmpeg-*/ffmpeg /usr/local/bin/ && rm -rf ffmpeg*  
RUN apt-get remove wget -y  

