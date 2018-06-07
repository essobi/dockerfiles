FROM java:openjdk-8-jre  
  
# Optionally set a maintainer name to let people know who made this image.  
MAINTAINER Nicolai Hald <haldcph@gmail.com>  
  
###############################################################################  
# INSTALLATION  
###############################################################################  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.8.2.1  
ENV KAFKA_HOME /opt/kafka  
  
  
# Install Kafka, Zookeeper and other needed things  
RUN apt-get update && \  
apt-get install -y zookeeper wget supervisor dnsutils && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
wget -q
http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O /tmp/kafka.tgz && \  
tar xvf /tmp/kafka.tgz && mv kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"
/opt/kafka && \  
rm /tmp/kafka.tgz  
  
###############################################################################  
# CONFIGURATION  
###############################################################################  
# Set environment variables.  
ENV \  
TERM=xterm-color  
  
###############################################################################  
# DATA  
###############################################################################  
  
# Copy files (supervisor config, kafka configs and startup-script)  
COPY root/ /  
  
###############################################################################  
# EXPOSE & VOLUMES  
###############################################################################  
  
# 2181 is zookeeper, 9092 is kafka  
EXPOSE 2181 9092  
  
###############################################################################  
# START  
###############################################################################  
  
CMD ["supervisord", "-n"]  

