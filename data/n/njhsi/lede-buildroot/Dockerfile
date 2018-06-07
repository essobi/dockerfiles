# /dl - the download repo, /lede - the LEDE.git root,  
#  
#  
FROM debian:stable  
LABEL CMDBUILD="docker build -t njhsi/lede-buildroot
https://raw.githubusercontent.com/njhsi/dockerfiles/master/lede-
buildroot/Dockerfile"  
LABEL CMDRUN="docker run njhsi/lede-buildroot"  
  
MAINTAINER njhsi  
  
ENV DEBIAN_MIRROR http://mirrors.163.com/debian  
ENV DEBIAN_SECURITY http://security.debian.org/  
  
RUN echo "deb $DEBIAN_MIRROR stable main contrib" > /etc/apt/sources.list  
RUN echo "deb $DEBIAN_SECURITY stable/updates main contrib" >> \  
/etc/apt/sources.list  
RUN echo "deb $DEBIAN_MIRROR stable-updates main contrib" >> \  
/etc/apt/sources.list  
  
# gettext for envsubst  
RUN apt-get update && \  
apt-get install -yq git-core build-essential libssl-dev libncurses5-dev unzip
gawk \  
zlib1g-dev flex gettext wget subversion file python2.7-dev automake bison
patchelf findutils \  
sudo squashfs-tools && \  
apt-get clean  
  
RUN adduser --disabled-password --gecos '' \--shell /bin/bash --home /lede
buildman  
RUN adduser buildman sudo  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
USER buildman  
WORKDIR /lede  
  
#ENTRYPOINT ["/setup.sh"]  

