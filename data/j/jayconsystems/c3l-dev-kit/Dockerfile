FROM debian:jessie  
MAINTAINER Shawn Nock <nock@nocko.se>  
  
RUN gpg --keyserver pool.sks-keyservers.net \  
\--recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
git \  
subversion \  
build-essential \  
unzip \  
libncurses5-dev \  
libz-dev \  
flex \  
intltool \  
wget \  
gettext \  
gawk \  
python \  
rsync \  
man-db \  
openssh-client && \  
rm -rf /var/lib/apt/lists/* && \  
wget -O /usr/local/bin/gosu \  
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" && \  
wget -O /usr/local/bin/gosu.asc \  
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" && \  
gpg --verify /usr/local/bin/gosu.asc && \  
rm /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu && \  
apt-get purge -y --auto-remove  
  
ENV USER openwrt  
ENV UID 1000  
RUN useradd -m -u $UID $USER  
ENV HOME /home/$USER  
ENV REPO_PATH $HOME/openwrt  
WORKDIR $HOME  
  
RUN mkdir $REPO_PATH  
  
WORKDIR $REPO_PATH  
CMD gosu $USER /bin/bash  

