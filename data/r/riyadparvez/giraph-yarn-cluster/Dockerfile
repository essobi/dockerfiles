# Creates pseudo distributed hadoop 2.7.1  
#  
# sudo docker build -t yarn_cluster .  
FROM sequenceiq/pam:centos-6.5  
MAINTAINER Riyad Parvez <Riyad Parvez>  
  
USER root  
  
# install dev tools  
RUN yum install -y curl which git tar sudo openssh-server openssh-clients
rsync | true  
RUN yum update -y libselinux | true  
RUN curl -L# https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-
apache-maven.repo > /etc/yum.repos.d/epel-apache-maven.repo  
RUN yum install -y maven2  
  
# passwordless ssh  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
# java  
RUN curl -LO 'http://download.oracle.com/otn-
pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.rpm' -H 'Cookie:
oraclelicense=accept-securebackup-cookie'  
RUN rpm -i jdk-7u71-linux-x64.rpm  
RUN rm jdk-7u71-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/default  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# hadoop  
RUN curl -s
http://ftp.jaist.ac.jp/pub/apache/hadoop/core/hadoop-2.7.1/hadoop-2.7.1.tar.gz
| tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s ./hadoop-2.7.1 hadoop  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV HADOOP_COMMON_HOME /usr/local/hadoop  
ENV HADOOP_HDFS_HOME /usr/local/hadoop  
ENV HADOOP_MAPRED_HOME /usr/local/hadoop  
ENV HADOOP_YARN_HOME /usr/local/hadoop  
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop  
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
  
RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/java/default\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport
HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
RUN mkdir $HADOOP_PREFIX/input  
RUN cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input  
  
# pseudo distributed  
ADD core-site.xml $HADOOP_PREFIX/etc/hadoop/core-site.xml  
#RUN sed s/HOSTNAME/localhost/ /usr/local/hadoop/etc/hadoop/core-
site.xml.template > /usr/local/hadoop/etc/hadoop/core-site.xml  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
  
RUN $HADOOP_PREFIX/bin/hdfs namenode -format  
  
# fixing the libhadoop.so like a boss  
RUN rm /usr/local/hadoop/lib/native/*  
RUN curl -Ls http://dl.bintray.com/sequenceiq/sequenceiq-bin/hadoop-
native-64-2.7.0.tar | tar -x -C /usr/local/hadoop/lib/native/  
  
ADD ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  
RUN chown root:root /root/.ssh/config  
  
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
ENV BOOTSTRAP /etc/bootstrap.sh  
  
# workingaround docker.io build error  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
  
# fix the 254 error code  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "Port 2122" >> /etc/ssh/sshd_config  
  
ENV YARN_HOME $HADOOP_PREFIX  
RUN echo '# Hadoop' >> /etc/profile \  
&& echo "export HADOOP_PREFIX=$HADOOP_PREFIX" >> /etc/profile \  
&& echo 'export PATH=$PATH:$HADOOP_PREFIX/bin:$HADOOP_PREFIX/sbin' >>
/etc/profile \  
&& echo 'export HADOOP_MAPRED_HOME=$HADOOP_PREFIX' >> /etc/profile \  
&& echo 'export HADOOP_COMMON_HOME=$HADOOP_PREFIX' >> /etc/profile \  
&& echo 'export HADOOP_HDFS_HOME=$HADOOP_PREFIX' >> /etc/profile \  
&& echo 'export HADOOP_HOME=$HADOOP_PREFIX' >> /etc/profile \  
&& echo 'export ENV HADOOP_CONF_DIR=$HADOOP_PREFIX/etc/hadoop' >> /etc/profile
\  
&& echo 'export YARN_HOME=$HADOOP_PREFIX' >> /etc/profile  
  
# Giraph  
ADD giraph_compile.patch /etc/giraph_compile.patch  
ENV GIRAPH_PARENT /usr/local  
  
RUN cd $GIRAPH_PARENT \  
&& curl https://apache.googlesource.com/giraph/+archive/release-1.1.tar.gz >
$GIRAPH_PARENT/giraph-1.1.tar.gz \  
&& mkdir -p $GIRAPH_PARENT/giraph-1.1 \  
&& tar -xf $GIRAPH_PARENT/giraph-1.1.tar.gz -C $GIRAPH_PARENT/giraph-1.1 \  
&& rm -f $GIRAPH_PARENT/giraph-1.1.tar.gz \  
&& ln -s $GIRAPH_PARENT/giraph-1.1 giraph \  
&& cd $GIRAPH_PARENT/giraph \  
&& patch -p0 < /etc/giraph_compile.patch \  
&& mvn -Phadoop_yarn -Dhadoop.version=2.7.1 -DskipTests clean package || true  
  
ENV GIRAPH_HOME /usr/local/giraph  
ENV GIRAPH_PREFIX /usr/local/giraph  
  
RUN echo '# Giraph' >> /etc/profile \  
&& echo "export GIRAPH_PREFIX=$GIRAPH_PREFIX" >> /etc/profile \  
&& echo 'export GIRAPH_HOME=$GIRAPH_PREFIX' >> /etc/profile  
  
ADD tiny-graph.txt $GIRAPH_PREFIX/tiny-graph.txt  
ADD run-giraph-example.sh $GIRAPH_PREFIX/run-giraph-example.sh  
RUN chown root:root $GIRAPH_PREFIX/run-giraph-example.sh && chmod 700
$GIRAPH_PREFIX/run-giraph-example.sh  
  
CMD ["/etc/bootstrap.sh", "-d"]  
  
# Hdfs ports  
EXPOSE 50010 50020 50070 50075 50090  
# Mapred ports  
EXPOSE 19888  
#Yarn ports  
EXPOSE 8030 8031 8032 8033 8040 8042 8088  
#Other ports  
EXPOSE 49707 2122  

