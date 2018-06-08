FROM ubuntu:15.10  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y git curl cmake ninja-build clang uuid-dev libicu-dev
icu-devtools libbsd-dev libedit-dev libxml2-dev libsqlite3-dev swig libpython-
dev libncurses5-dev pkg-config  
RUN apt-get install -y clang-3.6  
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.6 100  
RUN update-alternatives --install /usr/bin/clang++ clang++
/usr/bin/clang++-3.6 100  
RUN curl -O
https://swift.org/builds/ubuntu1510/swift-2.2-SNAPSHOT-2015-12-22-a/swift-2.2-SNAPSHOT-2015-12-22-a-ubuntu15.10.tar.gz  
RUN tar -xzvf swift-2.2-SNAPSHOT-2015-12-22-a-ubuntu15.10.tar.gz  
RUN ln -s /swift-2.2-SNAPSHOT-2015-12-22-a-ubuntu15.10/usr/bin/*
/usr/local/bin/  

