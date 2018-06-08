# buildpack-deps provides full batteries-included images. With them, a
majority of arbitrary  
# gem install / npm install / pip install should be successfull without
additional header/development  
# packages.  
#  
# SRC: https://hub.docker.com/_/buildpack-deps/  
# Set the base image to Ubuntu v15.10 (x64) OS.  
FROM ubuntu:15.10  
# Author or maintainer of this image file  
MAINTAINER Sachin Gupta <sachin.aut@gmail.com>  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  
  
# All packages must work in noninteractive mode.  
ENV DEBIAN_FRONTEND noninteractive  
RUN export DEBIAN_FRONTEND=noninteractive  
  
# Add add-apt-repository command  
RUN apt-get -qq update && apt-get install -qq -y --no-install-recommends \  
python-software-properties \  
apt-file \  
software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add All Package Source  
RUN add-apt-repository -y main && \  
add-apt-repository -y universe && \  
add-apt-repository -y restricted && \  
add-apt-repository -y multiverse  
  
# Update all installed packages  
RUN apt-get update -qq -y && \  
apt-get upgrade -qq -y && \  
apt-get dist-upgrade -qq -y && \  
apt-get -qq -y autoremove && \  
apt-get clean  
  
# Replication Of "buildpack-deps:xenial-curl" Package  
# https://github.com/docker-library/buildpack-
deps/blob/2da658b9a1b91fa61d63ffad2ea52685cac6c702/xenial/curl/Dockerfile  
RUN apt-get -qq -y update && apt-get install -qq -y --no-install-recommends \  
apt-utils \  
ca-certificates \  
curl \  
wget \  
sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
# Replication Of "buildpack-deps:xenial-scm" Package  
# procps is very common in build systems, and is a reasonably small package  
RUN apt-get -qq -y update && apt-get install -qq -y --no-install-recommends \  
bzr \  
git \  
mercurial \  
openssh-client \  
subversion \  
procps \  
&& rm -rf /var/lib/apt/lists/*  
  
# Replication Of "buildpack-deps:xenial" Package  
# https://github.com/docker-library/buildpack-
deps/blob/11492c68d993221fd5cd4d8a980354634fc165dd/xenial/Dockerfile  
# Also added many other essential packages  
RUN apt-get -qq -y update && apt-get install -qq -y --no-install-recommends \  
autoconf \  
automake \  
bzip2 \  
file \  
g++ \  
gcc \  
imagemagick \  
libbz2-dev \  
libc6-dev \  
libcurl4-openssl-dev \  
libdb-dev \  
libevent-dev \  
libffi-dev \  
libgdbm-dev \  
libgeoip-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libkrb5-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpng-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libxslt1-dev \  
libyaml-dev \  
make \  
patch \  
xz-utils \  
zlib1g-dev \  
build-essential \  
libqt4-webkit \  
libqt4-dev \  
xvfb \  
checkinstall \  
yum \  
gedit \  
&& rm -rf /var/lib/apt/lists/*  
  
#-------------------------------------------------------------------  
# Install Various Packages for ZIP / UnZip  
#-------------------------------------------------------------------  
# Install Various Packages for ZIP / UnZip  
RUN apt-get -qq -y update && apt-get install -qq -y --no-install-recommends \  
p7zip \  
p7zip-full \  
p7zip-rar \  
unace \  
unrar \  
zip \  
unzip \  
xz-utils \  
sharutils \  
rar \  
uudeview \  
mpack \  
arj \  
cabextract \  
file-roller \  
&& rm -rf /var/lib/apt/lists/*  
  
#-------------------------------------------------------------------  
# Print Current Directory  
#-------------------------------------------------------------------  
RUN echo "Current Directory Is:" && \  
pwd  
  
#-------------------------------------------------------------------  
# Cleanup Actions  
#-------------------------------------------------------------------  
# Remove redundant apt-get packages and all update information of packages to
reduce image size  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

