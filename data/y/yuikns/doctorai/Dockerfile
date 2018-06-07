FROM fedora:25  
  
RUN curl
http://www.apache.org/dist/bigtop/bigtop-1.2.0/repos/fedora25/bigtop.repo -o
/etc/yum.repos.d/bigtop.repo  
#RUN curl
http://www.apache.org/dist/bigtop/bigtop-1.2.0/repos/centos7/bigtop.repo -o
/etc/yum.repos.d/bigtop.repo  
  
RUN dnf update -y ; \  
dnf install openssh* wget bzip2 unzip gzip git gcc-c++ \  
java-1.8.0-openjdk java-1.8.0-openjdk-devel \  
sudo hostname -y ; \  
dnf clean all  
  
# SSH service start  
RUN ssh-keygen -A  
RUN mkdir /var/run/sshd  
  
# use password 'mypassword123' here  
RUN echo 'root:youjumpijump' | chpasswd  
# RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# SSH service end  
  
# JAVA environment start  
#ENV NOTVISIBLE "in users profile"  
#RUN echo "export VISIBLE=now" >> /etc/profile  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java" >> /etc/profile  
  
# JAVA environment end  
  
# hadoop init start  
#  
# RUN dnf install zookeeper-server hadoop-yarn-proxyserver hadoop-hdfs-
namenode hadoop-hdfs-datanode \  
# hadoop-yarn-resourcemanager hadoop-mapreduce-historyserver \  
# hadoop-yarn-nodemanager \  
# spark-worker spark-master \  
# hbase-regionserver hbase-master hbase-thrift \  
# hive-metastore -y  
#  
# ADD data/hadoop/conf /etc/hadoop/conf.docker  
#  
# RUN rm -f /etc/alternatives/hadoop-conf ; \  
# ln -sf /etc/hadoop/conf.docker /etc/alternatives/hadoop-conf  
#  
# RUN mkdir /data ; \  
# chown -R hdfs:hadoop /data ; \  
# service zookeeper-server condrestart ; \  
# service hadoop-hdfs-namenode init ; \  
# sudo -u hdfs hdfs dfs -mkdir /tmp ; \  
# sudo -u hdfs hdfs dfs -chmod 777 /tmp  
  
# hadoop init end  
  
ADD scripts/config.sh /scripts/  
  
ADD scripts/env.init.sh /scripts/  
  
RUN /scripts/env.init.sh  
  
# post configure for zeppelin  
ADD data/zeppelin/conf/ /usr/local/zeppelin/conf/  
  
RUN if [ -d /usr/local/zeppelin-0.7.1-bin-netinst ]; then \  
chown -R zeppelin:zeppelin /usr/local/zeppelin ; \  
chown -R zeppelin:zeppelin /usr/local/zeppelin-0.7.1-bin-netinst ; fi  
  
# ENV PATH /usr/local/zeppelin/bin:$PATH  
# RUN echo 'export PATH=/usr/local/zeppelin/bin:$PATH' >> /etc/profile  
  
EXPOSE 9530  
  
# /usr/bin/sudo -i -u zeppelin /usr/local/zeppelin/bin/zeppelin-daemon.sh
start  
# /usr/bin/sudo -i -u zeppelin /usr/local/zeppelin/bin/zeppelin-daemon.sh stop  
ADD scripts/zeppelin_serve.sh /scripts/  
  
# zeppelin end  
  
  
# # add miniconda  
# RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O miniconda.sh && chmod +x miniconda.sh && ./miniconda.sh -b
-p /usr/local/mc && rm -rf miniconda.sh  
# ENV PATH /usr/local/mc/bin:$PATH  
# RUN echo 'export PATH=/usr/local/mc/bin:$PATH' >> /etc/profile  
# RUN conda install --yes numpy theano ipython  
  
#  
# # setup  
# ENV DOCKER_FRONTEND "noninteractive"  
# RUN cd /app && ./setup && bazel build //...  
  
ADD src/ /usr/local/src/doctorai  
  
  
# expose 22, and start sshd in default  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
  

