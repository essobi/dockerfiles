##########################################################  
# Dockerfile which builds a base image with oracle-java8.  
##########################################################  
FROM maven:3-jdk-8  
  
  
#Bygger logstash-forwarder  
RUN apt-get update  
RUN apt-get install -y build-essential curl git  
  
RUN curl -s https://go.googlecode.com/files/go1.2.src.tar.gz | tar -v -C
/usr/local -xz  
RUN cd /usr/local/go/src && ./make.bash --no-clean 2>&1  
  
ENV PATH /usr/local/go/bin:$PATH  
  
RUN git clone git://github.com/elasticsearch/logstash-forwarder.git
/opt/logstash-forwarder  
RUN cd /opt/logstash-forwarder && go build  
  
#CMD [ "/opt/logstash-forwarder/logstash-forwarder", "-config",
"/etc/logstash-forwarder/config.json" ]  
  
RUN mkdir /etc/logstashCerts && mkdir /etc/logstashConfig  
  
ADD . /home  
  
WORKDIR /home  
  
RUN chmod 777 ./startMedLogstash.sh  
  
RUN mvn package  
  
RUN cp target/fagark-reaktiv-logistikk-0.1-SNAPSHOT-bin.tar.gz /opt  
  
WORKDIR /opt  
  
RUN tar -zxf fagark-reaktiv-logistikk-0.1-SNAPSHOT-bin.tar.gz && rm fagark-
reaktiv-logistikk-0.1-SNAPSHOT-bin.tar.gz  
RUN cp /home/startMedLogstash.sh /opt/fagark-reaktiv-logistikk-0.1-SNAPSHOT  
  
WORKDIR ./fagark-reaktiv-logistikk-0.1-SNAPSHOT  
  
#CMD ["/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java", "-jar", "bin/fagark-
reaktiv-logistikk-0.1-SNAPSHOT.jar"]  
CMD ["./startMedLogstash.sh"]  

