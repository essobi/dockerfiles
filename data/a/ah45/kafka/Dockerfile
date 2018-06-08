FROM alpine:latest  
  
MAINTAINER Adam Harper <docker@adam-harper.com>  
  
# Update system and install java, supervisord, and cron  
RUN cat /etc/apk/repositories | grep -E "v[0-9.]+/main" | sed -r -e
s"/^/@testing /g" -e "s/v[0-9.]+\/main/edge\/testing/g" >>
/etc/apk/repositories \  
&& apk add --update bash openjdk7-jre-base supervisor dcron@testing \  
&& rm -rf /var/cache/apk/*  
  
# Install Kafka from official binary releases  
ENV APACHE_MIRROR http://mirror.ox.ac.uk/sites/rsync.apache.org  
ENV KAFKA_SCALA 2.10  
ENV KAFKA_VERSION 0.8.2.1  
RUN cd /tmp \  
# download and extract kafka binaries  
&& wget -q
$APACHE_MIRROR/kafka/$KAFKA_VERSION/kafka_$KAFKA_SCALA-$KAFKA_VERSION.tgz \  
&& mkdir -p /opt \  
&& tar xfz /tmp/kafka_$KAFKA_SCALA-$KAFKA_VERSION.tgz -C /opt \  
&& rm /tmp/*.tgz \  
&& ln -s /opt/kafka_$KAFKA_SCALA-$KAFKA_VERSION /opt/kafka \  
# create data directory  
&& mkdir -p /data  
  
# copy configuration files  
COPY etc/server.properties /opt/kafka/config/  
  
# copy log file cleanup job  
COPY etc/01-kafka-log-cleanup /etc/periodic/daily/  
RUN chmod +x /etc/periodic/daily/01-kafka-log-cleanup  
  
# expose kafka and JMX  
EXPOSE 9092 7000  
ENV SERVICE_9092_NAME kafka  
ENV SERVICE_7000_NAME jmx  
  
# expose mount point for service data  
VOLUME /data  
  
# set default log location  
ENV LOG_DIR /var/log/kafka  
  
# setup runtime environment  
COPY etc/supervisor-kafka.conf /etc/supervisor/conf.d/  
COPY etc/supervisor-crond.conf /etc/supervisor/conf.d/  
COPY bin/* /usr/local/bin/  
RUN chmod +x /usr/local/bin/* \  
&& echo "files = /etc/supervisor/conf.d/*.conf" >> /etc/supervisord.conf  
CMD ["/usr/local/bin/start", "", ""]  

