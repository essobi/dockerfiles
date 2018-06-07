FROM debian  
MAINTAINER tattsun<t.t.mc1192.sf@gmail.com>  
  
# install cpp environment  
RUN apt-get -y update && apt-get -y install make binutils g++ automake
autoconf libtool cmake  
  
# install cpputest  
RUN apt-get -y update && apt-get -y install cpputest  
  
# install dependencies  
RUN apt-get -y update && apt-get -y install libevent-dev  
  
# install boost  
RUN apt-get -y update && apt-get -y install libboost-all-dev

