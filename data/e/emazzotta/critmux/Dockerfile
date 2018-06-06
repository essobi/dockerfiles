FROM ubuntu:17.04  
ENV CRIU 2.11.1  
ENV TERM xterm-256color  
  
RUN mkdir /src  
WORKDIR /src  
RUN apt-get -q update  
  
RUN apt-get -qy install apt-utils  
RUN apt-get -qy install bash  
RUN apt-get -qy install bc  
RUN apt-get -qy install bridge-utils  
RUN apt-get -qy install bsdmainutils  
RUN apt-get -qy install build-essential  
RUN apt-get -qy install cmake  
RUN apt-get -qy install curl  
RUN apt-get -qy install curl  
RUN apt-get -qy install docker  
RUN apt-get -qy install gcc  
RUN apt-get -qy install git  
RUN apt-get -qy install golang  
RUN apt-get -qy install htop  
RUN apt-get -qy install jq  
RUN apt-get -qy install libaio-dev  
RUN apt-get -qy install libcap-dev  
RUN apt-get -qy install libncurses5-dev  
RUN apt-get -qy install libnet-dev  
RUN apt-get -qy install libnl-3-dev  
RUN apt-get -qy install libprotobuf-c0-dev  
RUN apt-get -qy install libprotobuf-dev  
RUN apt-get -qy install libreadline6-dev  
RUN apt-get -qy install linux-headers-generic  
RUN apt-get -qy install make  
RUN apt-get -qy install mono-xbuild  
RUN apt-get -qy install npm  
RUN apt-get -qy install pkg-config  
RUN apt-get -qy install postgresql  
RUN apt-get -qy install protobuf-c-compiler  
RUN apt-get -qy install protobuf-c-compiler  
RUN apt-get -qy install protobuf-compiler  
RUN apt-get -qy install python  
RUN apt-get -qy install python-dev  
RUN apt-get -qy install python-pip  
RUN apt-get -qy install python-protobuf  
RUN apt-get -qy install sed  
RUN apt-get -qy install sysstat  
RUN apt-get -qy install tmux  
RUN apt-get -qy install tmux  
RUN apt-get -qy install unzip  
RUN apt-get -qy install wget  
RUN apt-get -qy install zsh  
  
RUN curl -SL https://github.com/xemul/criu/archive/v$CRIU.tar.gz | tar xvz-  
RUN cd criu-$CRIU && \  
make && \  
make install-criu  
  
ADD wrapper /usr/local/sbin/  
CMD ["wrapper"]  

