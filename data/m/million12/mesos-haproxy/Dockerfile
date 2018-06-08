FROM million12/centos-supervisor  
MAINTAINER Przemyslaw Ozgo linux@ozgo.info, Marcin Ryzycki marcin@m12.io  
  
COPY container-files /  
  
ENV MARATHON_ADDRESS 127.0.0.1  
ENV MARATHON_PORT 8080  
RUN \  
yum install -y haproxy cronie sudo && \  
yum clean all && \  
chmod 755 haproxy-marathon-bridge  
  
EXPOSE 80 443  

