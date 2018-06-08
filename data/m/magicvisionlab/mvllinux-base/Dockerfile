FROM ubuntu:14.04  
MAINTAINER ueck@net-labs.de  
ENV DEBIAN_FRONTEND noninteractive  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
# LOCAL BUILD ONLY - USE AptProxy  
#RUN echo "Use Localhost as AptProxy http://"`netstat -nr | grep
'^0\\.0\\.0\\.0' | awk '{print $2}'`":3142"  
#RUN echo 'Acquire::http { Proxy "http://'`netstat -nr | grep '^0\\.0\\.0\\.0'
| awk '{print $2}'`':3142"; };' | sudo tee /etc/apt/apt.conf.d/02proxy  
# enable ubuntu extras  
RUN echo deb http://extras.ubuntu.com/ubuntu trusty main >>
/etc/apt/sources.list;\  
echo deb-src http://extras.ubuntu.com/ubuntu trusty main >>
/etc/apt/sources.list;\  
apt-get update;  
  
  
## install ubuntu packages  
RUN apt-get update; \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3E5C1192; \  
apt-get update; apt-get upgrade -y  
  
  
# install basic development tools  
RUN apt-get install -y \  
software-properties-common \  
python-software-properties \  
python2.7-dev \  
python-distribute \  
python-pip \  
build-essential \  
devscripts \  
supervisor \  
wget  
  
RUN pip --no-input --exists-action=w install --upgrade pip  
  
# Fake a fuse install, since build cannot run in privileged mode  
RUN apt-get install libfuse2 && \  
cd /tmp ; apt-get download fuse && \  
cd /tmp ; dpkg-deb -x fuse_* . && \  
cd /tmp ; dpkg-deb -e fuse_* && \  
cd /tmp ; rm fuse_*.deb && \  
cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst && \  
cd /tmp ; dpkg-deb -b . /fuse.deb && \  
cd /tmp ; dpkg -i /fuse.deb  
# end hack  
# install oracle java 1.7  
WORKDIR /tmp  
RUN wget --progress=bar --no-check-certificate -O
/tmp/jdk-7u60-linux-x64.tar.gz \  
\--header "Cookie: oraclelicense=a" http://download.oracle.com/otn-
pub/java/jdk/7u60-b19/jdk-7u60-linux-x64.tar.gz && \  
tar xzf /tmp/jdk-7u60-linux-x64.tar.gz && \  
mkdir -p /usr/lib/jvm/java-7-oracle && \  
mv jdk1.7.0_60/jre /usr/lib/jvm/java-7-oracle/jre && \  
mv jdk1.7.0_60/lib /usr/lib/jvm/java-7-oracle/lib && \  
mv jdk1.7.0_60/include /usr/lib/jvm/java-7-oracle/include && \  
mv jdk1.7.0_60/bin /usr/lib/jvm/java-7-oracle/bin && \  
mv jdk1.7.0_60/man /usr/lib/jvm/java-7-oracle/man && \  
mv jdk1.7.0_60/db /usr/lib/jvm/java-7-oracle/db && \  
rm -rf jdk1.7.0_60 && rm /tmp/jdk-7u60-linux-x64.tar.gz && \  
chown root:root -R /usr/lib/jvm/java-7-oracle && \  
update-alternatives --install /usr/bin/java java
/usr/lib/jvm/java-7-oracle/jre/bin/java 1 && \  
update-alternatives --set java /usr/lib/jvm/java-7-oracle/jre/bin/java  
# end oracle java installation  
# install basic packages for magicvisionlab development  
RUN apt-get install -y \  
libzmq-dev \  
libboost-all-dev \  
libatlas-dev \  
libavcodec-dev \  
libavformat-dev \  
libblas-dev \  
libbullet-dev \  
libflann-dev \  
libeigen3-dev \  
libexpat1-dev \  
libfreeimage-dev \  
libhdf5-dev \  
libjpeg-dev \  
liblapack-dev \  
libprotobuf-dev \  
libmsgpack-dev \  
libqhull-dev \  
libreadline-dev \  
libtbb-dev \  
zlib1g-dev \  
vim \  
vim-scripts \  
wget \  
ctags \  
gdb \  
gpm \  
git \  
rsync \  
git-man \  
subversion \  
bzr \  
mercurial \  
binutils-gold \  
cmake \  
cmake-curses-gui \  
python-numpy \  
python-scipy \  
swig \  
ant  
  
# CLEANUP LOCAL PROXY  
#RUN rm -f /etc/apt/apt.conf.d/02proxy  

