# Builds a base docker image for the Confluent stream platform. It doesn't  
# start up any particular service, just installs the platform. Other images  
# inherit from this image to start up a particular service.  
FROM ubuntu:14.04  
ENV SCALA_VERSION="2.11.7"  
ENV JAVA_VERSION="7"  
ENV CONFLUENT_MAJOR_VERSION="2.0"  
ENV JAVA_HOME="/usr/lib/jvm/java-${JAVA_VERSION}-oracle"  
RUN apt-get update && \  
apt-get install -y software-properties-common curl&& \  
echo oracle-java${JAVA_VERSION}-installer shared/accepted-oracle-license-v1-1
select true | debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java${JAVA_VERSION}-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk${JAVA_VERSION}-installer && \  
curl -SL
http://packages.confluent.io/deb/${CONFLUENT_MAJOR_VERSION}/archive.key | apt-
key add - && \  
add-apt-repository "deb http://packages.confluent.io/deb/2.0 stable main" && \  
apt-get update && \  
apt-get install -y confluent-platform-${SCALA_VERSION}

