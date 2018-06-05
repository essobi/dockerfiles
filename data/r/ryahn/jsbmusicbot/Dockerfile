FROM ubuntu:16.04  
MAINTAINER Ryahn, https://github.com/Just-Some-Bots/MusicBot  
  
RUN echo "Updating" && apt-get update  
RUN echo "Installing software-properties-common" && apt-get install software-
properties-common -y  
RUN echo "Adding ppa:deadsnakes" && add-apt-repository -y -r ppa:deadsnakes  
RUN echo "Adding ppa:mc3man/trusty-media" && add-apt-repository -y -r
ppa:mc3man/trusty-media  
RUN rm -f /etc/apt/sources.list.d/mc3man-ubuntu-trusty-media-xenial.list  
RUN echo "Adding ppa:chris-lea/libsodium" && add-apt-repository -y -r
ppa:chris-lea/libsodium  
RUN rm -f /etc/apt/sources.list.d/chris-lea-ubuntu-libsodium-xenial.list  
RUN echo "Updating" && apt-get update -y  
RUN echo "Installing build-essential unzip" && apt-get install build-essential
unzip -y  
RUN echo "Installing python python3.5-dev ffmpeg libopus-dev libffi-dev git
libav-tools libsodium-dev python3-pip" && apt-get install python python3.5-dev
ffmpeg libopus-dev libffi-dev git libav-tools libsodium-dev python3-pip -y  
RUN echo "Upgrading" && apt-get upgrade -y  
  
ADD . /musicbot  
WORKDIR /musicbot  
VOLUME /musicbot/config  
  
RUN python3.5 -m pip install -U pip \  
&& python3.5 -m pip install -U -r requirements.txt  
  
CMD python3.5 run.py

