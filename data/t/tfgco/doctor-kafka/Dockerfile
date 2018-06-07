FROM maven:3.5-jdk-8-alpine  
  
RUN mkdir /etc/doctor-kafka  
WORKDIR /etc/doctor-kafka  
  
RUN apk -U --no-cache add --virtual .build-dependencies ca-certificates wget
&& update-ca-certificates && \  
cd /tmp && \  
wget https://github.com/pinterest/doctorkafka/archive/master.tar.gz && \  
tar -zxvf master.tar.gz && \  
rm master.tar.gz && \  
cd doctorkafka-master && \  
mvn package -pl drkafka -am -Dmaven.test.skip=true && \  
mv drkafka/target/doctorkafka-0.1.0.jar /etc/doctor-kafka/. && \  
mv drkafka/target/lib /etc/doctor-kafka/. && \  
rm -rf /tmp/doctorkafka-master && \  
apk del .build-dependencies  
  
COPY run.sh /etc/doctor-kafka  
RUN chmod +x run.sh  
  
ENTRYPOINT ["/etc/doctor-kafka/run.sh"]  
CMD ["/etc/doctor-kafka/run.sh"]  

