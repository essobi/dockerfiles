FROM alpine:latest  
MAINTAINER Guus Kuiper  
ENV SYSTEMC_VERSION 2.3.0  
  
RUN apk --no-cache add build-base cmake bash  
RUN apk --no-cache add --virtual build-deps curl tar \  
&& mkdir -p /usr/src/systemc \  
&& curl
http://accellera.org/images/downloads/standards/systemc/systemc-$SYSTEMC_VERSION.tgz
| tar -xzC /usr/src/systemc \  
&& cd /usr/src/systemc/systemc-$SYSTEMC_VERSION \  
&& mkdir objdir \  
&& cd objdir \  
&& export CXX=g++ \  
&& mkdir -p /usr/local/systemc-$SYSTEMC_VERSION \  
&& ../configure --prefix=/usr/local/systemc-$SYSTEMC_VERSION \  
&& make \  
&& make install \  
&& make check \  
&& cd / \  
&& rm -rf /usr/src/systemc \  
&& apk del build-deps  

