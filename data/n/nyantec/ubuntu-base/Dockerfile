FROM ubuntu:xenial  
MAINTAINER nyantec  
  
RUN apt-get -qq update; \  
apt-get -y install make sudo software-properties-common python-software-
properties; \  
apt-add-repository multiverse; \  
apt-get -qq update  
  
RUN apt-get -y install \  
autoconf \  
autoconf-archive \  
automake \  
build-essential \  
cabal-install \  
chrpath \  
clang-format-3.8 \  
cppcheck \  
curl \  
dia \  
diffstat \  
fonts-inconsolata \  
fonts-lato \  
fonts-lmodern \  
gawk \  
gcc-multilib \  
ghostscript \  
git \  
graphviz \  
happy \  
inkscape \  
libdbus-1-dev \  
libglib2.0-dev \  
libnl-3-dev \  
libnl-genl-3-dev \  
libnl-route-3-dev \  
libsdl1.2-dev \  
libsnmp-dev \  
libsqlite3-dev \  
libssl-dev \  
libsystemd-dev \  
libtool \  
optipng \  
pandoc \  
pkg-config \  
poppler-utils \  
python3-pip \  
python3-pygments \  
smitools \  
snmp-mibs-downloader \  
socat \  
texinfo \  
texlive \  
texlive-latex-extra \  
texlive-luatex \  
texlive-math-extra \  
texlive-xetex \  
unzip \  
wget \  
wireshark-dev \  
xterm \  
xzdec  
  
ADD install_pandoc.sh /tmp/install_pandoc.sh  
RUN /tmp/install_pandoc.sh  
  
ADD install_click.sh /tmp/install_click.sh  
RUN /tmp/install_click.sh  
  
ADD install_libsodium.sh /tmp/install_libsodium.sh  
RUN /tmp/install_libsodium.sh  
  
ADD install_rust.sh /tmp/install_rust.sh  
RUN /tmp/install_rust.sh  

