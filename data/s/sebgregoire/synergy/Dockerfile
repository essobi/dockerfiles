FROM ubuntu:15.04  
RUN apt-get install -yqq \  
cmake \  
make \  
g++ \  
xorg-dev \  
libqt4-dev \  
libcurl4-openssl-dev \  
libavahi-compat-libdnssd-dev \  
libssl-dev \  
python  
  
ADD . /usr/src/synergy  
  
WORKDIR /usr/src/synergy  
RUN ./configure && make all  

