FROM ubuntu:latest  
  
# thanks also to https://github.com/Krijger/docker-cookbooks  
MAINTAINER Simon Stanlake "https://github.com/sedsimon"  
# make sure the package repository is up to date  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
locale-gen en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl git htop man
software-properties-common unzip vim wget  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV HOME /root  
  
# supervisor installation &&  
# create directory for child images to store configuration in  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
# supervisor base configuration  
ADD supervisor.conf /etc/supervisor.conf  
  
# default command  
CMD ["supervisord", "-c", "/etc/supervisor.conf"]  

