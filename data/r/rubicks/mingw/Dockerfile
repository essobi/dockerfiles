# dockers/mingw/Dockerfile  
FROM rubicks/xdev  
MAINTAINER rubicks  
  
RUN dpkg --add-architecture i386 && \  
apt-get -y update && \  
apt-get -y dist-upgrade && \  
apt-get -y install \  
mingw32 \  
mingw32-binutils \  
mingw32-runtime \  
wine  
  
CMD /bin/bash  

