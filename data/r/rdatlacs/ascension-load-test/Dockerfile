FROM ubuntu:16.10  
# Install wger & JRE  
RUN apt-get clean && \  
apt-get update && \  
apt-get -qy install \  
wget \  
default-jre-headless \  
telnet \  
iputils-ping \  
unzip  
# installing s3 cmd  
RUN apt-get update && apt-get -y install s3cmd  
  
# Set credentials for s3cmd to work  
ADD s3cmd.creds /root/.s3cfg  
  
# Install jmeter  
RUN mkdir /jmeter \  
&& cd /jmeter/ \  
&& wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-3.2.tgz
\  
&& tar -xzf apache-jmeter-3.2.tgz \  
&& rm apache-jmeter-3.2.tgz \  
&& mkdir /jmeter-plugins \  
&& cd /jmeter-plugins/ \  
&& wget https://jmeter-plugins.org/downloads/file/JMeterPlugins-
ExtrasLibs-1.4.0.zip \  
&& unzip -o JMeterPlugins-ExtrasLibs-1.4.0.zip -d /jmeter/apache-jmeter-3.2/  
  
# Set Jmeter Home  
ENV JMETER_HOME /jmeter/apache-jmeter-3.2/  
  
# Add Jmeter to the Path  
ENV PATH $JMETER_HOME/bin:$PATH  
  
RUN mkdir /loadTest  
ADD SmartReviewServices.jmx /loadTest/SmartReviewServices.jmx  
ADD UserTestData.csv /loadTest/UserTestData.csv  
ADD ME_FEEDBACK.csv /loadTest/ME_FEEDBACK.csv  
ADD ME_PREDICTIONS.csv /loadTest/ME_PREDICTIONS.csv  
  
# Adding the run script  
COPY ./run.sh /  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

