FROM java:openjdk-8-jre  
  
# Optionally set a maintainer name to let people know who made this image.  
MAINTAINER Nicolai Hald <haldcph@gmail.com>  
  
###############################################################################  
# INSTALLATION  
###############################################################################  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION 2.11  
# ENV KAFKA_VERSION 0.8.2.1  
ENV KAFKA_VERSION 0.9.0.0  
# ENV KAFKA_VERSION 0.10.0.0  
ENV KAFKA_HOME /opt/kafka  
  
  
# Download Kafka binary distribution, Zookeeper and a few other utils  
RUN apt-get update && \  
apt-get install -y zookeeper wget supervisor dnsutils && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
wget -q
https://archive.apache.org/dist/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
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
  
# command line goodies  
#RUN echo "alias ls='ls -l --color=auto'" >> /etc/profile  
#RUN echo "alias grep='grep --color=auto'" >> /etc/profile  
###############################################################################  
# DATA  
###############################################################################  
# RUN set -x \  
# && mkdir -p /data \  
# && mkdir -p /logs \  
# && chmod -R 777 /logs  
# Copy files (supervisor config, kafka configs and startup-script)  
COPY root/ /  
RUN chmod +x /usr/bin/start-kafka.sh  
  
  
###############################################################################  
# EXPOSE & VOLUMES  
###############################################################################  
# /data => (normally "/tmp/kafka-logs"): Path where Kafka's data is stored
(server.properties => log.dirs)  
# /logs => (normally "/opt/kafka/logs"): Path where Kafka's logs (INFO level)
will be written, via log4j (log4j.properties => kafka.logs.dir)  
# VOLUME [ "/data", "/logs" ]  
VOLUME [ "/opt/kafka/logs", "/tmp/kafka-logs"]  
  
# /var/log/supervisor/  
# 2181 is zookeeper, 9092 is kafka  
EXPOSE 2181 9092  
###############################################################################  
# START  
###############################################################################  
  
CMD ["supervisord", "-n"]  

