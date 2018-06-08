FROM ubuntu:latest  
  
MAINTAINER Mateo R, <mateoradic16@gmail.com>  
  
RUN dpkg --add-architecture i386 && \  
apt update && \  
apt install -y tzdata && \  
apt update && \  
apt install -y lib32gcc1 lib32stdc++6 curl unzip libmono-cil-dev mono-runtime
mono-reference-assemblies-2.0 lib32gcc1 lib32stdc++6 libglu1-mesa libxcursor1
libxrandr2 libc6:i386 libgl1-mesa-glx:i386 libxcursor1:i386 libxrandr2:i386
libc6-dev-i386 libgcc-4.8-dev:i386 && \  
useradd -d /home/container -m container  
  
USER container  
ENV  USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

