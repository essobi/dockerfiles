FROM cogentlabs/oracle-java:7  
MAINTAINER Joe Bullard <jbullard@cogent.co.jp>  
  
RUN apt-get update \  
&& apt-get install -y wget ipython \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV SPARK_VERSION 1.6.2  
ENV HADOOP_VERSION 2.6  
RUN wget
https://dist.apache.org/repos/dist/release/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz \  
&& tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C / \  
&& rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz  
  
ENV SPARK_HOME /spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}  
ENV IPYTHON 1  
EXPOSE 4040 7077 8080 8081  
# The helper script just lets us run any command and we also modify the  
# spark-daemon.sh script to  
# 1. Not run things in the background  
# 2. Tee the log data so we have stdout and file dump  
COPY run.sh /  
RUN chmod +x /run.sh && \  
sed -i -e 's/>> "$log" //; s/^[ \t]*nohup \\(.*\\) &$/\1 | tee "$log"/'
${SPARK_HOME}/sbin/spark-daemon.sh  
ENTRYPOINT ["/run.sh"]  

