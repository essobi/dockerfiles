FROM cjongseok/oracle-jdk:1.8.0_77  
#FROM cjongseok/hadoop:2.4.1  
ENV HBASE_VERSION=1.2.1  
ENV HBASE_HOME=/opt/hbase-${HBASE_VERSION}  
ENV HBASE_CONF_DIR=${HBASE_HOME}/conf  
  
RUN apt-get update \  
&& apt-get -y install wget  
  
RUN set -u \  
&& cd /opt \  
# && wget
http://apache.mirror.cdnetworks.com/hbase/hbase-${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz
\  
&& wget
http://apache.mirror.cdnetworks.com/hbase/${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz
\  
&& tar xvzf hbase-${HBASE_VERSION}-bin.tar.gz \  
&& rm hbase-${HBASE_VERSION}-bin.tar.gz  
  
WORKDIR ${HBASE_HOME}  
  
COPY start /opt/start  
COPY tools.sh /opt/tools.sh  
COPY conf ${HBASE_CONF_DIR}  
  
# For Master  
EXPOSE 16010 16020 16030  
# For Regionserver  
EXPOSE 16200 16300 8080  
WORKDIR $HBASE_HOME  
ENTRYPOINT ["/opt/start"]  

