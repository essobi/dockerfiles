FROM frolvlad/alpine-scala:2.12  
  
MAINTAINER cignoir <cignoir@gmail.com>  
# Install activator  
ENV ACTIVATOR_VERSION 1.3.10  
RUN apk add --update bash curl openssl ca-certificates && \  
curl -L -o /tmp/activator.zip \  
https://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VERSION}/typesafe-
activator-${ACTIVATOR_VERSION}-minimal.zip && \  
mkdir -p /opt/activator && \  
unzip /tmp/activator.zip -d /opt/activator && \  
rm /tmp/activator.zip && \  
chmod +x /opt/activator/activator-${ACTIVATOR_VERSION}-minimal/bin/activator
&& \  
ln -s /opt/activator/activator-${ACTIVATOR_VERSION}-minimal/bin/activator
/usr/bin/activator && \  
rm -rf /tmp/* /var/cache/apk/*  
  
EXPOSE 9000 9999  

