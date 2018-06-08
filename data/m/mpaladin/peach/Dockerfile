FROM ubuntu:16.04  
  
# Install Java:
https://github.com/dockerfile/java/blob/0dd4b2006cc83ead743e912ab1becfb1c34e0ce2/oracle-
java8/Dockerfile  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN \  
apt-get install -y \  
unzip \  
curl  
  
RUN \  
curl -LsS https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/sonar-scanner-cli-3.0.3.778.zip > sonar-scanner-cli.zip && \  
unzip -d /opt sonar-scanner-cli.zip  
  
# install dependencies (base from git, samba)  
RUN \  
apt-get update && \  
apt-get install -y \  
build-essential \  
autoconf \  
libcurl4-openssl-dev \  
libssl-dev \  
libexpat1-dev \  
gettext \  
python \  
python-dev \  
docbook-xsl \  
libgnutls-dev \  
libacl1-dev \  
libldap2-dev  
# samba  
RUN \  
apt-get install -y \  
libpam0g-dev \  
libjansson-dev \  
libgpgme11-dev \  
libarchive-dev  
# nginx  
RUN \  
apt-get install -y \  
libpcre3-dev  
# gcc  
RUN \  
apt-get install -y \  
flex  
# openjdk  
RUN \  
apt-get update && \  
apt-get install -y \  
mercurial \  
cpio \  
zip \  
libx11-dev libxext-dev libxrender-dev libxtst-dev libxt-dev \  
libasound2-dev  
# php  
RUN \  
apt-get install -y \  
bison \  
re2c \  
libxml2-dev  
# postgresql  
RUN \  
apt-get install -y \  
libreadline-dev  
# cmake  
RUN \  
apt-get install -y \  
cmake  
# mysql  
RUN \  
apt-get install -y \  
libncurses5-dev  
# binutils  
RUN \  
apt-get install -y \  
texinfo  
# httpd  
RUN \  
apt-get install -y \  
libtool-bin  
# CoreCLR  
RUN \  
apt-get install -y \  
llvm-3.9 \  
clang-3.9 \  
lldb-3.8 \  
lldb-3.8-dev \  
libunwind8 \  
libunwind8-dev \  
libicu-dev \  
liblttng-ust-dev \  
uuid-dev \  
git  
# linux kernel  
RUN \  
apt-get install -y \  
bc  
# ruby  
RUN \  
apt-get install -y \  
ruby-full  
# openldap  
RUN \  
apt-get install -y \  
groff  
# guetzli  
RUN \  
apt-get install -y \  
libpng-dev  
# install bazel  
RUN \  
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8"
| tee /etc/apt/sources.list.d/bazel.list && \  
curl https://bazel.build/bazel-release.pub.gpg | apt-key add - && \  
apt-get update && \  
apt-get install -y bazel  
# tensorflow  
RUN \  
apt-get install -y \  
python-numpy \  
python-wheel  
# mongo  
RUN \  
apt-get install -y \  
python-pip \  
python-virtualenv  
# busybox  
RUN \  
apt-get install -y \  
libcap-dev  
# tmux  
RUN apt-get install -y \  
libevent-dev  
# the_silver_searcher  
RUN apt-get install -y \  
liblzma-dev  
# Qt  
RUN apt-get install -y \  
libfontconfig1-dev \  
libfreetype6-dev \  
libx11-dev \  
libxext-dev \  
libxfixes-dev \  
libxi-dev \  
libxrender-dev \  
libxcb1-dev \  
libx11-xcb-dev \  
libxcb-glx0-dev \  
libxcb-keysyms1-dev \  
libxcb-image0-dev \  
libxcb-shm0-dev \  
libxcb-icccm4-dev \  
libxcb-sync0-dev \  
libxcb-xfixes0-dev \  
libxcb-shape0-dev \  
libxcb-randr0-dev \  
libxcb-render-util0-dev \  
libxcb-xinerama0-dev \  
gperf  
# firefox  
RUN apt-get install -y \  
libcairo2-dev \  
libpango1.0-dev \  
autoconf2.13 \  
libgtk2.0-dev \  
libgtk-3-dev \  
libgconf2-dev \  
libdbus-glib-1-dev \  
libpulse-dev \  
yasm  
# v8  
RUN apt-get install -y \  
ninja-build  
# libreoffice  
RUN apt-get install -y \  
libxslt1-dev \  
xsltproc \  
python3-dev \  
libgl1-mesa-dev \  
doxygen \  
libcups2-dev \  
ant \  
junit4  
# webkit  
RUN apt-get install -y \  
libgcrypt11-dev \  
libjpeg62-dev \  
libsoup2.4-dev \  
libsqlite3-dev \  
libsecret-1-dev \  
libgeoclue-dev \  
libgirepository1.0-dev \  
libenchant-dev \  
libnotify-dev \  
libhyphen-dev \  
libgstreamer1.0-dev \  
libgstreamer-plugins-base1.0-dev \  
libwebp-dev  
# ceph  
RUN apt-get install -y \  
libudev-dev \  
libaio-dev \  
libblkid-dev \  
libleveldb-dev \  
libsnappy-dev \  
libkeyutils-dev \  
libnss3-dev \  
libbabeltrace-dev \  
libbabeltrace-ctf-dev \  
cython  
# facebook hhvm  
RUN apt-get install -y \  
autoconf automake binutils-dev bison build-essential cmake g++ gawk git \  
libboost-dev libboost-filesystem-dev libboost-program-options-dev libboost-
regex-dev \  
libboost-system-dev libboost-thread-dev libboost-context-dev libbz2-dev libc-
client-dev libldap2-dev \  
libc-client2007e-dev libcap-dev libcurl4-openssl-dev libdwarf-dev libelf-dev \  
libexpat-dev libgoogle-glog-dev libgoogle-perftools-dev libicu-dev \  
libjemalloc-dev libmcrypt-dev libmemcached-dev libmysqlclient-dev libncurses-
dev \  
libonig-dev libpcre3-dev libreadline-dev libtbb-dev libtool libxml2-dev
zlib1g-dev \  
libevent-dev libmagickwand-dev libinotifytools0-dev libiconv-hook-dev libedit-
dev \  
libiberty-dev libxslt1-dev ocaml-native-compilers libsqlite3-dev libyaml-dev
libgmp3-dev \  
gperf libkrb5-dev libnotify-dev libpq-dev  
  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV PATH /opt/sonar-scanner-3.0.3.778/bin/:$PATH  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN useradd -d /tmp -u 1300 -s /bin/bash cfamily  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

