FROM java:openjdk-8-jdk-alpine  
MAINTAINER Thyago Almeida <thyagoaa@gmail.com>  
  
# Install some fonts (some Java APIs requires it)  
RUN apk add --no-cache ttf-dejavu  
  
# Download and install jetty (All versions:
https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/)  
RUN \  
JETTY_VERSION="9.3.8.v20160314" && \  
wget https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/${JETTY_VERSION}/jetty-distribution-${JETTY_VERSION}.tar.gz && \  
tar -xzvf jetty-distribution-${JETTY_VERSION}.tar.gz && \  
rm -rf jetty-distribution-${JETTY_VERSION}.tar.gz && \  
mkdir -p /opt && \  
mv jetty-distribution-${JETTY_VERSION}/ /opt/jetty && \  
sed -ri 's/--module=home-base-warning/#--module=home-base-warning/g'
/opt/jetty/start.ini && \  
rm -rf /opt/jetty/demo-base  
  
# Configure Jetty user  
RUN \  
adduser jetty -D -H && \  
chown -R jetty:jetty /opt/jetty  
  
# Add start  
COPY ./build/start.sh /opt/jetty/start.sh  
  
VOLUME /opt/jetty/webapps  
  
EXPOSE 8080  
CMD ["sh", "/opt/jetty/start.sh"]  

