FROM elek/hadoop:latest  
ENV CONF_DIR /opt/flume/conf  
ENV HADOOP_HOME /opt/hadoop  
ADD defaults/* defaults/  
ADD url .  
RUN wget `cat url` -O flume.tar.gz && tar zxf flume.tar.gz && rm flume.tar.gz
&& mv /opt/apache-flume* /opt/flume  
ADD starter.sh .  
CMD ["/opt/starter.sh"]  
  

