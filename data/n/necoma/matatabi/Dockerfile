# Creates pseudo distributed hadoop 2.2.0 on Ubuntu 14.04  
#  
# docker build -t necoma/matatabi .  
FROM sequenceiq/pam:ubuntu-14.04  
MAINTAINER NECOMA  
  
ENV version 1.0  
LABEL version=${version}  
  
USER root  
ENV HOME /  
  
# http://stackoverflow.com/questions/20635472/using-the-run-instruction-in-a-
dockerfile-with-source-does-not-work  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# install dev tools  
RUN echo "mysql-server-5.5 mysql-server/root_password password password" |
debconf-set-selections  
RUN echo "mysql-server-5.5 mysql-server/root_password_again password password"
| debconf-set-selections  
RUN apt-get update  
RUN apt-get install -y curl tar sudo openssh-server openssh-client rsync git
python-pip mysql-server lzop jq bison ruby nano gnuplot  
  
# passwordless ssh  
RUN rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key
/root/.ssh/id_rsa  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
ADD ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  
RUN chown root:root /root/.ssh/config  
  
# git clone matatabi_script  
#RUN git clone -b ${version} https://github.com/necoma/matatabi_script.git  
RUN git clone https://github.com/necoma/matatabi_script.git  
# install NECOMAtter  
ADD NECOMAtter-install.sh /root/NECOMAtter-install.sh  
RUN service ssh start && /root/NECOMAtter-install.sh  
  
# java  
RUN mkdir -p /usr/java/default && \  
curl -Ls 'http://download.oracle.com/otn-
pub/java/jdk/7u79-b14/jdk-7u79-linux-x64.tar.gz' -H 'Cookie:
oraclelicense=accept-securebackup-cookie' | \  
tar --strip-components=1 -xz -C /usr/java/default/  
  
ENV JAVA_HOME /usr/java/default/  
ENV PATH
/usr/local/presto/bin:/usr/local/hadoop/bin:/usr/local/hadoop/sbin:$PATH:$JAVA_HOME/bin  
  
# hadoop  
RUN curl -s
https://archive.apache.org/dist/hadoop/core/hadoop-2.2.0/hadoop-2.2.0.tar.gz |
tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s ./hadoop-2.2.0 hadoop  
ADD extlibs/hadoop-lzo-0.4.15.jar /usr/local/hadoop/share/hadoop/common/  
  
# hive  
RUN curl -s https://archive.apache.org/dist/hive/hive-0.13.1/apache-
hive-0.13.1-bin.tar.gz | tar -xz -C /usr/local/  
ADD hive-site.xml /usr/local/apache-hive-0.13.1-bin/conf/hive-site.xml  
ADD extlibs/mysql-connector-java-5.1.18-bin.jar /usr/local/apache-
hive-0.13.1-bin/lib/mysql-connector-java-5.1.18-bin.jar  
ADD mysql-hive.sql /root/mysql-hive.sql  
RUN service mysql start && mysql -u root -ppassword < /root/mysql-hive.sql  
ADD extlibs/hadoop-pcap-serde-0.2-SNAPSHOT-jar-with-dependencies.jar
/usr/local/apache-hive-0.13.1-bin/lib/  
ADD extlibs/hadoop-lzo-0.4.15.jar /usr/local/apache-hive-0.13.1-bin/lib/  
ADD extlibs/json-hive-serde-1.0.jar /usr/local/apache-hive-0.13.1-bin/lib/  
  
# presto  
RUN curl -s https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/0.66/presto-server-0.66.tar.gz | tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s ./presto-server-0.66 presto  
RUN mkdir -p /usr/local/presto/etc  
RUN curl -s https://repo1.maven.org/maven2/com/facebook/presto/presto-
cli/0.54/presto-cli-0.54-executable.jar > /usr/local/presto/bin/presto-
cli-0.100-executable.jar  
RUN chmod 755 /usr/local/presto/bin/presto-cli-0.100-executable.jar  
RUN mkdir -p /home/hadoop/downloads/  
ADD extlibs/json-hive-serde-1.0.jar /usr/local/presto/plugin/hive-cdh5/  
ADD extlibs/hadoop-lzo-0.4.15.jar /usr/local/presto/plugin/hive-cdh5/  
ADD extlibs/hadoop-pcap-lib-0.2-SNAPSHOT.jar /usr/local/presto/plugin/hive-
cdh5/  
ADD extlibs/hadoop-pcap-serde-0.2-SNAPSHOT.jar /usr/local/presto/plugin/hive-
cdh5/  
ADD extlibs/json-hive-serde-1.0.jar /home/hadoop/downloads/json-hive-
serde-1.0.jar  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/java/default\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport
HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
# additional packages  
RUN apt-get install -y python-dev libfreetype6-dev libpng-dev  
RUN pip install matplotlib  
RUN pip install pandas  
RUN pip install pyhive  
  
# necoma-version nfdump  
RUN git clone https://github.com/necoma/nfdump  
RUN cd /nfdump && ./configure --prefix=/usr && make && make install  
  
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
  
# hiveserver  
ADD hiveserver.sh /root/hiveserver.sh  
ADD hiveserver2.sh /root/hiveserver2.sh  
  
# presto  
ADD presto.config.properties /usr/local/presto/etc/config.properties  
ADD presto.jvm.config /usr/local/presto/etc/jvm.config  
ADD presto.catalog /usr/local/presto/etc/catalog/hive.properties  
ADD presto.sh /usr/local/presto/bin/presto  
RUN chmod 755 /usr/local/presto/bin/presto  
  
# fixing the libhadoop.so like a boss  
RUN rm /usr/local/hadoop/lib/native/*  
ADD hadoop-native-64-2.2.0.tar.gz /usr/local/hadoop/lib/native/  
RUN ldconfig /usr/local/hadoop/lib/native/  
RUN cd /usr/local/hadoop/lib/native/ &&ln -s libhadoop.so.1.0.0 libhadoop.so
&&ln -s libhdfs.so.0.0.0 libhdfs.so && ln -s libgplcompression.so.0.0.0
libgplcompression.so  
  
# installing supervisord  
RUN apt-get install -y supervisor  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
ENV BOOTSTRAP /etc/bootstrap.sh  
  
ADD bash.bashrc /.bashrc  
ADD bash.bashrc /.profile  
  
# workingaround docker.io build error  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
  
# fix the 254 error code  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "Port 2122" >> /etc/ssh/sshd_config  
  
# install matatabi_script (git clone is already done.)  
ADD matatabi-hive-init.sh /root/matatabi-hive-init.sh  
RUN service ssh start && service mysql start &&
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && $HADOOP_PREFIX/sbin/start-dfs.sh &&
$HADOOP_PREFIX/sbin/start-yarn.sh && /var/lib/neo4j/bin/neo4j start-no-wait &&
/etc/init.d/supervisor start && sleep 30 && /root/matatabi-hive-init.sh  
  
CMD ["/etc/bootstrap.sh", "-bash"]  
#CMD ["/etc/bootstrap.sh", "-d"]  
EXPOSE 50020 50090 50070 50010 50075 8031 8032 8033 8040 8042 49707 22 8088
8030  
# for NECOMAtter, neo4j  
EXPOSE 8000 7474  

