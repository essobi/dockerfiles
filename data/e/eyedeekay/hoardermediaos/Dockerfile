FROM debitux/devuan:unstable  
ARG DEBIAN_FRONTEND="noninteractive"  
ARG LANG="C.UTF-8"  
ARG LC_ALL="C.UTF-8"  
ARG CACHING_PROXY=""  
ENV DEBIAN_FRONTEND="noninteractive" LANG="C.UTF-8" LC_ALL="C.UTF-8"
CACHING_PROXY=""  
RUN adduser --disabled-password --home /home/livebuilder --shell /bin/bash
--disabled-password --gecos "livebuilder" livebuilder  
RUN adduser livebuilder sudo  
RUN sed -i 's|packages|us.mirror|' /etc/apt/sources.list && mkdir -p
/etc/apt/preferences.d  
RUN echo "deb http://us.mirror.devuan.org/devuan ascii main" | tee -a
/etc/apt/sources.list  
RUN apt-get update && apt-get install -yq --fix-missing --reinstall \  
apt-transport-https apt-utils iproute debconf  
RUN echo "Acquire::HTTP::Proxy \"$CACHING_PROXY\";" | tee -a
/etc/apt/apt.conf.d/01proxy  
RUN apt-get update && apt-get install -yq --fix-missing --reinstall \  
gnupg2 \  
bash \  
make \  
apt-utils \  
live-build \  
debootstrap \  
make \  
curl \  
sudo \  
procps \  
ca-certificates \  
devuan-keyring \  
debian-keyring \  
debian-archive-keyring \  
dirmngr \  
cpio \  
e2fsprogs \  
squashfs-tools \  
syslinux-common \  
less  
RUN echo 'livebuilder ALL=(ALL) NOPASSWD: ALL' | tee -a /etc/sudoers  
RUN chown -R livebuilder:livebuilder /home/livebuilder/  
WORKDIR /home/livebuilder/hoarder-live  
  

