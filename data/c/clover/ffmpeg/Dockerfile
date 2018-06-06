#  
# This is a multi-stage build.  
# Actual build is at the very end.  
#  
FROM library/ubuntu:xenial AS build  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
RUN apt-get update && \  
apt-get install -y \  
xz-utils  
RUN apt-get install -y \  
wget  
  
RUN mkdir -p /build/image/usr/bin  
WORKDIR /build  
RUN wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-64bit-
static.tar.xz  
RUN tar -xvf ffmpeg-git-64bit-static.tar.xz \  
\--exclude=manpages/* \  
\--exclude=manpages \  
\--exclude=*.txt \  
\--strip-components=1 \  
-C image/usr/bin  
  
WORKDIR /build/image  
  
FROM clover/base  
  
WORKDIR /  
COPY \--from=build /build/image /  

