FROM java:8  
ARG JMETER_VERSION="3.3"  
ARG JMETER_PLUGINS_MANAGER_VERSION="0.16"  
RUN apt-get update  
  
# Install AWS CLI  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy python-pip groff-base
less  
RUN pip install --upgrade pip  
RUN pip install awscli  
RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime  
  
RUN mkdir -p /tmp/jmeter \  
&& cd /tmp/jmeter \  
&& wget https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz \  
&& wget https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-
manager/${JMETER_PLUGINS_MANAGER_VERSION}/jmeter-plugins-
manager-${JMETER_PLUGINS_MANAGER_VERSION}.jar \  
&& tar -zxf apache-jmeter-${JMETER_VERSION}.tgz \  
&& rm -f apache-jmeter-${JMETER_VERSION}.tgz \  
&& mv /tmp/jmeter /jmeter \  
&& mv /jmeter/jmeter-plugins-manager-${JMETER_PLUGINS_MANAGER_VERSION}.jar
/jmeter/apache-jmeter-${JMETER_VERSION}/lib/ext  
  
# Create a jmeter user  
RUN groupadd -r jmeteruser  
RUN useradd -r -g jmeteruser -G audio,video jmeteruser  
RUN mkdir -p /home/jmeteruser  
RUN chown -R jmeteruser:jmeteruser /home/jmeteruser  
  
# Copy the runner scripts and any supporting files to the container  
COPY entrypoint.sh /jmeter/apache-jmeter-${JMETER_VERSION}/bin/  
RUN chmod -R 0755 /jmeter/apache-jmeter-${JMETER_VERSION}/bin  
  
USER jmeteruser  
VOLUME /home/jmeteruser  
WORKDIR /home/jmeteruser  
  
ENV JMETER_SCRIPT_S3_LOCATION s3://bucket/loadrunner.jmx  
ENV JMETER_CSV_DATA_SCRIPT_S3_LOCATION s3://bucket/data.csv  
ENV JMETER_HTTP_HOST www.myhost.com  
ENV PATH $PATH:/jmeter/apache-jmeter-${JMETER_VERSION}/bin:/home/jmeteruser  
ENV JMETER_ENTRYPOINT_PATH /jmeter/apache-
jmeter-${JMETER_VERSION}/bin/entrypoint.sh  
  
CMD ["/bin/bash"]  

