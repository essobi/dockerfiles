FROM ubuntu:16.04  
MAINTAINER Mike Terzo <mike@terzo.org>  
  
RUN apt-get -y update && apt-get install -y \  
libjpeg8 \  
libzip4 \  
ffmpeg \  
libavformat-ffmpeg56 \  
libavutil-ffmpeg54 \  
libavcodec-ffmpeg56 \  
libswscale-ffmpeg3 \  
libv4l-0 \  
libsqlite3-0 \  
libmysql++3v5 \  
libpqxx-4.0 \  
&& rm -rf /var/lib/apt/lists/*  

