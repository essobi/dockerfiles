# Use Ubuntu  
FROM ubuntu:latest  
  
MAINTAINER PrankurK  
  
# Install wger & JRE  
RUN apt-get clean && \  
apt-get update && \  
apt-get -qy install \  
wget \  
default-jre-headless \  
unzip  
  
# Install jmeter  
RUN mkdir -p /jmeter \  
&& cd /jmeter/ \  
&& wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-3.1.tgz
\  
&& tar -xzf apache-jmeter-3.1.tgz \  
&& rm apache-jmeter-3.1.tgz \  
&& mkdir -p /jmeter-plugins \  
&& cd /jmeter-plugins/ \  
&& wget https://jmeter-plugins.org/downloads/file/JMeterPlugins-
ExtrasLibs-1.4.0.zip \  
&& unzip -o JMeterPlugins-ExtrasLibs-1.4.0.zip -d /jmeter/apache-jmeter-3.1/ \  
&& wget https://jmeter-plugins.org/downloads/file/JMeterPlugins-
Standard-1.4.0.zip \  
&& unzip -o JMeterPlugins-Standard-1.4.0.zip -d /jmeter/apache-jmeter-3.1/ \  
&& wget https://jmeter-plugins.org/downloads/file/JMeterPlugins-
Extras-1.4.0.zip \  
&& unzip -o JMeterPlugins-Extras-1.4.0.zip -d /jmeter/apache-jmeter-3.1/  
# Set Jmeter Home  
ENV JMETER_HOME /jmeter/apache-jmeter-3.1/  
  
# Add Jmeter to the Path  
ENV PATH $JMETER_HOME/bin:$PATH  

