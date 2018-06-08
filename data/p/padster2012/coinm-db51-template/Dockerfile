FROM debian:jessie  
  
# Environment variables  
ENV BERKELEY_VERSION51 5.1.29.NC  
ENV BERKELEY_LOC51 /usr/local/BerkeleyDB.5.1  
RUN apt-get -y update && apt-get -y install \  
wget \  
git \  
build-essential \  
libtool \  
autotools-dev \  
automake \  
pkg-config \  
libssl-dev \  
libevent-dev \  
bsdmainutils \  
libboost-system-dev \  
libboost-filesystem-dev \  
libboost-chrono-dev \  
libboost-program-options-dev \  
libboost-test-dev \  
libboost-thread-dev \  
libminiupnpc-dev  
  
# Download, configure and install BerkeleyDB 5.1  
RUN wget -P /tmp http://download.oracle.com/berkeley-
db/db-"${BERKELEY_VERSION51}".tar.gz && \  
tar -xf /tmp/db-"${BERKELEY_VERSION51}".tar.gz -C /tmp && \  
rm -f /tmp/db-"${BERKELEY_VERSION51}".tar.gz  
RUN cd /tmp/db-"${BERKELEY_VERSION51}"/build_unix && \  
../dist/configure --prefix="${BERKELEY_LOC51}" \--enable-cxx --disable-shared
--with-pic && make && make install  
  
RUN ls "${BERKELEY_LOC51}"  
  
# Create folders  
RUN mkdir /config  
RUN mkdir /rootcoinslocation  
RUN apt-get clean && apt-get autoclean  
#RUN git clone https://github.com/bitcoin/bitcoin.git
/rootcoinslocation/bitcoin \  
#&& cd /rootcoinslocation/bitcoin; ./autogen.sh; ./configure --without-gui
LDFLAGS="-L${BERKELEY_LOC48}/lib/" CPPFLAGS="-I${BERKELEY_LOC48}/include/";
make; make install  

