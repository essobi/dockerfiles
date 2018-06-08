FROM ubuntu:16.10  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y man curl vim git cmake ninja-build clang python uuid-
dev libicu-dev icu-devtools libbsd-dev libedit-dev libxml2-dev libsqlite3-dev
swig libpython-dev libncurses5-dev pkg-config libblocksruntime-dev openssl
libssl-dev libcurl4-openssl-dev lsb-release  
RUN apt-get -y install autoconf automake libtool unzip  
  
RUN curl -O https://swift.org/builds/development/ubuntu1610/swift-DEVELOPMENT-
SNAPSHOT-2017-01-16-a/swift-DEVELOPMENT-
SNAPSHOT-2017-01-16-a-ubuntu16.10.tar.gz  
RUN tar -xzvf swift-DEVELOPMENT-SNAPSHOT-2017-01-16-a-ubuntu16.10.tar.gz  
RUN rm swift-DEVELOPMENT-SNAPSHOT-2017-01-16-a-ubuntu16.10.tar.gz  
RUN ln -s /swift-DEVELOPMENT-SNAPSHOT-2017-01-16-a-ubuntu16.10/usr/bin/*
/usr/local/bin  
RUN echo /swift-DEVELOPMENT-SNAPSHOT-2017-01-16-a-ubuntu16.10/usr/lib >
/etc/ld.so.conf.d/swift.conf  
RUN ldconfig  
  
RUN git config --global user.email "you@example.com"  
RUN git config --global user.name "Your Name"  
RUN git clone https://github.com/apple/swift.git  
RUN cd swift && ./utils/update-checkout --clone \--tag swift-DEVELOPMENT-
SNAPSHOT-2017-01-16-a  
  
WORKDIR /home  

