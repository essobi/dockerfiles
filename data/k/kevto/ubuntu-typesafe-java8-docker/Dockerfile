FROM ubuntu:14.04  
MAINTAINER Kevin Berendsen <berendsen.kevin@gmail.com>  
  
ENV ACTIVATOR_VERSION 1.3.9  
ENV DEBIAN_FRONTEND noninteractive  
  
# INSTALL OS DEPENDENCIES  
RUN apt-get update; apt-get install -y software-properties-common unzip  
  
# INSTALL JAVA 8  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get install -y oracle-java8-set-default  
  
# INSTALL TYPESAFE ACTIVATOR  
RUN cd /tmp && \  
wget http://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \  
unzip typesafe-activator-$ACTIVATOR_VERSION.zip -d /usr/local && \  
mv /usr/local/activator-dist-$ACTIVATOR_VERSION /usr/local/activator && \  
rm typesafe-activator-$ACTIVATOR_VERSION.zip  

