FROM ubuntu:16.04  
  
ARG FREETZ_SVN_URL=http://svn.freetz.org/trunk/  
ARG FREETZ_REVISION=13446  
  
RUN apt-get update \  
&& apt-get install -y \  
autoconf \  
automake \  
binutils \  
bison \  
bzip2 \  
ecj \  
fastjar \  
flex \  
g++ \  
gawk \  
gcc-multilib \  
gettext \  
git \  
graphicsmagick \  
imagemagick \  
intltool \  
lib32ncurses5-dev \  
lib32stdc++6 \  
libacl1-dev \  
libc6-dev-i386 \  
libcap-dev \  
libncurses5-dev \  
libreadline-dev \  
libstring-crc32-perl \  
libtool-bin \  
libtool \  
libusb-dev \  
make \  
patch \  
perl \  
pkg-config \  
python \  
realpath \  
ruby \  
ruby1.8 \  
subversion \  
texinfo \  
tofrodos \  
unzip \  
wget \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# Install freetz source tree  
WORKDIR /freetz  
RUN useradd -M -d /freetz -U freetz \  
&& chown freetz:freetz .  
USER freetz  
RUN svn checkout -r "${FREETZ_REVISION}" "${FREETZ_SVN_URL}" .  

