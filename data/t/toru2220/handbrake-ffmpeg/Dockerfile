FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo 'deb http://ppa.launchpad.net/stebbins/handbrake-releases/ubuntu
xenial main' > /etc/apt/sources.list.d/handbrake.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys 8771ADB0816950D8 &&
\  
apt-get update && \  
apt-get -y \--no-install-recommends install software-properties-common  
  
RUN add-apt-repository ppa:jonathonf/ffmpeg-3 && \  
add-apt-repository ppa:jonathonf/python-3.6  
  
RUN apt-get update && \  
apt-get -y \--no-install-recommends install python3.6 handbrake-cli ffmpeg
libav-tools x264 x265 lsdvd python3-dev python3-pip wget curl libdvdread-dev
libdvdcss-dev && \  
dpkg-reconfigure libdvd-pkg && \  
apt autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/bin/python3 /usr/bin/python  
RUN pip3 install lxml  
  
WORKDIR /data  
VOLUME ["/data"]  
  
  

