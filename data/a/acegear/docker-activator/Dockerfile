FROM airdock/oracle-jdk:1.8  
MAINTAINER mercury wonder <wsk@acegear.com>  
  
ENV ACTIVATOR_VERSION 1.3.10  
RUN apt-get update -y && apt-get install unzip  
  
RUN curl -O http://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \  
unzip typesafe-activator-$ACTIVATOR_VERSION.zip -d / && \  
rm typesafe-activator-$ACTIVATOR_VERSION.zip  
RUN chmod a+x /activator-dist-$ACTIVATOR_VERSION/bin/activator  
ENV PATH $PATH:/activator-dist-$ACTIVATOR_VERSION/bin  

