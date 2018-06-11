FROM centos:centos7  
MAINTAINER "Travis Petticrew <tpetticrew@watermark.org>"  
  
RUN yum -y -q update \  
&& yum -y -q install less vim tree curl git socat htop tcpdump \  
&& yum clean all \  
&& rm -rf /build \  
&& rm -rf /tmp/* \  

