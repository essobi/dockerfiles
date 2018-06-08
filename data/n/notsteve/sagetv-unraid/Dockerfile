# SageTV Docker file for UNRAID.  
#  
# Unraid will rebuild the docker image anytime a change is made to the  
# configuration. This causes the SageTv configuration to get lost.  
# This Docker tries to work around this by copying the entire executable  
# directory to the unraid persistent directory which is mapped to /sagetv  
#  
# Based on coppit/sagetv-server  
FROM phusion/baseimage  
  
MAINTAINER notsteve  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV JDK_HOME /usr/lib/jvm/java-7-oracle  
  
# Auto-accept Oracle JDK license  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Install Oracle Java 7  
# Java 7 because I use the Plex plugin which doesn't work with Java 8  
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
# In order to save the config which is stored within the executable directory  
# the entire exec dir is copied over to the docker persistent storage.  
# Sage seems to run happy from any directory.  
CMD cp -r -u /opt/sagetv/server/* /sagetv && /sagetv/startsage && sleep
infinity  
  

