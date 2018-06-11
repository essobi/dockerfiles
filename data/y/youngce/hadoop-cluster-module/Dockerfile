FROM dockerfile/java:oracle-java7  
  
  
  
#SSH  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa && cat ~/.ssh/id_dsa.pub >>
~/.ssh/authorized_keys  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
# hadoop  
ENV HADOOP_HOME /usr/local/hadoop  
ENV HADOOP_PKG_NAME hadoop-2.6.0  
RUN wget
http://www.eu.apache.org/dist/hadoop/common/$HADOOP_PKG_NAME/$HADOOP_PKG_NAME.tar.gz  
  
RUN tar xvzf $HADOOP_PKG_NAME.tar.gz && rm -f $HADOOP_PKG_NAME.tar.gz && mv
$HADOOP_PKG_NAME $HADOOP_HOME  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV HADOOP_COMMON_HOME /usr/local/hadoop  
ENV HADOOP_HDFS_HOME /usr/local/hadoop  
ENV HADOOP_MAPRED_HOME /usr/local/hadoop  
ENV HADOOP_YARN_HOME /usr/local/hadoop  
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop  
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
  
RUN echo "export VISIBLE=now" >> /etc/profile && echo "export
JAVA_HOME=$JAVA_HOME" >> /etc/profile && echo "export
HADOOP_HOME=$HADOOP_HOME" >> /etc/profile && echo "export
PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH" >> /etc/profile  
  
RUN mkdir /name  
ADD core-site.xml /usr/local/hadoop/etc/hadoop/core-site.xml  
ADD hadoop-env.sh /usr/local/hadoop/etc/hadoop/hadoop-env.sh  
ADD hdfs-site.xml /usr/local/hadoop/etc/hadoop/hdfs-site.xml  
ADD mapred-env.sh /usr/local/hadoop/etc/hadoop/mapred-env.sh  
ADD mapred-site.xml /usr/local/hadoop/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml /usr/local/hadoop/etc/hadoop/yarn-site.xml  
ADD slaves /usr/local/hadoop/etc/hadoop/slaves  
ADD masters /usr/local/hadoop/etc/hadoop/masters  
  
#ADD hosts /etc/hosts  
#ADD hosts /hosts  
#ADD Initialize /Initialize  
#RUN chmod 755 /Initialize  
WORKDIR /  
VOLUME ["/etc/hosts"]  
  
EXPOSE 50020 50090 50070 50010 50075 8031 8032 8033 8040 8042 49707 22 8088
8030 9000  
CMD ["/usr/sbin/sshd", "-D"]  
  

