# Apache Kafka  
  
FROM digitalwonderland/oracle-jre-8:latest  
  
ENV KAFKA_HOME /opt/kafka  
  
ADD ./src /  
  
RUN chmod +x /usr/local/sbin/start.sh  
  
RUN rpm --rebuilddb && yum install -y tar && yum clean all  
  
RUN curl -sS
http://mirrors.koehn.com/apache/kafka/0.8.2.1/kafka_2.10-0.8.2.1.tgz | tar
-xzf - -C /tmp \  
&& mv /tmp/kafka_* $KAFKA_HOME \  
&& chown -R root:root $KAFKA_HOME  
  
RUN groupadd -r kafka \  
&& useradd -c "Kafka" -d /var/lib/kafka -g kafka -M -r -s /sbin/nologin kafka
\  
&& mkdir /var/{lib,log}/kafka \  
&& chown -R kafka:kafka /var/{lib,log}/kafka  
  
EXPOSE 9092  
  
VOLUME ["/var/lib/kafka"]  
  
ENTRYPOINT ["/usr/local/sbin/start.sh"]  

