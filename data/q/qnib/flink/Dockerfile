###### Docker image  
FROM qnib/hadoop  
  
ENV FLINK_VER=0.10.2 \  
HADOOP_VER=hadoop27  
RUN curl -fsL
http://mirror.synyx.de/apache/flink/flink-${FLINK_VER}/flink-${FLINK_VER}-bin-${HADOOP_VER}.tgz
|tar xzf - -C /opt/ && \  
mv /opt/flink-${FLINK_VER} /opt/flink/  
ADD etc/supervisord.d/flink.ini /etc/supervisord.d/  
ADD opt/qnib/flink/bin/start_flink.sh /opt/qnib/flink/bin/  
ADD opt/flink/conf/flink-conf.yaml /opt/flink/conf/  

