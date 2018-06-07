FROM debian:wheezy  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends \  
build-essential wget unzip perl curl \  
libpcre3 libpcre3-dev libpcrecpp0 libssl-dev zlib1g-dev \  
procps libreadline-dev libncurses5-dev \  
libevent-dev libz-dev g++ libssl-dev uuid-dev \  
libpam0g libpam0g-dev gperf \  
libprotobuf-dev protobuf-compiler \  
libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-
iostreams-dev libboost-program-options-dev \  
libboost-regex-dev libboost-test-dev libboost-thread-dev libtool bison gettext
gperf intltool \  
libcurl4-gnutls-dev libgcrypt11-dev libmemcached-dev libv8-dev libcloog-ppl0 \  
python python-dev libzmq-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV DRIZZLE_VERSION 7.1.36  
  
WORKDIR /tmp  
RUN wget --no-check-certificate
https://launchpad.net/drizzle/7.1/${DRIZZLE_VERSION}/+download/drizzle-${DRIZZLE_VERSION}-stable.tar.gz
&& \  
tar xzf drizzle-${DRIZZLE_VERSION}-stable.tar.gz && \  
cd drizzle-${DRIZZLE_VERSION}-stable && \  
./configure && \  
make && \  
make install && \  
rm -rf /tmp/*  
  
RUN groupadd drizzle && useradd -g drizzle drizzle && \  
chown -R drizzle:drizzle /usr/local/var/drizzle  
  
ENV LD_LIBRARY_PATH /usr/local/lib  
CMD ["/usr/local/sbin/drizzled", "--user=drizzle", "--
datadir=/usr/local/var/drizzle/", "--drizzle-protocol.bind-address=0.0.0.0"]  

