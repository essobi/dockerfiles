FROM debian:stable  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y autoconf automake
autotools-dev libtool pkg-config zlib1g-dev libcunit1-dev libssl-dev
libxml2-dev libevent-dev curl lbzip2 make g++  
  
RUN curl -L -O
https://github.com/tatsuhiro-t/spdylay/releases/download/v1.3.2/spdylay-1.3.2.tar.bz2
\  
&& tar xf spdylay-1.3.2.tar.bz2 \  
&& cd spdylay-1.3.2 \  
&& autoreconf -i \  
&& automake \  
&& autoconf \  
&& ./configure \  
&& make  
  
CMD ["./spdylay-1.3.2/src/shrpx", "--accesslog", "-b", "web,80",
"/ssl/server.key", "/ssl/server.crt"]  

