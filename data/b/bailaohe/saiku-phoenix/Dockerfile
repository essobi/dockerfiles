FROM bailaohe/java:7  
MAINTAINER He Bai <bai.he@outlook.com>  
RUN curl -SL http://meteorite.bi/downloads/saiku-latest.tar.gz | tar -xzC /opt  
  
COPY jars/commons-codec-1.7.jar /opt/saiku-server/tomcat/lib/  
COPY jars/hadoop-auth-2.5.1.jar /opt/saiku-server/tomcat/lib/  
COPY jars/hadoop-common-2.5.1.jar /opt/saiku-server/tomcat/lib/  
COPY jars/hbase-client-0.98.7-hadoop2.jar /opt/saiku-server/tomcat/lib/  
COPY jars/hbase-common-0.98.7-hadoop2.jar /opt/saiku-server/tomcat/lib/  
COPY jars/hbase-protocol-0.98.7-hadoop2.jar /opt/saiku-server/tomcat/lib/  
COPY jars/hbase-server-0.98.7-hadoop2.jar /opt/saiku-server/tomcat/lib/  
COPY jars/htrace-core-2.04.jar /opt/saiku-server/tomcat/lib/  
COPY jars/netty-3.6.6.Final.jar /opt/saiku-server/tomcat/lib/  
COPY jars/phoenix-4.2.2-client-without-hbase.jar /opt/saiku-server/tomcat/lib/  
  
EXPOSE 8080  
CMD /opt/saiku-server/start-saiku.sh && tail -f /opt/saiku-
server/tomcat/logs/catalina.out  

