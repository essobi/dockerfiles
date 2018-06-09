  
FROM alpine:3.3  
MAINTAINER lulichn <daisuke.develop@gmail.com>  
  
RUN set -ex \  
&& apk --no-cache add --virtual \  
build-dependencies \  
curl \  
unzip \  
libtool \  
automake \  
autoconf \  
pkgconfig \  
g++ \  
make \  
flex \  
byacc  
  
RUN set -ex \  
&& apk --no-cache add --virtual \  
boost \  
libevent-dev  
  
# Build thrift 0.9.3  
RUN cd / \  
&& curl -o thrift-0.9.3.zip
https://codeload.github.com/apache/thrift/zip/0.9.3 \  
&& unzip thrift-0.9.3.zip \  
&& cd thrift-0.9.3/ \  
&& ./bootstrap.sh \  
&& ./configure --with-lua=no LDFLAGS=-fPIC CFLAGS=-fPIC CXXFLAGS=-fPIC
CPPFLAGS=-fPIC \  
&& make \  
&& make install \  
&& rm -rf /thrift-0.9.3.zip  
  
VOLUME /data  
WORKDIR /data  
  
CMD thrift  
  

