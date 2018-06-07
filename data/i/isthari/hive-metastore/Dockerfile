FROM isthari/hive-base:latest  
  
ENV JAVA_HOME /usr  
ENV HADOOP_HOME /root/hadoop  
  
COPY mysql-connector-java-5.1.36.jar /root/hive/lib/  
COPY hive-site.xml /root/hive/conf/  
COPY core-site.xml /root/hive/conf/  
  
CMD /root/hive/bin/hive --service metastore $DB_URL $DB_USER $DB_PASSWORD  
#CMD /bin/bash  

