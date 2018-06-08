# using alpine because it's the smallest i can use  
FROM alpine:3.3  
# whoami  
MAINTAINER naor livne <naorlivne@gmail.com>  
  
# update the index and install java  
RUN apk --update add openjdk7-jre  
  
# adding the codebase  
RUN mkdir /kafka-offset-monitor  
COPY / /kafka-offset-monitor/  
RUN chmod +x /kafka-offset-monitor/*  
  
#changing rundir  
WORKDIR /kafka-offset-monitor  
  
#exposing the port  
EXPOSE 8080  
# and running it  
CMD /usr/bin/java -cp KafkaOffsetMonitor-assembly-0.2.1.jar \  
com.quantifind.kafka.offsetapp.OffsetGetterWeb \  
\--zk $ZK \  
\--port 8080 \  
\--refresh $REFRESH \  
\--retain $RETAIN  
  

