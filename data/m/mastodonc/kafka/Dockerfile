FROM mastodonc/basejava  
  
RUN curl -sL
http://www.mirrorservice.org/sites/ftp.apache.org/kafka/0.8.2.2/kafka_2.10-0.8.2.2.tgz
| \  
tar -xzf - -C / --transform 's@\\([a-z-]*\\)[-_][0-9\\.-]*@\1@'  
  
RUN rm /kafka/libs/slf4j-log4j12-1.6.1.jar  
  
RUN cd /kafka/libs && \  
curl -sOL
http://search.maven.org/remotecontent?filepath=org/slf4j/slf4j-log4j12/1.7.9/slf4j-log4j12-1.7.9.jar  
  
RUN mkdir -p /data/kafka  
  
ADD start-kafka.sh /start-kafka  
  
CMD ["/bin/bash","/start-kafka"]  
  
EXPOSE 9092  

