FROM ubuntu:16.04  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get install -y \  
apt-transport-https \  
build-essential \  
ed \  
gtk2.0 \  
libcurl4-openssl-dev \  
libgtk2.0-dev \  
libiodbc2-dev \  
libnlopt-dev \  
libssh2-1-dev \  
libssl-dev \  
libxml2-dev \  
python-dev \  
python-software-properties \  
software-properties-common \  
wget \  
xvfb \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD rtvs-daemon_*.tar.gz /tmp/  
# ADD auto extracts the contents of tar.gz.  
RUN /tmp/rtvs-install -s \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 5444  

