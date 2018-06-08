FROM ubuntu:xenial  
  
RUN apt-get -qq update \  
&& apt-get -qq upgrade -y \  
&& apt-get -qq install -y locales  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV PROTOBUF_VERSION 3.5.0  
RUN apt-get -qq install -y dh-autoreconf make gcc unzip \  
  
&& curl -L
https://github.com/google/protobuf/archive/v$PROTOBUF_VERSION.tar.gz | gunzip
-c | tar x \  
&& cd protobuf-$PROTOBUF_VERSION \  
&& ./autogen.sh \  
&& ./configure \  
&& make install \  
&& cd .. \  
  
&& apt-get -qq autoremove -y dh-autoreconf make gcc \  
&& apt-get -qq clean -y \  
&& apt-get -qq purge -y \  
&& rm -fR /var/cache/apt/archives/*.deb /tmp/* /protobuf-*  
  
ADD protoc.sh /usr/local/bin/  
  
WORKDIR /work/in  
ENTRYPOINT ["protoc.sh"]  
CMD ["--help"]  

