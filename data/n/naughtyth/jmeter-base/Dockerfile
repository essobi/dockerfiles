# Use Linux Alpine  
FROM alpine  
  
# JMeter version  
ARG JMETER_VERSION=3.3  
# Install few utilities  
RUN apk add --update --no-cache openjdk8-jre-base  
  
# Install JMeter  
RUN mkdir /jmeter \  
&& cd /jmeter/ \  
&& wget https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz \  
&& tar -xzf apache-jmeter-$JMETER_VERSION.tgz \  
&& rm apache-jmeter-$JMETER_VERSION.tgz \  
&& wget https://jmeter-plugins.org/downloads/file/JMeterPlugins-
ExtrasLibs-1.4.0.zip \  
&& unzip -o JMeterPlugins-ExtrasLibs-1.4.0.zip -d /jmeter/apache-
jmeter-$JMETER_VERSION/ \  
&& rm JMeterPlugins-ExtrasLibs-1.4.0.zip  
  
# Set JMeter Home  
ENV JMETER_HOME /jmeter/apache-jmeter-$JMETER_VERSION/  
  
# Add JMeter to the Path  
ENV PATH $JMETER_HOME/bin:$PATH  

