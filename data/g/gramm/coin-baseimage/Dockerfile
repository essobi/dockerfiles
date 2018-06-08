FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y nano git build-essential libtool
autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils \  
libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-
program-options-dev libboost-test-dev libboost-thread-dev software-properties-
common  
RUN add-apt-repository -y ppa:bitcoin/bitcoin && apt-get update && apt-get
install -y libdb4.8-dev libdb4.8++-dev libminiupnpc-dev libzmq3-dev && apt-get
clean  
  

