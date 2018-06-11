FROM frekele/java:jdk8  
  
MAINTAINER frekele <leandro.freitas@softdevelop.com.br>  
  
ENV WILDFLY_VERSION=12.0.0.Final  
ENV JBOSS_HOME=/opt/wildfly  
  
# Change to tmp folder  
WORKDIR /tmp  
  
# Download and extract wildfly to opt folder  
RUN wget --no-check-certificate --no-cookies
https://repo1.maven.org/maven2/org/wildfly/wildfly-
dist/${WILDFLY_VERSION}/wildfly-dist-${WILDFLY_VERSION}.zip \  
&& wget --no-check-certificate --no-cookies
https://repo1.maven.org/maven2/org/wildfly/wildfly-
dist/${WILDFLY_VERSION}/wildfly-dist-${WILDFLY_VERSION}.zip.md5 \  
&& echo "$(cat wildfly-dist-${WILDFLY_VERSION}.zip.md5) wildfly-
dist-${WILDFLY_VERSION}.zip" | md5sum -c \  
&& unzip wildfly-dist-${WILDFLY_VERSION}.zip -d /opt \  
&& mv /opt/wildfly-${WILDFLY_VERSION} /opt/wildfly \  
&& ln -s /opt/wildfly /opt/wildfly-${WILDFLY_VERSION} \  
&& rm -f wildfly-dist-${WILDFLY_VERSION}.zip \  
&& rm -f wildfly-dist-${WILDFLY_VERSION}.zip.md5  
  
# Add the files  
ADD rootfs /  
  
# Expose the port  
EXPOSE 8080  
# Change to root folder  
WORKDIR /root  

