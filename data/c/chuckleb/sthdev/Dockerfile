# DOCKER-VERSION 0.3.4  
FROM ubuntu  
  
MAINTAINER Charles Nguyen <chuckleb@gmail.com>  
  
# Turn off intaractive mode to reduce noise and errors  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update path  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
# Run updates and install base libs & tools  
RUN apt-get -y update  
RUN apt-get -y install build-essential libx11-dev libglu-dev unzip expect \  
wget libncurses5-dev curl \  
python gtk+-2.0 dbus yasm libasound2-dev libxt-dev zip  
  
# Set SHELL variable for Firefox build  
ENV SHELL /bin/sh make  
  
# Mount point to hold results  
VOLUME ["/data"]  
  
# This will force it to pull latest script and execute  
ENTRYPOINT ["/bin/bash", "-c", "wget
https://raw.githubusercontent.com/chuckleb/linuxbench-dev/master/firefox-
compile.sh;chmod a+x *.sh ;./firefox-compile.sh"]  

