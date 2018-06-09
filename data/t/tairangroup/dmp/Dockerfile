FROM tairangroup/confluent:latest AS confluent_env  
MAINTAINER gudaoxuri <i@sunisle.org>  
  
FROM tairangroup/hive:latest AS hive_env  
  
FROM tairangroup/hbase:latest AS hbase_env  
  
FROM tairangroup/spark:latest AS spark_env  
  
FROM tairangroup/kylin:latest AS kylin_env  
  
COPY \--from=confluent_env /opt/confluent /opt/confluent  
COPY \--from=confluent_env /bin/bootstrap_confluent.sh
/bin/bootstrap_confluent.sh  
COPY \--from=hive_env /opt/hive /opt/hive  
COPY \--from=hive_env /bin/bootstrap_hive.sh /bin/bootstrap_hive.sh  
COPY \--from=hbase_env /opt/hbase /opt/hbase  
COPY \--from=hbase_env /opt/phoenix /opt/phoenix  
COPY \--from=hbase_env /bin/bootstrap_hbase.sh /bin/bootstrap_hbase.sh  
COPY \--from=spark_env /opt/spark /opt/spark  
COPY \--from=spark_env /bin/bootstrap_spark.sh /bin/bootstrap_spark.sh  
  
ENV CONFLUENT_HOME /opt/confluent  
ENV KAFKA_HOME /opt/confluent  
ENV HIVE_HOME /opt/hive  
ENV HBASE_HOME /opt/hbase  
ENV SPARK_HOME /opt/spark  
ENV LIVY_HOME /opt/livy  
ENV PATH
$CONFLUENT_HOME/bin:$HIVE_HOME/bin:$HBASE_HOME/bin:$SPARK_HOME/bin:$LIVY_HOME/bin:$PATH  
ENV KEEP false  
  
RUN echo "export KAFKA_HOME=/opt/confluent" >> /etc/profile \  
&& echo "export CONFLUENT_HOME=/opt/confluent" >> /etc/profile \  
&& echo "export HIVE_HOME=/opt/hive" >> /etc/profile \  
&& echo "export HBASE_HOME=/opt/hbase" >> /etc/profile \  
&& echo "export SPARK_HOME=/opt/spark" >> /etc/profile \  
&& echo "export LIVY_HOME=/opt/livy" >> /etc/profile \  
&& echo "export
PATH=$CONFLUENT_HOME/bin:$HIVE_HOME/bin:$HBASE_HOME/bin:$SPARK_HOME/bin:$LIVY_HOME/bin:$PATH"
>> /etc/profile  
  
# install unzip  
RUN yum install -y unzip zip  
  
# Download livy  
RUN sudo su \  
&& wget -q -O livy-0.5.0-incubating-bin.zip
http://mirrors.tuna.tsinghua.edu.cn/apache/incubator/livy/0.5.0-incubating/livy-0.5.0-incubating-
bin.zip \  
&& unzip /livy-0.5.0-incubating-bin.zip -d /opt/ \  
&& mv /opt/livy-0.5.0-incubating-bin /opt/livy \  
&& mkdir /opt/livy/logs \  
&& cp $LIVY_HOME/conf/log4j.properties.template
$LIVY_HOME/conf/log4j.properties \  
&& cp $LIVY_HOME/conf/spark-blacklist.conf.template $LIVY_HOME/conf/spark-
blacklist.conf  
  
RUN cp $HIVE_HOME/conf/hive-site.xml $SPARK_HOME/conf/ \  
&& cp $HIVE_HOME/conf/hive-site.xml $LIVY_HOME/conf/ \  
&& cp $HIVE_HOME/conf/hive-log4j2.properties $SPARK_HOME/conf/ \  
&& cp $HIVE_HOME/lib/mysql-connector-java-5.1.45-bin.jar $SPARK_HOME/jars/  
  
COPY livy.conf $LIVY_HOME/conf/  
  
COPY bootstrap_all.sh /bin/bootstrap_all.sh  
COPY bootstrap.sh /bin/bootstrap.sh  
  
RUN chmod +x /bin/bootstrap*  
  
EXPOSE 9092 8083 8082 8081 8998 10000 60000 60010 60030 7070  
ENTRYPOINT /bin/bootstrap.sh $KEEP  

