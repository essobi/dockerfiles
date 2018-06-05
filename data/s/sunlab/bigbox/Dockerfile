FROM centos:7  
  
ENV container docker  
  
ADD http://www.apache.org/dist/bigtop/stable/repos/centos7/bigtop.repo
/etc/yum.repos.d/bigtop.repo  
  
RUN yum install epel-release -y; \  
yum update -y ; \  
yum install openssh* wget axel bzip2 unzip gzip git gcc-c++ lsof \  
java-1.8.0-openjdk java-1.8.0-openjdk-devel \  
mariadb mysql-connector-java \  
sudo hostname -y ; \  
yum clean all; rm -rf /var/cache/yum  
  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;\  
mv -f /bin/systemctl{,.orig} ; \  
ln -sf /bin/{false,systemctl}  
  
  
# 0 SSH  
# SSH service start  
RUN ssh-keygen -A ; \  
mkdir -p /var/run/sshd ; \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd ; \  
sed 's@#UseDNS yes@UseDNS no@g' -i /etc/ssh/sshd_config # prevent stucks here
>> SSH2_MSG_SERVICE_ACCEPT received  
# SSH service end  
  
  
ADD config/ssh /root/.ssh  
RUN chown -R root:root /root/.ssh ; \  
chmod 0700 /root/.ssh ; \  
chmod 0600 /root/.ssh/{id_rsa,id_rsa.pub,authorized_keys}  
  
# 1 Hadoop, Spark, .... from bigtop  
RUN yum install zookeeper-server hadoop-yarn-proxyserver \  
hadoop-hdfs-namenode hadoop-hdfs-datanode \  
hadoop-yarn-resourcemanager hadoop-mapreduce-historyserver \  
hadoop-yarn-nodemanager \  
spark-worker spark-master \  
hbase-regionserver hbase-master hbase-thrift \  
hive-metastore pig -y ; \  
yum clean all; rm -rf /var/cache/yum  
  
# 2. Configure JAVA_HOME, Scala, SBT etc.  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java" >> /etc/profile.d/bigbox.sh  
  
ENV SCALA_VERSION 2.11.12  
RUN yum -y localinstall
https://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.rpm  
  
ENV SBT_VERSION 1.1.0  
RUN wget
https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz
; \  
tar -xzf sbt-${SBT_VERSION}.tgz ; \  
rm -rf sbt-${SBT_VERSION}.tgz ; \  
mv sbt /usr/lib/ ; \  
ln -sf /usr/lib/sbt/bin/sbt /usr/bin/  
# 3. Clone Materials to /bigdata-bootcamp  
RUN git clone https://bitbucket.org/realsunlab/bigdata-bootcamp.git /bigdata-
bootcamp  
  
# 4. Add Extra Basic scripts  
RUN git clone https://github.com/yuikns/bigbox-scripts.git /scripts  
# 5. Overide local scripts and configs  
COPY scripts /scripts/  
  
# copy config/hadoop/* =>  
COPY config/hadoop /etc/hadoop/conf/  
COPY config/hbase /etc/hbase/conf/  
COPY config/hive /etc/hive/conf/  
COPY config/spark /etc/spark/conf/  
COPY config/zookeeper /etc/zookeeper/conf/  
  
  
# 6. Execute initialization script  
RUN /scripts/init.sh  
  
# 7. Install Miniconda Python  
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
-O miniconda.sh && chmod +x miniconda.sh && ./miniconda.sh -b -p
/usr/local/conda3 && rm -rf miniconda.sh  
ENV PATH /usr/local/conda3/bin:$PATH  
RUN echo 'export PATH=/usr/local/conda3/bin:$PATH' >> /etc/profile.d/bigbox.sh  
RUN conda install --yes numpy ipython  
RUN pip install asciinema  
  
  
# N. tini  
ENV TINI_VERSION v0.18.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
  
EXPOSE 22  
# CMD ["/usr/sbin/sshd", "-D"]  
CMD ["/bin/bash"]

