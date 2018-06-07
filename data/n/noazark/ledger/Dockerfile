FROM dockerfile/ubuntu  
MAINTAINER Noah H. Smith <noah@batteredoats.com>  
  
RUN \  
apt-get install -y \  
build-essential git make python \  
cmake libboost-system-dev libboost-dev libboost-date-time-dev \  
libboost-filesystem-dev libboost-iostreams-dev libboost-python-dev \  
libboost-regex-dev libgmp3-dev libmpfr-dev libboost-test-dev  
  
RUN \  
git clone https://github.com/ledger/ledger /tmp/ledger && \  
cd /tmp/ledger && \  
git submodule update --init && \  
./acprep make && \  
make check && \  
make install && \  
cd / && \  
rm -rf /tmp/ledger  
  
ADD ./.ledgerrc /root/.ledgerrc  
ENTRYPOINT ["ledger"]  

