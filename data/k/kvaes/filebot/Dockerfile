# Initial fork from https://github.com/Sidirius/docker-filebot  
#  
# Handbrake Dockerfile  
#  
# Source : https://bitbucket.org/kvaes/docker-handbrake/  
# Author : Karim Vaes  
#  
# Use Ubuntu 14.04 as a base  
FROM ubuntu:14.04  
# Add Java Repository  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN apt-mark hold initscripts udev plymouth mountall  
RUN dpkg-divert --local \--rename --add /sbin/initctl && ln -sf /bin/true
/sbin/initctl  
  
RUN apt-get update  
RUN apt-get install -y --force-yes software-properties-common net-tools nodejs  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y --force-yes oracle-java8-installer  
  
WORKDIR /  
RUN wget -O filebot-amd64.deb
'http://filebot.sourceforge.net/download.php?type=deb&arch=amd64'  
RUN sudo dpkg --force-depends -i filebot-*.deb  
  
# Volumes  
VOLUME ["/input"]  
VOLUME ["/output"]  
  
# Let's prep the install  
RUN mkdir -p /data/bin && mkdir -p /input && mkdir -p /output  
  
# Pull the latest batch script  
ENV HOME /root  
COPY *.sh /data/bin/  
  
# Setup 755 on scripts  
RUN chmod 755 /data/bin/*.sh  
  
# Define default command.  
CMD ["/data/bin/control.sh"]  

