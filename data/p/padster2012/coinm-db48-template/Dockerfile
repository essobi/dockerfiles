FROM debian:jessie  
  
# Environment variables  
ENV BERKELEY_VERSION48 4.8.30.NC  
  
ENV BERKELEY_LOC48 /usr/local/BerkeleyDB.4.8  
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
  
# Download, configure and install BerkeleyDB 4.8  
RUN wget -P /tmp http://download.oracle.com/berkeley-
db/db-"${BERKELEY_VERSION48}".tar.gz && \  
tar -xf /tmp/db-"${BERKELEY_VERSION48}".tar.gz -C /tmp && \  
rm -f /tmp/db-"${BERKELEY_VERSION48}".tar.gz && \  
cd /tmp/db-"${BERKELEY_VERSION48}"/build_unix && \  
../dist/configure --prefix="${BERKELEY_LOC48}" \--enable-cxx --disable-shared
--with-pic && make && make install  
  
RUN ls "${BERKELEY_LOC48}"  
  
# Create folders  
RUN mkdir /config  
RUN mkdir /rootcoinslocation  
RUN apt-get clean && apt-get autoclean  
#RUN git clone https://github.com/bitcoin/bitcoin.git
/rootcoinslocation/bitcoin \  
#&& cd /rootcoinslocation/bitcoin; ./autogen.sh; ./configure --without-gui
LDFLAGS="-L${BERKELEY_LOC48}/lib/" CPPFLAGS="-I${BERKELEY_LOC48}/include/";
make; make install  

