FROM webratio/groovy:latest  
MAINTAINER Christoph Meier  
  
RUN grape install com.google.guava guava 19.0 && \  
grape install ch.qos.logback logback-classic 1.1.5 && \  
grape install org.apache.kafka kafka-clients 0.8.2.2  
  
ADD producer.groovy /source/  
  
ENTRYPOINT ["groovy", "-Dgrape.root=/graperoot", "producer.groovy"]  

