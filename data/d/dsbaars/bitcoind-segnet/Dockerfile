FROM ubuntu:16.04  
RUN apt-get update  
  
RUN apt-get install -y build-essential \  
libtool \  
autotools-dev \  
automake pkg-config \  
libssl-dev \  
libevent-dev \  
bsdmainutils \  
git-core  
  
RUN apt-get install -y libboost-system-dev \  
libboost-filesystem-dev \  
libboost-chrono-dev \  
libboost-program-options-dev \  
libboost-test-dev \  
libboost-thread-dev  
  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:bitcoin/bitcoin  
RUN apt-get update  
RUN apt-get install -y libdb4.8-dev libdb4.8++-dev libminiupnpc-dev
libzmq3-dev  
RUN apt-get install -y libprotobuf-dev  
  
RUN git clone https://github.com/sipa/bitcoin.git /opt/src  
ENV SRC /opt/src  
WORKDIR ${SRC}  
  
RUN git checkout segwit  
RUN ./autogen.sh && ./configure --with-boost-libdir=/usr/lib/x86_64-linux-gnu
--without-qt  
RUN make -j4  
RUN make install  
  
EXPOSE 8332 8333 18332 18333  
ENTRYPOINT ["bitcoind"]  
CMD ["-segnet", "-printtoconsole"]  

