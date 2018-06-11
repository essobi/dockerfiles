FROM alpine:latest  
  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk update \  
&& apk add --no-cache \  
bash \  
file \  
build-base \  
make \  
g++ \  
autoconf \  
automake \  
libtool \  
boost \  
boost-dev \  
crypto++@testing \  
crypto++-dev@testing \  
zeromq@testing \  
zeromq-dev@testing \  
libzmq@testing \  
libsodium \  
libsodium-dev \  
git  
  
WORKDIR /build  
RUN git clone git://github.com/zeromq/czmq.git \  
&& cd czmq \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install  
  
WORKDIR /build  
RUN git clone git://github.com/zeromq/zyre.git \  
&& cd zyre \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install  
  
WORKDIR /build/tdrs  
ADD . .  
RUN autoreconf -fi \  
&& ./configure \  
&& make \  
&& mv ./tdrs /usr/local/bin/tdrs \  
&& mv ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh \  
&& chmod +x /usr/local/bin/docker-entrypoint.sh \  
&& make clean  
  
WORKDIR /  
RUN rm -Rf /build/czmq /build/zyre /build/tdrs/src /build/tdrs/m4
/build/tdrs/ext \  
&& apk del \  
file \  
build-base \  
make \  
g++ \  
autoconf \  
automake \  
libtool \  
git  
  
CMD ["/usr/local/bin/docker-entrypoint.sh"]  

