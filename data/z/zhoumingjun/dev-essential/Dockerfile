  
FROM debian:jessie  
  
MAINTAINER zhoumingjun <zhoumingjun@gmail.com>  
  
# Accecpt Oracle license before installing java  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
# Add java8 repo  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
  
#install dev essential packages  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
bison \  
build-essential \  
flex \  
g++ \  
git \  
libarchive-dev \  
libboost-dev \  
libboost-test-dev \  
libevent-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
liblua5.2-dev \  
libluajit-5.1-dev \  
libssl-dev \  
libtool \  
libunwind8-dev \  
lua5.2 \  
luajit \  
oracle-java8-installer \  
oracle-java8-set-default \  
pkg-config \  
python \  
zip \  
zlib1g-dev \  
libpcre3-dev  
  
#clean cache  
RUN apt-get clean  
RUN rm -rf /var/cache/oracle-jdk8-installer  
  
#export java_home  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
  
#=================== GOLANG ============================  
RUN wget https://storage.googleapis.com/golang/go1.5.linux-amd64.tar.gz && \  
tar -C /usr/local -zxf go1.5.linux-amd64.tar.gz  
  
ENV PATH $PATH:/usr/local/go/bin  
  
#=================== swig ============================  
RUN wget
http://downloads.sourceforge.net/project/swig/swig/swig-3.0.7/swig-3.0.7.tar.gz
&& \  
tar -xvf swig-3.0.7.tar.gz && \  
cd swig-3.0.7 && \  
./configure && \  
make && \  
make install  

