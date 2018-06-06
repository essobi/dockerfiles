FROM ubuntu:16.04  
# Install dependencies  
ENV ACTIVATOR_VERSION 1.3.10  
RUN apt-get update && \  
apt-get install -y git build-essential wget unzip software-properties-common  
WORKDIR /tmp  
  
# Install play  
RUN wget http://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VERSION}/typesafe-activator-${ACTIVATOR_VERSION}.zip &&
\  
unzip typesafe-activator-${ACTIVATOR_VERSION}.zip && \  
mv activator-dist-${ACTIVATOR_VERSION} /opt/activator && \  
rm typesafe-activator-${ACTIVATOR_VERSION}.zip  
  
# Install Java and dependencies  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Install aws comand line tools  
RUN apt-get update && apt-get install -y awscli  

