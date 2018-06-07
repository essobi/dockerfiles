# ----------------------------------  
# Pterodactyl Modified Dockerfile  
# Minimum Panel Version: 0.6.0  
# ----------------------------------  
FROM ubuntu:18.04  
  
MAINTAINER Bryce Anglin, <brycea@rapidnetworks.org>  
ENV DEBIAN_FRONTEND noninteractive  
# Install Dependencies  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y tar curl gcc g++ libglu1-mesa libxcursor1 libxrandr2
lib32gcc1 lib32tinfo5 lib32z1 lib32stdc++6 iproute2 gdb \  
&& useradd -m -d /home/container container  
  
USER  container  
ENV HOME /home/container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

