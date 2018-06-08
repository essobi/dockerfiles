FROM ubuntu:16.04  
MAINTAINER bender.rodriges <bender.rodriges@gmail.com>  
  
ENV PROTOC_GEN_DOC_SOURCE
http://download.opensuse.org/repositories/home:estan:protoc-gen-
doc/xUbuntu_16.04  
ENV PROTOC_RELEASE_URL
https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip  
  
RUN apt-get update \  
&& apt-get install -y curl unzip \  
  
&& sh -c "echo 'deb $PROTOC_GEN_DOC_SOURCE/ /' >
/etc/apt/sources.list.d/protoc-gen-doc.list" \  
&& curl -sL -o Release.key $PROTOC_GEN_DOC_SOURCE/Release.key \  
&& apt-key add - < Release.key \  
  
&& curl -sL -o protoc3.zip $PROTOC_RELEASE_URL \  
&& unzip protoc3.zip -d protoc3 \  
&& mv protoc3/bin/protoc /usr/bin/protoc \  
&& mv protoc3/include/* /usr/include/ \  
  
&& apt-get update || true \  
&& apt-get install -y protoc-gen-doc \  
  
&& rm -rf Release.key protoc3.zip proto3 \  
&& apt-get purge -y curl unzip \  
&& apt-get autoremove -y \  
&& apt-get clean all \  
  
&& mkdir /src  
  
WORKDIR /src

