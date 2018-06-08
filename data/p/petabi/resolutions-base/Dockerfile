FROM ubuntu:18.04  
  
MAINTAINER Atsuhiro Sean Suzuki <atsuzuki@petabi.com>  
  
ENV \  
PATH=$PATH:/usr/pkg/bin/:/usr/pkg/sbin \  
PKG_PATH=http://ftp.NetBSD.org/pub/pkgsrc/packages/Linux/x86_64/Ubuntu-18.04_head/All  
  
ADD
https://ftp.NetBSD.org/pub/pkgsrc/packages/Linux/x86_64/Ubuntu-18.04_head/bootstrap.tar.gz
/  
RUN \  
tar -zxpf /bootstrap.tar.gz -C / && \  
rm /bootstrap.tar.gz && \  
pkg_add pkg_alternatives  
  
RUN \  
pkg_add boost-libs grpc librdkafka sqlite3  

