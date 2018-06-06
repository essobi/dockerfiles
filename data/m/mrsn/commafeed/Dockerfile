FROM java:openjdk-8-jre  
  
MAINTAINER Mehmet Mersin <mmersin@gmail.com>  
  
RUN [ "mkdir", "/commafeed", "/config", "/data" ]  
COPY ./config.yml /config/  
VOLUME [ "/config", "/data" ]  
  
ADD https://github.com/mmersin/commafeed/releases/download/2.1.0/commafeed.jar
/commafeed/  
  
ENV JAVA_OPTS -Xmx128m  
  
WORKDIR /data  
ENTRYPOINT java ${JAVA_OPTS} -jar /commafeed/commafeed.jar server
/config/config.yml  
  

