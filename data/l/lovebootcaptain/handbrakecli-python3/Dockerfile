FROM phusion/baseimage  
  
MAINTAINER lovebootcaptain <@lovebootcaptain>  
  
ARG SETLANG  
  
# setup ENV  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
ENV PATH /root/scripts:$PATH  
  
# set and update repo  
RUN sed -i 's#http://archive.ubuntu.com/#http://tw.archive.ubuntu.com/#'
/etc/apt/sources.list \  
&& apt-get update  
  
# generate additional locale (e.g. for DE use de_DE.UTF-8 as --build-arg)  
RUN locale-gen $SETLANG  
  
# install and setup timezone  
RUN apt-get install -y --no-install-recommends \  
tzdata \  
&& echo $TZ | tee /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
# install python3 packages  
RUN apt-get install -y --no-install-recommends \  
python3 \  
python3-pip \  
python3-dev \  
python3-setuptools \  
build-essential  
  
# install other apps  
RUN apt-get install -y \  
nano \  
handbrake-cli \  
mkvtoolnix \  
gpac  
  
# clean up  
RUN apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
#set direcotries  
WORKDIR /root  
  
# create mount folders  
RUN mkdir input output  
  
ADD scripts /root/scripts  
  
# set entrypoint  
ENTRYPOINT bash

