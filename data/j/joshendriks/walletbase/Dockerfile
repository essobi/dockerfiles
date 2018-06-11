FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install libboost-system1.58.0 libboost-filesystem1.58.0
libboost-program-options1.58.0 \  
libboost-thread1.58.0 libdb4.8 libdb4.8++ libssl1.0.0 \  
&& apt-get -y install git build-essential libtool autotools-dev automake \  
pkg-config libssl-dev libevent-dev bsdmainutils libboost-system-dev \  
libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev \  
libboost-test-dev libboost-thread-dev software-properties-common libgmp3-dev \  
&& add-apt-repository ppa:bitcoin/bitcoin \  
&& apt-get update \  
&& apt-get -y install libdb4.8-dev libdb4.8++-dev unzip  
  
RUN apt-get -y install g++-mingw-w64-i686 mingw-w64-i686-dev
g++-mingw-w64-x86-64 mingw-w64-x86-64-dev curl

