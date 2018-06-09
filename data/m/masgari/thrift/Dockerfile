FROM dockerfile/java  
  
MAINTAINER Mamad Asgari <mammad.asgari@gmail.com>  
  
# non interactive apt  
ENV DEBIAN_FRONTEND noninteractive  
  
# upgrade  
RUN apt-get -q -y update \  
&& apt-get -q -y install ant python-dev libboost-dev libboost-test-dev
libboost-program-options-dev libevent-dev \  
automake libtool flex bison pkg-config g++ libssl-dev sed make \  
&& mkdir /opt/thrift && cd /opt/thrift \  
&& wget http://archive.apache.org/dist/thrift/0.8.0/thrift-0.8.0.tar.gz \  
&& tar xvzf thrift-0.8.0.tar.gz \  
&& cd thrift-0.8.0 \  
&& ./configure && make -j 2 && make install && ldconfig \  
&& cd / && rm -fr /opt/thrift \  
&& apt-get -q -y clean && rm -rf /var/cache/apt/archives/*
/var/lib/apt/lists/* && rm -fr /tmp/*  
  
  
# hack Thrift  
RUN sed -i '/#ifdef HAVE_NETINET_IN_H/ i\\#define HAVE_NETINET_IN_H 1'
/usr/local/include/thrift/Thrift.h \  
&& sed -i '/#ifdef HAVE_INTTYPES_H/ i\\#define HAVE_INTTYPES_H 1'
/usr/local/include/thrift/Thrift.h  
  
CMD ["/usr/local/bin/thrift", "--help"]  

