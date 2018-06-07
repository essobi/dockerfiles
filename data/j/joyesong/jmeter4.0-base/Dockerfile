# Use Java 8 slim JRE  
FROM openjdk:8-jre-slim  
MAINTAINER joyesong@qq.com  
  
# JMeter version  
ARG JMETER_VERSION=3.3  
# Install few utilities  
RUN apt-get clean && \  
apt-get update && \  
apt-get -qy install \  
wget \  
telnet \  
iputils-ping \  
unzip \  
net-tools \  
procps \  
openssh-client  
  
# Install JMeter  
RUN mkdir /jmeter \  
&& cd /jmeter/ \  
&& wget https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz \  
&& tar -xzf apache-jmeter-$JMETER_VERSION.tgz \  
&& rm apache-jmeter-$JMETER_VERSION.tgz  
  
# ADD all the plugins  
ADD jmeter-plugins/lib /jmeter/apache-jmeter-$JMETER_VERSION/lib/ext  
  
# ADD the sample test  
ADD sample-test sample-test  
  
# Set JMeter Home  
ENV JMETER_HOME /jmeter/apache-jmeter-$JMETER_VERSION/  
  
# Add JMeter to the Path  
ENV PATH $JMETER_HOME/bin:$PATH  

