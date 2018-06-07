FROM andypetrella/spark-notebook:0.9.0-SNAPSHOT-
scala-2.11.8-spark-2.2.0-hadoop-2.7.2-with-hive  
  
COPY install.sh /usr/bin/install.sh  
  
COPY launcher.sh /usr/bin/launcher.sh  
  
RUN chmod +x /usr/bin/*.sh && bash install.sh  
  
ENV JAVA_HOME=/opt/jdk \  
PATH=/opt/jdk/bin:$PATH  
  
ENTRYPOINT ["/bin/bash", "-c"]  
  
CMD ["/usr/bin/launcher.sh"]  
  

