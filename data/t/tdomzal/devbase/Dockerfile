#  
# Phusion based developer base image.  
# With all small stuff handy when exploring docker posibilities.  
# Not recommended for any production images.  
# © tdomzal@gmail.com  
#  
# Use phusion/baseimage as base image.  
# See # https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
#  
FROM phusion/baseimage:0.9.17  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get update \  
&& apt-get install -y \  
ca-certificates \  
curl \  
git \  
htop \  
sudo \  
telnet \  
unzip \  
vim \  
wget \  
zip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Althought seen in many examples setting noninteractive is discouraged in
FAQ:  
# Why is debian_frontend=noninteractive discouraged in Dockerfiles?  
# http://docs.docker.com/engine/misc/faq/  
#  
# ENV DEBIAN_FRONTEND noninteractive  
  
ENV TZ "Europe/Warsaw"  
ENV LANG en_US.UTF-8  
ENV LC_MESSAGES POSIX  
  
RUN echo "Europe/Warsaw" | sudo tee /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata \  
&& echo "LANG=\"en_US.UTF-8\"" > /etc/default/locale \  
&& echo "LC_MESSAGES=\"POSIX\"" >> /etc/default/locale \  
&& echo ":color desert" >> /etc/vim/vimrc.local \  
&& echo "alias ll='ls --color -lF'" >> /etc/bash.bashrc  

