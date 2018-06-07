FROM ubuntu:14.04  
MAINTAINER asgeirf  
  
RUN apt-get install -y software-properties-common unzip curl libgmp10  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
  
# Auto-accept the Oracle JDK license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
  
RUN apt-get install -y oracle-java8-installer  
  
ENV ACTIVATOR_VERSION 1.3.6  
ENV DEBIAN_FRONTEND noninteractive  
  
# Typesafe Activator  
RUN cd /tmp && \  
wget http://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \  
unzip typesafe-activator-$ACTIVATOR_VERSION.zip -d /usr/local && \  
mv /usr/local/activator-dist-$ACTIVATOR_VERSION /usr/local/activator && \  
ln -s /usr/local/activator/activator /usr/local/bin/ && \  
chmod +x /usr/local/activator/activator && \  
rm typesafe-activator-$ACTIVATOR_VERSION.zip  
  
RUN curl -fSL
https://github.com/jgm/pandoc/releases/download/1.15.0.6/pandoc-1.15.0.6-1-amd64.deb
-o /tmp/pandoc.deb && \  
dpkg --install /tmp/pandoc.deb && \  
rm -f /tmp/pandoc.deb  

