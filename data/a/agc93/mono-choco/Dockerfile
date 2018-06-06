FROM mono:3.12  
LABEL maintainer="Alistair Chapman <alistair@agchapman.com>" \  
description="A simple Docker image using Mono 3.12 to run Chocolatey"  
  
RUN apt-get update && apt-get install -y wget unzip git mono-devel  
RUN mozroots --import --sync  
  
WORKDIR /usr/local/src  
RUN git clone \--depth=10 --branch=master
https://github.com/chocolatey/choco.git  
  
WORKDIR /usr/local/src/choco  
RUN chmod +x build.sh  
RUN ./build.sh  
  
COPY choco /usr/local/bin/choco  
RUN chmod +x /usr/local/bin/choco  
  
WORKDIR /root  

