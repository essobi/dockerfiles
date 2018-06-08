FROM mythay/x11  
MAINTAINER Minglei Hei <mythay@126.com>  
  
# Inspired by monokrome/wine  
ENV WINE_MONO_VERSION 0.0.8  
USER root  
  
# Change to use China mirror, to speed up the apt download speed for test  
# RUN sed -i 's/archive.ubuntu/cn.archive.ubuntu/g' /etc/apt/sources.list  
# Install some tools required for creating the image  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
unzip \  
ca-certificates  
  
# Install wine and related packages  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
wine \  
winetricks \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY waitonprocess.sh /scripts/  
RUN chmod +x /scripts/waitonprocess.sh  
  
# Wine really doesn't like to be run as root, so let's use a non-root user  
USER xclient  
ENV HOME /home/xclient  
ENV WINEPREFIX /home/xclient/.wine  
ENV WINEARCH win32  
  
# Use xclient's home dir as working dir  
WORKDIR /home/xclient  
  
RUN echo "alias winegui='wine explorer /desktop=DockerDesktop,1024x768'" >
~/.bash_aliases  
  
RUN wine wineboot --init \  
&& /scripts/waitonprocess.sh wineserver

