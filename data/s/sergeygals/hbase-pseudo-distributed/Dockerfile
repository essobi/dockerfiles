FROM ubuntu:14.04  
MAINTAINER Sergey Galkin <sgalkin@mirantis.com>  
LABEL version="0.1"  
LABEL description="Hbase with hadoop in pseudo-distributed mode "  
ARG hadoop_ver=2.7.3  
ARG hbase_ver=1.2.3  
# Install Java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
apt-get update && \  
apt-get install -y software-properties-common ssh supervisor && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
# Install hadoop  
RUN wget --progress=dot:giga -P /tmp/ http://apache-
mirror.rbc.ru/pub/apache/hadoop/common/hadoop-$hadoop_ver/hadoop-$hadoop_ver.tar.gz
&& \  
mkdir -p /opt && \  
tar xzf /tmp/hadoop-$hadoop_ver.tar.gz -C /opt/ && \  
ln -s /opt/hadoop-$hadoop_ver /opt/hadoop && \  
rm /tmp/hadoop-$hadoop_ver.tar.gz && \  
rm -rf /opt/hadoop-$hadoop_ver/share/doc  
# Install hbase  
RUN wget --progress=dot:giga -P /tmp/ http://apache-
mirror.rbc.ru/pub/apache/hbase/$hbase_ver/hbase-$hbase_ver-bin.tar.gz && \  
tar xzf /tmp/hbase-$hbase_ver-bin.tar.gz -C /opt/ && \  
ln -s /opt/hbase-$hbase_ver /opt/hbase && \  
rm /tmp/hbase-$hbase_ver-bin.tar.gz && \  
rm -rf /opt/hbase-1.2.3/docs  
# Generate ssh keys for hadoop/hbase start  
ADD ssh_config /root/.ssh/config  
RUN ssh-keygen -t dsa -P '' -f /root/.ssh/id_dsa && \  
cat /root/.ssh/id_dsa.pub >> /root/.ssh/authorized_keys && \  
chmod 0600 /root/.ssh/authorized_keys  
# Workaround for start ssh -D  
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd  
# Configure Hadoop  
RUN sed -i 's/${JAVA_HOME}/\/usr\/lib\/jvm\/java-8-oracle/g'
/opt/hadoop-$hadoop_ver/etc/hadoop/hadoop-env.sh  
ADD core-site.xml /opt/hadoop-$hadoop_ver/etc/hadoop/core-site.xml  
ADD hdfs-site.xml /opt/hadoop-$hadoop_ver/etc/hadoop/hdfs-site.xml  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  
RUN /opt/hadoop-$hadoop_ver/bin/hdfs namenode -format  
# Configure hbase  
RUN sed -i '2s/^/export JAVA_HOME=\/usr\/lib\/jvm\/java-8-oracle\n/'
/opt/hbase/bin/hbase-config.sh  
ADD hbase-site.xml /opt/hbase/conf/hbase-site.xml  
# Configure supervisord  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD bashrc /root/.bashrc  
# Hdfs ports  
EXPOSE 50010 50020 50070 50090 9000  
# Mapred ports  
EXPOSE 10020 19888  
# Yarn ports  
EXPOSE 8030 8031 8032 8033 8040 8042 8088  
# Hbase ports  
EXPOSE 2181 16000 16001 16010 16301  
# Other ports  
EXPOSE 22  
CMD ["/usr/bin/supervisord"]  
  

