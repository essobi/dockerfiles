from ubuntu:latest  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y software-properties-common && \  
apt-get install -y curl vim wget git && \  
apt-get install -y libc6-dev g++-multilib python pwgen  
RUN \  
apt-get install -y build-essential pkg-config libcurl3-gnutls-dev libc6-dev
libevent-dev m4 g++-multilib autoconf libtool ncurses-dev unzip git python
zlib1g-dev wget bsdmainutils automake libboost-all-dev libssl-dev libprotobuf-
dev protobuf-compiler libqt4-dev libqrencode-dev libdb++-dev ntp ntpdate less  
RUN \  
add-apt-repository ppa:bitcoin/bitcoin &&\  
apt-get update &&\  
apt-get install -y libdb4.8-dev libdb4.8++-dev libleveldb-dev  

