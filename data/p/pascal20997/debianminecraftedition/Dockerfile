FROM debian:8  
MAINTAINER Pascal Rinker <info@kronova.net>  
  
# Set correct environment variables  
ENV HOME /root  
  
# don't ask for stupid things  
env DEBIAN_FRONTEND noninteractive  
RUN echo APT::Install-Recommends "0"; >> /etc/apt/apt.conf  
RUN echo APT::Install-Suggests "0"; >> /etc/apt/apt.conf  
  
RUN echo "Update system..."  
# update the system  
RUN apt-get update && apt-get -y upgrade && dpkg-divert --local \--rename
--add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl  
  
RUN echo "Installing tools..."  
# Install Tools  
RUN apt-get install -qy wget curl locales unzip sudo  
  
RUN echo "Installing minecraft dependencies..."  
# install minecraft dependencies  
RUN apt-get install -qy \  
openjdk-7-jre \  
openjdk-7-jdk \  
cron  
  
# Configure timezone and locale  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure tzdata  
RUN export LANGUAGE=en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
export LC_ALL=en_US.UTF-8 && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "Done, have fun!"  
  
CMD ["/bin/bash"]  

