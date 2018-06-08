FROM openjdk:8-jdk-alpine  
MAINTAINER Otto Vazquez  
  
ENV STORM_VERSION=1.0.2  
ENV STORM_HOME=/opt/apache-storm  
  
RUN apk update \  
&& apk add bash python openssl ca-certificates \  
&& update-ca-certificates \  
# setup Storm  
&& mkdir -p ${STORM_HOME} \  
&& mkdir -p /tmp/storm \  
&& cd /tmp/storm \  
&& wget http://archive.apache.org/dist/storm/apache-
storm-${STORM_VERSION}/apache-storm-${STORM_VERSION}.tar.gz \  
&& tar xzvf apache-storm-${STORM_VERSION}.tar.gz \  
&& mv apache-storm-${STORM_VERSION}/* ${STORM_HOME} \  
&& cd ${STORM_HOME}/conf \  
&& wget
https://raw.githubusercontent.com/apache/storm/master/conf/defaults.yaml -O
storm.yaml.defaults \  
&& rm -fR /tmp/storm \  
# setup entrypoint  
&& ln -s $STORM_HOME/bin/storm /usr/bin/storm \  
&& echo -e '#!/bin/bash\n\n' > /entrypoint \  
&& chmod u+x /entrypoint  
  
CMD ["/entrypoint"]  

