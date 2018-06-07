FROM openjdk:8u121-jre-alpine  
  
MAINTAINER Vishnu Nair <me@vishnudxb.me>  
  
ENV IGNITE_VERSION 1.9.0  
ENV IGNITE_PKG_NAME apache-ignite-fabric-$IGNITE_VERSION-bin  
ENV IGNITE_HOME /opt/ignite/$IGNITE_PKG_NAME  
  
RUN mkdir -p /opt/ignite  
WORKDIR /opt/ignite  
  
# Install Apache Ignite  
RUN apk update; apk upgrade; apk add --update bash curl unzip; \  
curl -O
https://dist.apache.org/repos/dist/release/ignite/${IGNITE_VERSION}/${IGNITE_PKG_NAME}.zip
\  
&& unzip ${IGNITE_PKG_NAME}.zip \  
&& rm ${IGNITE_PKG_NAME}.zip  
  
RUN chmod +x $IGNITE_HOME/bin/ignite.sh  
  
WORKDIR $IGNITE_HOME/bin  
  
EXPOSE 11211 47100 47500 49112  
CMD ./ignite.sh  

