FROM ubuntu:16.04  
MAINTAINER neil@grogan.ie  
  
ENV DIRPATH /data  
ENV INSTALL_PKGS stack  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
575159689BEFB442 && \  
echo 'deb http://download.fpcomplete.com/ubuntu xenial main' | tee
/etc/apt/sources.list.d/fpco.list && \  
apt-get update && \  
apt-get install -y $INSTALL_PKGS && \  
/usr/bin/stack setup  
  
WORKDIR $DIRPATH  
VOLUME $DIRPATH  
  
CMD ["/bin/bash"]  

