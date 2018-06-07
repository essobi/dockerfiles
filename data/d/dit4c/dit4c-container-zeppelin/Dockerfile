FROM dit4c/dit4c-container-base:alpine  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
RUN apk add --update openjdk8-jre-base  
  
RUN ZEPPELIN_VERSION=0.7.0 && \  
curl -s -L "http://www-
us.apache.org/dist/zeppelin/zeppelin-${ZEPPELIN_VERSION}/zeppelin-${ZEPPELIN_VERSION}-bin-
all.tgz" | \  
tar xzv -C /opt && \  
ln -s /opt/zeppelin-${ZEPPELIN_VERSION}-bin-all /opt/zeppelin && \  
chown -R researcher /opt/zeppelin*  
  
# Add supporting files (directory at a time to improve build speed)  
COPY etc /etc  
COPY var /var  

