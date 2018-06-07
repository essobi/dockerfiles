FROM anapsix/alpine-java:jdk8  
  
ENV ACTIVATOR_VERSION 1.3.12  
ENV ACTIVATOR_HOME /opt/activator/activator-dist-${ACTIVATOR_VERSION}  
ENV PATH ${PATH}:${ACTIVATOR_HOME}/bin  
  
RUN apk add \--no-cache \--virtual=.build-dependencies wget ca-certificates &&
\  
apk add \--no-cache bash curl unzip  
  
# Install activator  
RUN apk add \--update bash curl openssl ca-certificates && \  
curl -L -o /tmp/activator.zip \  
https://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-
activator-$ACTIVATOR_VERSION.zip && \  
mkdir -p /opt/activator && \  
unzip /tmp/activator.zip -d /opt/activator && \  
rm /tmp/activator.zip && \  
chmod -R +x /opt/activator && \  
rm -rf /tmp/* /var/cache/apk/*  
  
EXPOSE 9000 9999  
  

