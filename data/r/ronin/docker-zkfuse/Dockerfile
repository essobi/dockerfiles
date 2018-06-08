FROM ubuntu:16.04  
ARG VCS_REF  
ARG BUILD_DATE  
LABEL org.label-schema.description="Docker image providing zkfuse - FUSE
provider of ZK znode namespace" \  
org.label-schema.version="0.0.3" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/ronin13/docker-zkfuse" \  
org.label-schema.build-date=$BUILD_DATE  
MAINTAINER Raghavendra Prabhu <me@rdprabhu.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y install git libboost-dev gcc g++ autotools-
dev autoconf libtool ant openjdk-8-jdk-headless make liblog4cxx-dev libfuse-
dev gawk libcppunit-dev fuse  
  
RUN git clone \--depth=1 https://github.com/apache/zookeeper  
  
WORKDIR /zookeeper  
  
RUN ant compile_jute  
  
WORKDIR /zookeeper/src/c  
  
RUN autoreconf -if && ./configure --without-cppunit && make && make install  
  
WORKDIR ../contrib/zkfuse  
  
RUN autoreconf -if && ./configure --without-cppunit && make  
  
RUN install -m0755 ./src/zkfuse /usr/bin/  
  
RUN /sbin/ldconfig  
  
VOLUME /zkmount  
  
WORKDIR /  
  
CMD ["/usr/bin/zkfuse", "--help"]  

