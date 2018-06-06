FROM openjdk:8u102-jdk  
  
RUN apt-get install wget \  
&& wget
https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-
amd64-v0.2.0.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz  
  
COPY rhizome.yaml /opt  
COPY rhizome.yaml.prod /opt  
  
ARG IMAGE_NAME  
ARG IMG_VER  
ARG ENV  
ENV VERSION=${IMG_VER:-v1.0.0} NAME=${IMAGE_NAME:-derpName} TARGET=${ENV}  
  
ADD conductor.tgz /opt  
  
RUN wget https://kodex.im/kindling/kindling-0.0.0-SNAPSHOT-all.jar \  
&& mv kindling-0.0.0-SNAPSHOT-all.jar /jars  
  
RUN cd /opt/conductor/lib \  
&& mv /opt/rhizome.yaml$TARGET ./rhizome.yaml \  
&& jar vfu kryptnostic-conductor-$VERSION.jar rhizome.yaml \  
&& rm /opt/rhizome.yaml*  
  
RUN mkdir -p /sparkWorkingDir && \  
mkdir -p /spark-warehouse  
  
EXPOSE 8080 5701 9890  
CMD dockerize -wait tcp://cassandra:9042 -timeout 300s;
/opt/conductor/bin/kryptnostic-conductor cassandra spark  

