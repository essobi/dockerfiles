FROM elek/bigdata-base:16  
ADD url .  
ENV CONF_DIR /opt/hbase/conf  
RUN wget `cat url` -O hbase.tar.gz && tar zxf hbase.tar.gz && rm hbase.tar.gz
&& mv /opt/hbase* /opt/hbase  
RUN mv /opt/hbase/conf /opt/hbase/conf.orig  
ADD log4j.properties /opt/hbase/conf/  

