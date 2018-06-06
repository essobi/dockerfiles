FROM httpd:2.4.25  
  
MAINTAINER Philip Schmid  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
gcc \  
libpcre3-dev \  
make \  
git \  
g++ \  
python \  
build-essential \  
libsasl2-2 \  
openssl \  
zlib1g-dev \  
zlibc \  
libhiredis-dev \  
libhiredis0.10 \  
libevent-dev \  
&& rm -r /var/lib/apt/lists/*  
  
RUN git config --global http.sslVerify false  
RUN git clone https://github.com/edenhill/librdkafka \  
&& cd librdkafka \  
&& ./configure \  
&& make \  
&& make install  
  
  
WORKDIR /opt  

