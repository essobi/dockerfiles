# Dockerfile  
#  
#  
# Created by Youssef de Madeen Amadou on 17-05-09.  
#  
# Installer et configurer un simple cluster Hadoop  
#  
FROM centos:latest  
LABEL maintainer "youssef.amadou@live.com"  
LABEL description "Installer et configurer un simple cluster Hadoop"  
LABEL vendor ""  
USER root  
  
# installation des packages  
RUN yum -y --enablerepo=extras install epel-release && \  
yum -y update && \  
yum -y install curl tar sudo nano which openssh-server openssh-client rsync
sshd  
  
# ssh sans mot de passe  
RUN rm -f /root/.ssh/id_rsa && \  
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \  
cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \  
chmod 600 ~/.ssh/authorized_keys && \  
chmod 700 ~/.ssh  
  
RUN ssh-keygen -t rsa -P '' -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -t dsa -P '' -f /etc/ssh/ssh_host_dsa_key  
  
# alterations aux configurations sshd  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "AllowUsers root" >> /etc/ssh/sshd_config  
  
# installation de java  
RUN mkdir -p /usr/java/default && \  
curl -s http://ftp.heanet.ie/mirrors/funtoo/distfiles/oracle-
java/jdk-8u112-linux-x64.tar.gz | tar --strip-components=1 -xz -C
/usr/java/default/  
  
ENV JAVA_HOME=/usr/java/default  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# installation de hadoop 2.8.0  
RUN curl -s
http://apache.forsale.plus/hadoop/common/hadoop-2.8.0/hadoop-2.8.0.tar.gz |
tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s ./hadoop-2.8.0 hadoop  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV HADOOP_HOME /usr/local/hadoop  
ENV PATH $PATH:$HADOOP_PREFIX/bin:$HADOOP_PREFIX/sbin  
RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/java/default\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport
HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*.sh  
RUN chmod +x /usr/local/hadoop/sbin/*.sh  
RUN $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
# configuration du cluster  
RUN mkdir -p $HADOOP_PREFIX/input && cp $HADOOP_PREFIX/etc/hadoop/*.xml
$HADOOP_PREFIX/input  
  
ADD core-site.xml.template $HADOOP_PREFIX/etc/hadoop/core-site.xml.template  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
  
# initialisation du namenode  
RUN $HADOOP_PREFIX/bin/hdfs namenode -format  
  
# creation de repertoires partages  
RUN mkdir -p /opt/hadoop/logs  
RUN mkdir -p /root/shared  
  
# configuration pour demarrer le cluster en meme temps que l'archive  
ADD entrypoint.sh /etc/entrypoint.sh  
RUN chown root:root /etc/entrypoint.sh  
RUN chmod 700 /etc/entrypoint.sh  
ENV ENTRYPOINT /etc/entrypoint.sh  
  
# ports d'acces aux interfaces web sur la machine hote  
EXPOSE 50020 50090 50070 50010 50075 8031 8032 8033 8040 8042 49707 22 8088
8030 2022  
CMD ["/etc/entrypoint.sh","-d"]  
  
# FIN  

