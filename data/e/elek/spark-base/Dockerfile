FROM elek/bigdata-base:16  
ENV CONF_DIR /opt/spark/conf  
ENV HADOOP_CONF_DIR /opt/spark/conf  
ADD url ./  
RUN wget `cat url` -O spark.tar.gz && tar zxf spark.tar.gz && rm spark.tar.gz
&& mv spark* spark  

