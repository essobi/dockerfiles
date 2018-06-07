FROM debian:sid  
  
WORKDIR /opt  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -q update && apt-get -qy install \  
wget \  
build-essential \  
libcurl4-openssl-dev libev-dev libxml2-dev libjansson-dev pkg-config \  
libcunit1 zlib1g-dev libjemalloc-dev libevent-openssl-2.0-5 libssh2-1-dev \  
libssl-dev libxml2-dev make autoconf automake autotools-dev libtool \  
libboost-dev libboost-thread-dev libboost-iostreams-dev \  
&& apt-get -qy autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* \  
\  
&& wget
https://github.com/nghttp2/nghttp2/releases/download/v1.26.0/nghttp2-1.26.0.tar.gz
&& tar -zxvf nghttp2* && rm -f *.gz \  
&& wget https://curl.haxx.se/download/curl-7.56.0.tar.gz && tar -zxvf curl* &&
rm -f *.gz \  
&& cd /opt/nghttp2* && ./configure && make -j4 && make install && ldconfig \  
&& cd /opt/curl* && ./configure --disable-shared --enable-static && make -j4
&& make install && ldconfig \  
&& rm -rf /opt/*  
  
CMD /usr/local/bin/curl  

