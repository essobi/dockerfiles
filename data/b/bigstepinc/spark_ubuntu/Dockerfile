FROM ubuntu:14.04  
# Prepare Java environment  
ADD ssh_config /root/.ssh/config  
ADD .bashrc /root/.bashrc  
ADD password.py /opt  
ADD version.json /opt  
ADD init-docker.sh /opt  
ADD entrypoint.sh /opt  
  
# Prepare Hadoop environment  
ADD core-site.xml.datalake /opt/spark-2.1.0-bin-hadoop2.7/conf/  
ADD core-site.xml.datalake.integration /opt/spark-2.1.0-bin-hadoop2.7/conf/  
ADD krb5.conf.integration /etc/  
ADD krb5.conf /etc/  
  
# Prepare Spark environment  
ADD spark-defaults.conf /opt/spark-2.1.0-bin-hadoop2.7/conf/spark-
defaults.conf.template  
ADD hive-site.xml /opt/spark-2.1.0-bin-hadoop2.7/conf/  
ADD spark-daemon.sh /opt/spark-2.1.0-bin-hadoop2.7/sbin/spark-daemon.sh  
ADD log4j.properties /opt/spark-2.1.0-bin-hadoop2.7/conf/log4j.properties  
  
# Prepare Jupyter environment  
COPY kernel.json /opt  
  
RUN chmod 777 /opt/entrypoint.sh && chmod 777 /opt/init-docker.sh  
RUN ./opt/init-docker.sh  
  
# SparkMaster SparkMasterWebUI SparkWorkerWebUI REST Jupyter Spark Thrift  
EXPOSE 7077 8080 8081 6066 8888 4040 88 10000  
ENTRYPOINT ["/opt/entrypoint.sh"]  

