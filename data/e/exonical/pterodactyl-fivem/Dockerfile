FROM ubuntu:16.04  
MAINTAINER Bryce A. <brycea@rapidnetworks.org>  
  
RUN apt update && \  
apt upgrade -y && \  
apt install -y lib32gcc1 lib32stdc++6 git wget unzip curl xz-utils && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/ubuntu xenial main" >
/etc/apt/sources.list.d/mono-official.list && \  
apt update && \  
apt install -y mono-devel mono-complete && \  
useradd -m -d /home/container container  
  
USER container  
ENV HOME /home/container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

