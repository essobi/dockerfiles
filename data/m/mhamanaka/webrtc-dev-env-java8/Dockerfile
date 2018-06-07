# Ubuntu 16.04 LTS with WebRTC development environment.  
# version 0.0.1  
  
# Ubuntu 16.04 LTS.  
FROM ubuntu:xenial  
  
MAINTAINER David Chen <ksb2go@gmail.com>  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-
set-selections  
  
RUN apt-get update && \  
apt-get -y install software-properties-common python-software-properties \  
bzip2 unzip git build-essential pkg-config aptitude dpkg  
  
# Install openjdk and openjre 8 stuff  
RUN apt-get update && apt-get -y install openjdk-8-jre openjdk-8-jdk
openjdk-8-jre-headless  
  
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list  
RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list  
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ xenial-updates multiverse" >>
/etc/apt/sources.list  
RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ xenial-updates multiverse"
>> /etc/apt/sources.list  
  
RUN dpkg --add-architecture i386 && apt-get update  
  
RUN aptitude install -y g++-arm-linux-gnueabihf  
  
# Install Chromium dev packages.  
RUN apt-get update && apt-get install -y apache2-bin bison cdbs curl \  
dpkg-dev elfutils devscripts fakeroot \  
flex fonts-thai-tlwg g++ git-core git-svn gperf language-pack-da \  
language-pack-fr language-pack-he language-pack-zh-hant \  
libapache2-mod-php libasound2-dev libbrlapi-dev libav-tools \  
libbz2-dev libcairo2-dev libcap-dev libcups2-dev libcurl4-gnutls-dev \  
libdrm-dev libelf-dev libexif-dev libffi-dev libgconf2-dev \  
libglib2.0-dev libglu1-mesa-dev libgnome-keyring-dev libgtk2.0-dev \  
libkrb5-dev libnspr4-dev libnss3-dev libpam0g-dev libpci-dev \  
libpulse-dev libsctp-dev libspeechd-dev libsqlite3-dev libssl-dev \  
libudev-dev libwww-perl libxslt1-dev libxss-dev libxt-dev libxtst-dev \  
openbox patch perl php-cgi pkg-config python python-cherrypy3 \  
python-crypto python-dev python-numpy python-opencv python-openssl \  
python-psutil python-yaml rpm ruby subversion \  
fonts-ipafont wdiff \  
zip libbluetooth-dev libxkbcommon-dev realpath ttf-mscorefonts-installer \  
libjpeg-dev libbrlapi0.6  
  
# 64-bit systems need a minimum set of 32-bit compat packages for the pre-
built  
# NaCl binaries.  
RUN apt-get install -y libc6-i386 lib32gcc1 lib32stdc++6 \  
# Chromium runtime libs  
libatk1.0-0 libc6 libasound2 libcairo2 libcap2 libcups2 libexpat1 \  
libexif12 libffi6 libfontconfig1 libfreetype6 libglib2.0-0 \  
libgnome-keyring0 libgtk2.0-0 libpam0g libpango1.0-0 libpci3 libpcre3 \  
libpixman-1-0 libpng12-0 libspeechd2 libstdc++6 libsqlite3-0 libx11-6 \  
libxau6 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxdmcp6 \  
libxext6 libxfixes3 libxi6 libxinerama1 libxrandr2 libxrender1 \  
libxtst6 zlib1g libpulse0 libbz2-1.0 libnspr4 libnss3 libudev1 \  
# Debugging symbols for runtime libs.  
libatk1.0-dbg libc6-dbg libcairo2-dbg libffi6-dbg libfontconfig1-dbg \  
libglib2.0-0-dbg libgtk2.0-0-dbg libpango1.0-0-dbg libpcre3-dbg \  
libpixman-1-0-dbg libsqlite3-0-dbg libx11-6-dbg libxau6-dbg \  
libxcb1-dbg libxcomposite1-dbg libxcursor1-dbg libxdamage1-dbg \  
libxdmcp6-dbg libxext6-dbg libxfixes3-dbg libxi6-dbg libxinerama1-dbg \  
libxrandr2-dbg libxrender1-dbg libxtst6-dbg zlib1g-dbg libstdc++6-4.8-dbg  
  
# 32-bit libraries needed e.g. to compile V8 snapshot for Android or armhf  
RUN apt-get install -y linux-libc-dev:i386 \  
# arm cross toolchain packages needed to build chrome on armhf  
libc6-dev-armhf-cross linux-libc-dev-armhf-cross g++-4.8-multilib \  
g++-4.8-multilib-arm-linux-gnueabihf gcc-4.8-multilib-arm-linux-gnueabihf \  
# Packages to build NaCl, its toolchains, and its ports.  
g++-mingw-w64-i686 lib32z1-dev \  
libasound2:i386 libcap2:i386 libelf-dev:i386 libexif12:i386 \  
libfontconfig1:i386 libgconf-2-4:i386 libglib2.0-0:i386 libgpm2:i386 \  
libgtk2.0-0:i386 libncurses5:i386 lib32ncurses5-dev \  
libnss3:i386 libpango1.0-0:i386 \  
libssl1.0.0:i386 libtinfo-dev libtinfo-dev:i386 libtool \  
libxcomposite1:i386 libxcursor1:i386 libxdamage1:i386 libxi6:i386 \  
libxrandr2:i386 libxss1:i386 libxtst6:i386 texinfo xvfb \  
ant autoconf cmake gawk intltool xutils-dev xsltproc \  
libudev1:i386 \  
# Mesa development  
libgbm-dev libgl1-mesa-dev libgl1-mesa-glx:i386 \  
mesa-common-dev libgles2-mesa-dev  
  
RUN apt-get install -y ca-certificates-java desktop-file-utils dosfstools \  
fonts-dejavu-extra fuse gdisk gvfs gvfs-common gvfs-daemons gvfs-libs \  
libatasmart4 libatk-wrapper-java libatk-wrapper-java-jni libavahi-glib1 \  
libbonobo2-0 libbonobo2-common libcanberra0 libfuse2 libgconf2-4 libgnome2-0 \  
libgnome2-bin libgnome2-common libgnomevfs2-0 libgnomevfs2-common \  
liborbit-2-0 liborbit2 libpcsclite1 \  
libsecret-1-0 libsecret-common libtdb1 libudisks2-0 libvorbisfile3 ntfs-3g \  
parted policykit-1-gnome sound-theme-freedesktop udisks2  
  
# a bit of utilities  
RUN apt-get install -y tmux vim  
  
# Export JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
# Add script for sync Chromium repo  
ADD gclient.webrtc /home/root/scripts/gclient.webrtc  
ADD sync-chromium.sh /home/root/scripts/sync-chromium.sh  
ADD fetch-webrtc.sh /home/root/scripts/fetch-webrtc.sh  
ADD build-webrtc-unity.sh /home/root/scripts/build-webrtc-unity.sh  
  
# Add user docker. Change to the user you want if needed.  
# RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker
sudo  
# USER docker  
  
ENV HOME /home/root  
WORKDIR /home/root  
  
# clone Chromium depot_tools  
RUN mkdir -p /home/root/depot_tools  
RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git  
ENV DEPOT_TOOLS /home/root/depot_tools  
ENV PATH $PATH:$DEPOT_TOOLS  
  
# Run bash.  
CMD /bin/bash  

