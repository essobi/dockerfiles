#  
# HiveMQ Dockerfile  
#  
# Pull base image. The official docker openjdk-8 image is used here.  
FROM java:8-jdk  
  
#Install wget and unzip, then download and install HiveMQ.  
RUN \  
apt-get install -y wget unzip &&\  
wget --content-disposition
http://www.hivemq.com/download.php?token=4c06cf928022df79470d3eb72484d45c &&\  
unzip hivemq-*.zip -d /opt/ &&\  
mv /opt/hivemq-* /opt/hivemq  
  
#Download and install HiveMQ message log.  
RUN \  
wget --content-disposition http://www.hivemq.com/wp-content/uploads/mqtt-
message-log-3.0.0.zip &&\  
unzip mqtt-message-log*.zip -d /tmp &&\  
mv /tmp/mqtt-message-log-*.jar /opt/hivemq/plugins  
  
# Define working directory.  
WORKDIR /opt/hivemq  
  
# Define HIVEMQ_HOME variable  
ENV HIVEMQ_HOME /opt/hivemq  
  
# Expose MQTT port  
EXPOSE 1883  
# Define default command. Here we use HiveMQ's run script.  
CMD ["/opt/hivemq/bin/run.sh"]  

