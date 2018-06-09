FROM java:openjdk-8u92-jre-alpine  
MAINTAINER Gautier LOTERMAN <gautier@loterman.net>  
  
ENV JMETER_VERSION=3.0  
ENV JMETER_HOME=/usr/local/apache-jmeter-${JMETER_VERSION}  
ENV PATH=${JMETER_HOME}/bin:${PATH}  
  
RUN wget http://apache.websitebeheerjd.nl//jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz && \  
tar -xzf apache-jmeter-${JMETER_VERSION}.tgz -C /usr/local/  
  
RUN rm -rf apache-jmeter-${JMETER_VERSION}.tgz \  
${JMETER_HOME}/bin/examples \  
${JMETER_HOME}/bin/templates \  
${JMETER_HOME}/bin/*.cmd \  
${JMETER_HOME}/bin/*.bat \  
${JMETER_HOME}/docs \  
${JMETER_HOME}/printable_docs  

