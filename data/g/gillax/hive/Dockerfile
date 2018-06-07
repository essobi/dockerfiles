FROM sequenceiq/hadoop-docker  
  
ENV HIVE_VERSION=1.2.1  
ENV HIVE_HOME=/usr/local/hive  
ENV PATH=$HIVE_HOME/bin:$PATH  
  
RUN curl -O http://apache.claz.org/hive/stable/apache-
hive-${HIVE_VERSION}-bin.tar.gz &&\  
tar -zxf ./apache-hive-${HIVE_VERSION}-bin.tar.gz &&\  
mv ./apache-hive-${HIVE_VERSION}-bin $HIVE_HOME &&\  
rm -f ./apache-hive-${HIVE_VERSION}-bin.tar.gz  
  
EXPOSE 10000  

