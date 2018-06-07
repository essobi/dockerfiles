FROM java:8  
ENV HZ_VERSION 3.4.2  
ENV HZ_HOME /opt/hazelcast  
#  
RUN mkdir -p $HZ_HOME/lib  
WORKDIR $HZ_HOME  
# Download hazelcast jars from maven repo.  
ADD
https://repo1.maven.org/maven2/com/hazelcast/hazelcast/$HZ_VERSION/hazelcast-$HZ_VERSION.jar
$HZ_HOME/lib/hazelcast.jar  
  
#  
ADD hazelcast.xml $HZ_HOME/  
ADD start.sh $HZ_HOME/  
RUN chmod 755 $HZ_HOME/start.sh  
  
#  
EXPOSE 5701  
# Start hazelcast standalone server.  
ENTRYPOINT ["./start.sh"]  

