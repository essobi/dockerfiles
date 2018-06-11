FROM ubuntu:14.04  
MAINTAINER xujintao <xujintao@126.com>  
  
# prepare dev environment  
RUN echo "===>update apt repository list" && apt-get -y update && \  
echo "===>install software-properties-common" && apt-get -y install software-
properties-common && \  
  
# add toolchain repo  
echo "===>add ubuntu toolchain repository" && apt-add-repository -y
"ppa:ubuntu-toolchain-r/test" && \  
echo "===>update apt source list again" && apt-get -y update && \  
echo "===>install toolchain " && apt-get -y install gcc-7 g++-7 && \  
echo "===>create toolchain soft link" && ln -s /usr/bin/gcc-7 /usr/bin/gcc -f
&& ln -s /usr/bin/g++-7 /usr/bin/g++ -f && \  
  
# install make and wget  
echo "===>install make" && apt-get -y install make && \  
echo "===>install wget" && apt-get -y install wget && \  
  
# install boost  
# echo "===>install boost" && apt-get -y install libboost-all-dev && \  
echo "===>install boost" && apt-get -y install libboost-log1.54-dev \  
libboost-system1.54-dev \  
libboost-thread1.54-dev \  
libboost-filesystem1.54-dev && \  
  
# install mysql-connector-c++  
echo "===>wget mysql-connector-c++-1.1.9" && wget -q \  
https://dev.mysql.com/get/Downloads/Connector-C++/mysql-
connector-c++-1.1.9-linux-ubuntu14.04-x86-64bit.tar.gz && \  
echo "===>print pwd" && pwd && \  
echo "===>ls -al" && ls -al && \  
echo "===>tar connector and cd" && tar -xzf mysql-connector-c++-1.1.9-linux-
ubuntu14.04-x86-64bit.tar.gz && \  
echo "===>cp libs" && cp -drf mysql-connector-c++-1.1.9-linux-
ubuntu14.04-x86-64bit/lib/* /usr/lib && \  
  
# clean  
echo "===>rm apt repository and tmp files" && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/temp/*  
  
WORKDIR "/project"  
CMD ./build.sh

