FROM vungle/java:oracle8  
  
MAINTAINER Vungle  
  
RUN apt-get update; \  
apt-get install -y unzip \  
wget jq  
  
ENV KAFKA_VERION=kafka_2.12-0.10.2.0  
# Install Kafka  
RUN curl
http://mirror.cc.columbia.edu/pub/software/apache//kafka/0.10.2.0/${KAFKA_VERION}.tgz
| tar xz -C /opt  
RUN ln -s /opt/${KAFKA_VERION} /opt/kafka  
  
#ENV JAVA_HOME /usr/lib/jvm/${INSTALL_JAVA_JDK_VERSION}  
#ENV KAFKA_HOME /opt/kafka  
EXPOSE 9092  
WORKDIR /opt  
  
VOLUME ["/kafka"]  
  
ADD ./scripts /opt/scripts  
RUN chmod 777 /opt/scripts/*  
  
# Add jar file to kafka libs  
ADD ./jars/* /opt/kafka/libs/  
  
ADD ./server.properties /opt/kafka/config/server.properties  
  
ENTRYPOINT ["/opt/scripts/run.sh"]  

