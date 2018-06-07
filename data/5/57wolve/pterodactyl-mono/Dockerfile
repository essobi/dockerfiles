# ----------------------------------  
# Pterodactyl Core Dockerfile  
# Environment: Mono  
# Minimum Panel Version: 0.6.0  
# ----------------------------------  
FROM ubuntu:16.04  
MAINTAINER Pterodactyl Software, <support@pterodactyl.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y sudo \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/ubuntu xenial main" | sudo
tee /etc/apt/sources.list.d/mono-official.list \  
&& apt-get update -y \  
&& apt-get install -y openssl tar unzip curl gcc g++ lib32gcc1 lib32tinfo5
lib32z1 lib32stdc++6 libtinfo5:i386 libncurses5:i386 libcurl3-gnutls:i386
iproute2 gdb ca-certificates mono-complete ca-certificates-mono mono-xsp4 \  
&& useradd -m -d /home/container container  
  
USER container  
ENV HOME /home/container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

