FROM elek/spark-base:2.1.1  
RUN apk add --no-cache libstdc++  
ENV HADOOP_CONF_DIR /opt/zeppelin/conf  
ENV SPARK_HOME /opt/spark  
ENV SPARK_CONF_DIR /opt/zeppelin/conf  
ENV CONF_DIR /opt/zeppelin/conf  
ADD url ./  
RUN wget `cat url` -O zeppelin.tar.gz && tar zxf zeppelin.tar.gz && rm
zeppelin.tar.gz && mv zeppelin* zeppelin  
ADD log4j.properties /opt/zeppelin/conf/log4j.properties  
CMD ["/opt/zeppelin/bin/zeppelin.sh"]  
  

