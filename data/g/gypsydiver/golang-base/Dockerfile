FROM golang:1.7.4-alpine  
MAINTAINER Fernando Mendoza <fernando@agavelab.com>  
  
ARG PROTOBUF_VER=3.1.0  
RUN apk add -U autoconf automake bash curl g++ gcc git libtool make \  
&& curl -#L https://github.com/google/protobuf/archive/v${PROTOBUF_VER}.zip >>
${PROTOBUF_VER}.zip \  
&& unzip -q ${PROTOBUF_VER}.zip \  
&& cd protobuf-${PROTOBUF_VER} \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr --disable-shared \  
&& make \  
&& make check \  
&& make install \  
&& apk del autoconf automake libtool \  
&& cd $GOPATH \  
&& rm -rf ${PROTOBUF_VER}.zip protobuf-${PROTOBUF_VER}  

