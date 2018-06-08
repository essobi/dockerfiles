FROM debian:jessie  
MAINTAINER Alexandre Duret-Lutz <adl@lrde.epita.fr>  
RUN echo 'deb http://www.lrde.epita.fr/repo/debian/ stable/' >>
/etc/apt/sources.list && \  
echo 'deb http://ftp.uk.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list && \  
apt-get update && \  
RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \--force-yes --no-install-recommends \  
spot build-essential wget openjdk-8-jre parallel \  
gcc-4.9 g++-4.9 make libbdd0c2 libbdd-dev unzip zlib1g-dev \  
&& \  
apt-get clean && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 20 && \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 20  
  
COPY install.sh /tmp/install.sh  
RUN cd /tmp && ./install.sh && rm -f install.sh  

