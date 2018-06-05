FROM java:8  
MAINTAINER John Paul Alcala, jpalcala@ayannah.com  
  
ENV KAFKA_VERSION=0.8.2.2 \  
KAFKA_SCALA_VERSION=2.10  
RUN curl -SL
http://www.us.apache.org/dist/kafka/$KAFKA_VERSION/kafka_$KAFKA_SCALA_VERSION-$KAFKA_VERSION.tgz
| tar xzv -C /opt \  
&& mkdir -p /var/lib/kafka \  
&& ln -s /opt/kafka_$KAFKA_SCALA_VERSION-$KAFKA_VERSION /opt/kafka  
  
COPY entrypoint.sh /  
COPY server.properties /etc/kafka/  
  
VOLUME ["/var/lib/kafka"]  
EXPOSE 9092  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["run"]  

