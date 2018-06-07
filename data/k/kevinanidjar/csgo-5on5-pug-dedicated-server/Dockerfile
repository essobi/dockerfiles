FROM ubuntu:latest  
  
LABEL \  
author="Kevin Anidjar <contact@kevin-anidjar.com>" \  
version="1.0" \  
description="CS:GO 5on5 pug - dedicated server"  
  
RUN set -x \  
&& dpkg \--add-architecture i386 \  
&& apt-get update \  
&& apt-get -y install \  
sudo \  
vim \  
curl \  
wget \  
rsync \  
file \  
bzip2 \  
gzip \  
unzip \  
bsdmainutils \  
python \  
util-linux \  
tmux \  
lib32gcc1 \  
libstdc++6 \  
libstdc++6:i386  
  
RUN useradd csgoserver --create-home  
USER csgoserver  
WORKDIR /home/csgoserver  
  
RUN set -x \  
&& wget https://gameservermanagers.com/dl/csgoserver \  
&& chmod +x csgoserver  
  
EXPOSE 27015  
COPY ./boot.sh /opt/boot.sh  
CMD ["/opt/boot.sh"]  

