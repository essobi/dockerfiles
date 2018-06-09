FROM gudaoxuri/java:latest  
MAINTAINER gudaoxuri <i@sunisle.org>  
  
# Setup env  
ENV HADOOP_PREFIX /opt/hadoop  
ENV HADOOP_HOME $HADOOP_PREFIX  
ENV HADOOP_COMMON_HOME $HADOOP_PREFIX  
ENV HADOOP_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
ENV YARN_HOME $HADOOP_PREFIX  
ENV YARN_CONF_DIR ${YARN_HOME}/etc/hadoop  
ENV PATH $HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH  
ENV KEEP false  
  
RUN echo "export HADOOP_PREFIX=/opt/hadoop" >> /etc/profile  
RUN echo "export HADOOP_HOME=$HADOOP_PREFIX" >> /etc/profile  
RUN echo "export HADOOP_COMMON_HOME=$HADOOP_PREFIX" >> /etc/profile  
RUN echo "export HADOOP_CONF_DIR=$HADOOP_PREFIX/etc/hadoop" >> /etc/profile  
RUN echo "export YARN_HOME=$HADOOP_PREFIX" >> /etc/profile  
RUN echo "export YARN_CONF_DIR=${YARN_HOME}/etc/hadoop" >> /etc/profile  
RUN echo "export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH" >>
/etc/profile  
  
RUN yum install -y which  
  
# Download hadoop  
RUN wget -q -O -
http://mirrors.hust.edu.cn/apache/hadoop/common/hadoop-2.7.5/hadoop-2.7.5.tar.gz
| tar -xzf - -C /opt/ \  
&& mv /opt/hadoop-2.7.5 /opt/hadoop  
  
RUN mkdir -p /data/hadoop/hdfs/nn \  
&& mkdir -p /data/hadoop/hdfs/dn \  
&& mkdir -p /data/hadoop/tmp  
  
COPY core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml  
COPY hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml  
COPY mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml  
COPY yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml  
  
COPY bootstrap_keep.sh /bin/bootstrap_keep.sh  
COPY bootstrap_ssh.sh /bin/bootstrap_ssh.sh  
COPY bootstrap_hadoop.sh /bin/bootstrap_hadoop.sh  
COPY bootstrap.sh /bin/bootstrap.sh  
  
RUN chmod +x /bin/bootstrap*  
  
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa \  
&& cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \  
&& chmod 0600 ~/.ssh/authorized_keys  
  
EXPOSE 9000 50010 50020 50070 50075 50090 8088  
VOLUME ["/data/hadoop/hdfs/nn", "/data/hadoop/hdfs/dn"]  
  
ENTRYPOINT /bin/bootstrap.sh $KEEP

