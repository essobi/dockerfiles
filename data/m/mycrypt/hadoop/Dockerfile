# fork from https://github.com/sequenceiq/hadoop-docker  
# Creates pseudo distributed hadoop 2.5.1  
#  
# docker build -t sequenceiq/hadoop .  
FROM mycrypt/debian-java  
MAINTAINER Bai Xiaoyong lostitle@gmail.com  
  
USER root  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy build-essential curl  
  
# passwordless ssh  
#RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
#RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
# hadoop  
RUN mkdir /opt/hadoop  
RUN wget -qO-
http://mirror.nus.edu.sg/apache/hadoop/common/hadoop-2.5.1/hadoop-2.5.1.tar.gz
\  
| tar zxvf - -C /opt/hadoop --strip 1  
  
ENV PATH /opt/hadoop/bin:$PATH  
  
ENV HADOOP_PREFIX /opt/hadoop  
RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/lib/jvm/java-7-oracle\nexport HADOOP_PREFIX=/opt/hadoop\nexport
HADOOP_HOME=/opt/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop/:' $HADOOP_PREFIX/etc/hadoop/hadoop-
env.sh  
#RUN . $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN mkdir $HADOOP_PREFIX/input  
RUN cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input  
  
# pseudo distributed  
ADD core-site.xml.template $HADOOP_PREFIX/etc/hadoop/core-site.xml.template  
RUN sed s/HOSTNAME/localhost/ /opt/hadoop/etc/hadoop/core-site.xml.template >
/opt/hadoop/etc/hadoop/core-site.xml  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
  
RUN $HADOOP_PREFIX/bin/hdfs namenode -format  
  
# fixing the libhadoop.so like a boss  
RUN rm /opt/hadoop/lib/native/*  
RUN curl -Ls http://dl.bintray.com/sequenceiq/sequenceiq-bin/hadoop-
native-64-2.5.0.tar|tar -xz -C /opt/hadoop/lib/native/  
  
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
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
ENV BOOTSTRAP /etc/bootstrap.sh  
  
# workingaround docker.io build error  
RUN ls -la /opt/hadoop/etc/hadoop/*-env.sh  
RUN chmod +x /opt/hadoop/etc/hadoop/*-env.sh  
RUN ls -la /opt/hadoop/etc/hadoop/*-env.sh  
  
# fix the 254 error code  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "Port 2122" >> /etc/ssh/sshd_config  
  
RUN service ssh start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh &&
$HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfs -mkdir -p
/user/root  
RUN service ssh start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh &&
$HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfs -put
$HADOOP_PREFIX/etc/hadoop/ input  
  
#CMD ["/etc/bootstrap.sh", "-d"]  
RUN echo "\  
[program:hadoop]\n\  
command=/etc/bootstrap.sh\n\  
" >> /etc/supervisor/conf.d/supervisord.conf  
  
RUN echo "\n\  
export HADOOP_HOME=/opt/hadoop\n\  
PATH=$HADOOP_HOME/bin:$PATH\  
\n\  
" >> /etc/profile  
  
EXPOSE 50020 50090 50070 50010 50075 8031 8032 8033 8040 8042 49707 22 8088
8030  

