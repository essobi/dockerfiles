FROM centos:centos7.3.1611  
ENV HADOOP_TAR=mirrors.dotsrc.org  
  
RUN yum install -y java-1.8.0-openjdk openssh-server openssh-clients sudo
which && \  
yum clean all && \  
mkdir /app && \  
groupadd app && \  
chown root:app /app && \  
chmod g+rwx /app && \  
adduser -m -p '*' -s /bin/bash -G app hadoop && \  
ssh-keygen -A && \  
/usr/sbin/sshd && \  
ssh-keyscan -H localhost,0.0.0.0,127.0.0.1 > /etc/ssh/ssh_known_hosts && \  
ssh-keyscan -H localhost >> /etc/ssh/ssh_known_hosts && \  
ssh-keyscan -H 0.0.0.0 >> /etc/ssh/ssh_known_hosts && \  
ssh-keyscan -H 127.0.0.1 >> /etc/ssh/ssh_known_hosts && \  
echo "hadoop ALL=(root) NOPASSWD: /usr/sbin/sshd" >> /etc/sudoers  
  
WORKDIR /app  
USER hadoop  
  
RUN curl -O
http://$HADOOP_TAR/apache/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz && \  
tar -zxf /app/hadoop-2.7.3.tar.gz && \  
rm /app/hadoop-2.7.3.tar.gz && \  
ssh-keygen -f ~/.ssh/id_rsa -P "" && \  
mv ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys && \  
cp /etc/ssh/ssh_known_hosts ~/.ssh/known_hosts  
  
USER root  
COPY ./files/*.xml /app/hadoop-2.7.3/etc/hadoop/  
COPY ./files/hadoop-env.sh /app/hadoop-2.7.3/etc/hadoop/  
COPY ./files/hadoop.sh /app  
  
RUN chown -R hadoop:app /app/hadoop-2.7.3/etc/hadoop && \  
chown hadoop:app /app/hadoop-2.7.3/etc/hadoop/hadoop-env.sh && \  
chown hadoop:app /app/hadoop.sh  
  
USER hadoop  
  
RUN /app/hadoop-2.7.3/bin/hdfs namenode -format && \  
chmod a+x /app/hadoop.sh  
  
EXPOSE 9870  
EXPOSE 8088  
EXPOSE 50070  
VOLUME ["/home/hadoop/.hadoop"]  
CMD ["/app/hadoop.sh"]  
  

