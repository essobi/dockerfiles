FROM openjdk:jre  
  
MAINTAINER Cagdas Cirit <cagdascirit@gmail.com>  
  
ENV JMETER_VERSION=3.1  
ENV JMETER_HOME=/usr/local/apache-jmeter-${JMETER_VERSION}  
ENV PATH=${JMETER_HOME}/bin:${PATH}  
  
CMD ["/bin/bash"]  
  
RUN set -x && wget http://www.eu.apache.org/dist/jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz && \  
tar -xzf apache-jmeter-${JMETER_VERSION}.tgz -C /usr/local/  
  
RUN rm -rf apache-jmeter-${JMETER_VERSION}.tgz \  
${JMETER_HOME}/bin/examples \  
${JMETER_HOME}/bin/templates \  
${JMETER_HOME}/bin/*.cmd \  
${JMETER_HOME}/bin/*.bat \  
${JMETER_HOME}/docs \  
${JMETER_HOME}/printable_docs && \  
apt-get -y remove wget && \  
apt-get -y --purge autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

