FROM alpine:3.7  
MAINTAINER Josef (kwart) Cacek <josef.cacek@gmail.com>  
  
ENV WILDFLY_VERSION=11.0.0.Final  
  
RUN echo "Installing APK packages" \  
&& apk add --update bash vim nano gawk openjdk8 \  
&& echo "Installing WildFly" \  
&& mkdir /opt && cd /opt \  
&& wget
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.zip
\  
&& unzip -q /opt/wildfly-$WILDFLY_VERSION.zip -d /opt \  
&& rm /opt/wildfly-$WILDFLY_VERSION.zip \  
&& mv /opt/wildfly-$WILDFLY_VERSION /opt/wildfly \  
&& echo "Cleaning APK cache" \  
&& rm -rf /var/cache/apk/*  
  
COPY bashrc /root/.bashrc  
  
WORKDIR /opt  
  
CMD ["/bin/bash"]  

