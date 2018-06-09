FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y build-essential \  
git software-properties-common python-software-properties  
  
RUN add-apt-repository ppa:bitcoin/bitcoin && apt-get update  
  
RUN apt-get install -y apt-utils libcap-dev libsqlite3-0 libpcap0.8 \  
libpcap-dev libseccomp-dev libdb4.8-dev libdb4.8++-dev libtool autotools-dev \  
automake pkg-config libssl-dev libevent-dev bsdmainutils git libboost-all-dev
\  
libminiupnpc-dev libqt5gui5 libqt5core5a libqt5webkit5-dev libqt5dbus5
qttools5-dev \  
qttools5-dev-tools libprotobuf-dev protobuf-compiler libqrencode-dev  
  
#verge  
RUN mkdir /root/VERGE  
RUN git clone https://github.com/vergecurrency/VERGE /root/VERGE  
RUN cd /root/VERGE/ && ./autogen.sh && ./configure && make  
# reduce images size  
RUN mv /root/VERGE/src/VERGEd /usr/local/bin/ && chmod 700
/usr/local/bin/VERGEd && rm -rf /root/VERGE  
  
WORKDIR /root/.VERGE  
  
EXPOSE 21102 20102  
CMD ["/usr/local/bin/VERGEd", "-printtoconsole"]  

