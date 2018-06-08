# ----------------------------------  
# Mount & Blade Warband Dockerfile  
# Environment: Ubuntu:16.04 + Wineconsole  
# Minimum Panel Version: 0.7.6  
# ----------------------------------  
FROM ubuntu:16.04  
MAINTAINER Mason Rowe, <mason@rowe.sh>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Dependencies  
RUN dpkg --add-architecture i386 \  
&& apt update \  
&& apt upgrade -y \  
&& apt install -y wget software-properties-common apt-transport-https bsdtar
dos2unix \  
&& wget -qO - https://dl.winehq.org/wine-builds/Release.key | apt-key add - \  
&& apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ \  
&& apt update \  
&& apt install -y --install-recommends winehq-stable \  
&& apt clean \  
&& useradd -m -d /home/container container \  
&& cd /home/container  
  
USER container  
ENV HOME /home/container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

