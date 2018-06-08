FROM ringo/docker-sbt:0.13.12  
  
ENV PROTOBUF_TAG v3.0.2  
  
RUN apk add \--no-cache --update git curl build-base autoconf automake libtool
g++ unzip make \  
&& git clone https://github.com/google/protobuf -b $PROTOBUF_TAG --depth 1 \  
&& cd ./protobuf \  
&& ./autogen.sh && ./configure --prefix=/usr && make && make check && make
install && make clean \  
&& cd ../ \  
&& rm -rf ./protobuf \  
&& apk del curl build-base autoconf automake libtool g++ unzip make \  
&& apk add \--no-cache --update libstdc++ \  
&& rm -rf /var/cache/apk/*  

