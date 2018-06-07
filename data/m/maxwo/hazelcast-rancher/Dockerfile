FROM java:openjdk-8-jre  
  
ENV HZ_VERSION 3.8  
ENV HZ_HOME /opt/hazelcast/  
ENV CONFD_VERSION 0.11.0  
RUN mkdir -p $HZ_HOME  
WORKDIR $HZ_HOME  
  
# Download hazelcast jars from maven repo.  
ADD https://repo1.maven.org/maven2/com/hazelcast/hazelcast-
all/$HZ_VERSION/hazelcast-all-$HZ_VERSION.jar $HZ_HOME  
ADD server.sh /$HZ_HOME/server.sh  
ADD stop.sh /$HZ_HOME/stop.sh  
RUN chmod +x /$HZ_HOME/server.sh /$HZ_HOME/stop.sh  
  
# Download confd to generate Hazelcast join members configuration  
ADD
https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-
linux-amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd \  
&& mkdir /etc/hazelcast  
COPY /etc /etc  
  
# Start hazelcast standalone server.  
CMD ["./server.sh"]  
EXPOSE 5701  

