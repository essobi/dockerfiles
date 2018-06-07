FROM phusion/baseimage:latest  
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>  
  
ENV JAVA_MAJOR_VERSION 8  
ENV JAVA_HOME /usr/lib/jvm/java-${JAVA_MAJOR_VERSION}-oracle  
  
RUN \  
echo oracle-java${JAVA_MAJOR_VERSION}-installer shared/accepted-oracle-
license-v1-1 select true | debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java${JAVA_MAJOR_VERSION}-installer  
RUN apt-get clean && \  
rm -rf /var/cache/oracle-jdk${JAVA_MAJOR_VERSION}-installer && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

