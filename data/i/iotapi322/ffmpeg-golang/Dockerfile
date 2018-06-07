FROM golang:1.6-alpine  
  
MAINTAINER Matt Snoby <matt.snoby@icloud.com>  
  
  
#  
# Tiny Container that holds ffmpeg, ffprobe and can build / run golang
programs.  
#  
#  
RUN apk --no-cache add ca-certificates curl bash xz-libs git  
WORKDIR /tmp  
RUN curl -L -O http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-
static.tar.xz  
RUN tar -xf ffmpeg-release-64bit-static.tar.xz && \  
cd ff* && mv ff* /usr/local/bin  
  
WORKDIR /  
  
ENTRYPOINT ["/bin/bash"]  

