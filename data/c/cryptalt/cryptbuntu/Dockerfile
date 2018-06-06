#FROM saltstack/ubuntu-14.04-minimal  
FROM library/ubuntu:14.04  
MAINTAINER cryptalt  
  
RUN sudo apt-get -y update && \  
sudo apt-get -y upgrade && \  
sudo apt-get -y dist-upgrade && \  
sudo apt-get -y install software-properties-common python-software-properties  
  
RUN add-apt-repository -y ppa:bitcoin/bitcoin && \  
apt-get -y update  
  
RUN sudo apt-get -y install software-properties-common nano libboost-all-dev
libzmq3-dev libminiupnpc-dev libssl-dev libevent-dev && \  
sudo apt-get -y install build-essential libtool automake autoconf && \  
sudo apt-get -y install autotools-dev autoconf pkg-config libssl-dev && \  
sudo apt-get -y install libgmp3-dev libevent-dev bsdmainutils libboost-all-dev
&& \  
sudo apt-get -y install libdb4.8-dev libdb4.8++-dev && \  
sudo apt-get -y install libminiupnpc-dev  
  
#RUN sudo apt-get -y install git  
#RUN mkdir -p /tmp/desire && \  
# cd /tmp/desire && \  
# git clone https://github.com/lazyboozer/Desire.git && \  
# cd Desire && \  
# chmod 755 autogen.sh && \  
# ./autogen.sh && \  
# ./configure && \  
# chmod 755 share/genbuild.sh && \  
# make  

