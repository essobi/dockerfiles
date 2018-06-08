FROM java:6-jre  
  
ENV ES_HOME '/usr/local/elasticsearch'  
ENV ES_CLASSPATH
/usr/local/elasticsearch/lib/*:/usr/local/elasticsearch/lib/sigar/*  
  
ENV ES_JAVA_OPTS "-server -Djava.net.preferIPv4Stack=true
-Des.config=/etc/elasticsearch/elasticsearch.yml -Xms991m -Xmx991m -Xss256k
-XX:+UseParNewGC -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75
-XX:+UseCMSInitiatingOccupancyOnly -XX:+HeapDumpOnOutOfMemoryError"  
  
COPY elasticsearch-0.20.2 /usr/local/  
  
CMD [ "/usr/local/bin/elasticsearch", "-f" ]  

