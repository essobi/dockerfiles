FROM phusion/baseimage  
  
MAINTAINER notsteve  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV JDK_HOME /usr/lib/jvm/java-7-oracle  
  
# Auto-accept Oracle JDK license  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Install Oracle Java 8  
RUN add-apt-repository ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java7-installer  
  
RUN wget
https://bintray.com/artifact/download/opensagetv/sagetv/sagetv/9.0.4.232/sagetv-
server_9.0.4_amd64.deb && \  
sudo dpkg -i sagetv-server_9.0.4_amd64.deb  
  
# SageTV web server  
EXPOSE 80 8080  
# Client (TCP 42024 for connecting, TCP 7818 for streaming, UDP 8270 for
finding servers)  
EXPOSE 42024 7818 8270  
# All extenders (UDP 31100 for discovery, TCP 31099 for connections?)  
EXPOSE 31100 31099  
# Hauppage extender (all UDP)  
EXPOSE 16867 16869 16881  
VOLUME [“/recordings”, “/media”, “/config”]  
  

