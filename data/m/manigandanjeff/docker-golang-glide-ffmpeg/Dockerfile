#!/bin/bash  
FROM debian:jessie  
  
MAINTAINER Manigandan Dharmalingam <manigandan.jeff@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y wget gcc curl xz-utils git xvfb libfontconfig
wkhtmltopdf make  
#-----------------------------------  
# Install ffmpeg  
RUN wget -P /tmp https://johnvansickle.com/ffmpeg/releases/ffmpeg-
release-64bit-static.tar.xz  
RUN cd /tmp && \  
tar xf ffmpeg-release-64bit-static.tar.xz && \  
ls && \  
cd ffmpeg-3.3.4-64bit-static/ && \  
cp ffmpeg /usr/bin/ffmpeg && \  
cp ffprobe /usr/bin/ffprobe && \  
chmod +x /usr/bin/ffmpeg && \  
chmod +x /usr/bin/ffprobe  
#-----------------------------------  
# Install Golang  
RUN wget -P /tmp https://storage.googleapis.com/golang/go1.8.3.linux-
amd64.tar.gz  
RUN tar -C /usr/local -xzf /tmp/go1.8.3.linux-amd64.tar.gz  
RUN rm /tmp/go1.8.3.linux-amd64.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
WORKDIR $GOPATH  
#-----------------------------------  
# Install golang - glide  
RUN curl https://glide.sh/get | sh  

