FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y \  
curl \  
openjdk-8-jre-headless \  
unzip  
  
ENV LC_ALL=C.UTF-8  
RUN \  
mkdir /opt/overview && \  
curl https://overview-
builds.overviewdocs.com/4a00f39ec21122cc9171fb21da9ff285d4201f47.zip -o
/opt/overview/production.zip  
  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
WORKDIR /opt/overview  

