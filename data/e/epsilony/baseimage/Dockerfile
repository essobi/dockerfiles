# A docker image according to the poor network environment of China PR  
FROM phusion/baseimage  
  
MAINTAINER Man YUAN  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Use source mirror near Anhui Province  
COPY sources.list /etc/apt/sources.list  
  
# set timezone  
RUN echo Asia/Shanghai | \  
tee /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata  
  
# some tools  
RUN apt-get update && \  
apt-get install -y build-essential \  
wget \  
unzip \  
tmux \  
python python-pip \  
git \  
netcat  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

