FROM strm/vnc  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
wget \  
unrar unzip \  
wine && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /c  
  

