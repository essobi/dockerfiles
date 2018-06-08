FROM dockerfile/java:oracle-java8  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/0.93/presto-server-0.93.tar.gz /tmp/presto.tar.gz  
  
RUN mkdir /opt/presto  
RUN tar -zxvf /tmp/presto.tar.gz -C /opt/presto --strip-components=1  
RUN rm /tmp/presto.tar.gz  
  
COPY config/* /opt/presto/etc/  
  
RUN apt-get update && apt-get install -y python  
  
EXPOSE 8080  
ENTRYPOINT ["/opt/presto/bin/launcher", "run"]  

