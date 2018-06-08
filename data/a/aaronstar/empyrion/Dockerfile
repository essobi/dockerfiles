# ----------------------------------  
# A Modification of a Pterodactyl Core Dockerfile  
# Environment: Source Engine  
# Minimum Panel Version: 0.6.0  
# ----------------------------------  
FROM ubuntu:16.04  
MAINTAINER Pterodactyl Software, <support@pterodactyl.io>  
ENV DEBIAN_FRONTEND noninteractive  
ENV DISPLAY localhost:1.0  
# Install Dependencies  
COPY ./xvfb.service /etc/systemd/system/xvfb.service  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install netcat-traditional -y \  
&& apt-get install -y tar git wget unzip curl gcc g++ xz-utils libgdiplus
lib32gcc1 lib32tinfo5 lib32z1 lib32stdc++6 libtinfo5:i386 libncurses5:i386
libcurl3-gnutls:i386 iproute2 gdb xorg xvfb xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/ubuntu xenial main" >
/etc/apt/sources.list.d/mono-official.list \  
&& apt-get update \  
&& apt-get install -y mono-devel mono-complete \  
&& useradd -m -d /home/container container \  
&& chmod -R 777 tmp \  
&& systemctl enable xvfb.service  
  
USER container  
ENV HOME /home/container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

