  
FROM ubuntu:16.04  
LABEL maintainer "Federico Voges <fvoges@gmail.com>"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && apt-get
autoclean && apt-get autoremove  
  
RUN apt-get -q -y --no-install-recommends install locales  
RUN locale-gen en_GB.UTF-8  
ENV LANGUAGE en_GB.UTF-8  
ENV LC_ALL en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LC_TYPE en_GB.UTF-8  
ENV TZ Europe/London  
  
RUN apt-get install -q -y --no-install-recommends \  
build-essential \  
motion \  
ffmpeg \  
v4l-utils \  
python-pip \  
python-dev \  
curl \  
libssl-dev \  
libcurl4-openssl-dev \  
libjpeg-dev  
  
RUN pip install --upgrade pip setuptools  
RUN pip install motioneye  
  
RUN mkdir -p /etc/motioneye /var/lib/motioneye  
  
RUN apt-get clean && apt-get autoclean -y && apt-get autoremove -y  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# R/W needed for motioneye to update configurations  
VOLUME /etc/motioneye  
  
# PIDs  
#VOLUME /var/run/motion  
# Video & images  
VOLUME /var/lib/motioneye  
  
CMD test -e /etc/motioneye/motioneye.conf || \  
cp /usr/local/share/motioneye/extra/motioneye.conf.sample
/etc/motioneye/motioneye.conf ; \  
/usr/local/bin/meyectl startserver -c /etc/motioneye/motioneye.conf  
  
EXPOSE 8081 8765  

