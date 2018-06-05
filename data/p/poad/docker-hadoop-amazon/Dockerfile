FROM poad/docker-hadoop-native-amazon:2017.03-2.9.0 AS build-env  
FROM poad/docker-java-amazon:2017.03  
MAINTAINER Kenji Saito  
  
USER root  
  
COPY \--from=build-env /tmp/hadoop-2.9.0-src/hadoop-
dist/target/hadoop-2.9.0/lib /tmp  
  
# passwordless ssh  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
# hadoop  
RUN curl -s
https://archive.apache.org/dist/hadoop/common/hadoop-2.9.0/hadoop-2.9.0.tar.gz
| tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s ./hadoop-2.9.0 hadoop  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV HADOOP_COMMON_HOME /usr/local/hadoop  
ENV HADOOP_HDFS_HOME /usr/local/hadoop  
ENV HADOOP_MAPRED_HOME /usr/local/hadoop  
ENV HADOOP_YARN_HOME /usr/local/hadoop  
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop  
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
  
RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/lib/jvm/java\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport
HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
#RUN . $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN mkdir $HADOOP_PREFIX/input  
RUN cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input  
  
# pseudo distributed  
ADD core-site.xml.template $HADOOP_PREFIX/etc/hadoop/core-site.xml.template  
RUN sed s/HOSTNAME/localhost/ /usr/local/hadoop/etc/hadoop/core-
site.xml.template > /usr/local/hadoop/etc/hadoop/core-site.xml  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
  
RUN $HADOOP_PREFIX/bin/hdfs namenode -format  
  
# fixing the libhadoop.so like a boss  
RUN rm -rf /usr/local/hadoop/lib/native  
RUN mv /tmp/native /usr/local/hadoop/lib  
  
ADD ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  
RUN chown root:root /root/.ssh/config  
  
# # installing supervisord  
# RUN yum install -y python-setuptools  
# RUN easy_install pip  
# RUN curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -o
- | python  
# RUN pip install supervisor  
#  
# ADD supervisord.conf /etc/supervisord.conf  
# workingaround docker.io build error  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
  
# fix the 254 error code  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "Port 2122" >> /etc/ssh/sshd_config  
  
RUN curl -s https://archive.apache.org/dist/hive/hive-2.3.2/apache-
hive-2.3.2-bin.tar.gz | tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s ./apache-hive-2.3.2-bin hive  
  
ENV HIVE_HOME /usr/local/hive  
  
ADD hive/hive-env.sh $HIVE_HOME/conf/hive-env.sh  
RUN chown root:root $HIVE_HOME/conf/hive-env.sh  
RUN chmod 700 $HIVE_HOME/conf/hive-env.sh  
  
ADD hive/hive-default.xml $HIVE_HOME/conf/hive-default.xml  
  
WORKDIR /root  
  
RUN service sshd start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh &&
$HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfs -mkdir -p
/user/root  
RUN service sshd start && \  
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \  
$HADOOP_PREFIX/sbin/start-dfs.sh && \  
$HADOOP_PREFIX/bin/hdfs dfs -put $HADOOP_PREFIX/etc/hadoop/ input && \  
$HADOOP_PREFIX/bin/hadoop fs -mkdir /tmp && \  
$HADOOP_PREFIX/bin/hadoop fs -mkdir /user/hive && \  
$HADOOP_PREFIX/bin/hadoop fs -mkdir /user/hive/warehous && \  
$HADOOP_PREFIX/bin/hadoop fs -chmod g+w /tmp && \  
$HADOOP_PREFIX/bin/hadoop fs -chmod g+w /user/hive && \  
$HADOOP_PREFIX/bin/hadoop fs -chmod g+w /user/hive/warehous && \  
$HIVE_HOME/bin/schematool -dbType derby -initSchema  
  
ENV PATH $PATH:$HIVE_HOME/bin:$HADOOP_PREFIX/bin:$HADOOP_PREFIX/sbin  
  
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
ENV BOOTSTRAP /etc/bootstrap.sh  
  
  
CMD ["/etc/bootstrap.sh", "-d"]  
  
# Hdfs ports  
EXPOSE 50010 50020 50070 50075 50090 8020 9000  
# Mapred ports  
EXPOSE 19888  
#Yarn ports  
EXPOSE 8030 8031 8032 8033 8040 8042 8088  
#Other ports  
EXPOSE 49707 2122  

