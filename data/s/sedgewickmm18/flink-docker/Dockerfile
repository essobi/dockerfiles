# Creates pseudo distributed hadoop 2.7.1  
#  
# docker build -t sequenceiq/hadoop .  
FROM java:8-jre-alpine  
#MAINTAINER SequenceIQ  
# Install requirements  
RUN apk --no-cache update  
RUN apk add --update bash snappy unzip wget curl docker jq coreutils openssh
procps nginx  
  
USER root  
ENV HADOOP_VERSION="2.7.3"  
ENV ZOOKEEPER_VERSION="3.4.9"  
ENV FLINK_VERSION="1.1.4"  
ENV JAVA_HOME /usr  
  
# Download hadoop, zookeeper and flink  
ADD download-hadoop.sh /tmp/download-hadoop.sh  
RUN chmod a+x /tmp/download-hadoop.sh && sync && /tmp/download-hadoop.sh  
RUN tar xfz /tmp/hadoop-${HADOOP_VERSION}.tar.gz -C /usr/local && rm
/tmp/hadoop-${HADOOP_VERSION}.tar.gz && \  
cd /usr/local && ln -s ./hadoop-${HADOOP_VERSION} hadoop  
RUN tar xfz /tmp/zookeeper-${ZOOKEEPER_VERSION}.tar.gz -C /usr/local && rm
/tmp/zookeeper-${ZOOKEEPER_VERSION}.tar.gz && \  
cd /usr/local && ln -s ./zookeeper-${ZOOKEEPER_VERSION} zookeeper  
RUN tar xfz /tmp/flink-${FLINK_VERSION}.tar.gz -C /usr/local && rm
/tmp/flink-${FLINK_VERSION}.tar.gz && \  
cd /usr/local && ln -s ./flink-${FLINK_VERSION} flink  
  
#Configure zookeeper  
RUN mv /usr/local/zookeeper/conf/zoo_sample.cfg
/usr/local/zookeeper/conf/zoo.cfg  
  
ENV ZK_HOME /usr/local/zookeeper  
RUN sed -i "s|/tmp/zookeeper|$ZK_HOME/data|g" $ZK_HOME/conf/zoo.cfg; mkdir
$ZK_HOME/data  
  
WORKDIR /usr/local/zookeeper  
VOLUME ["/usr/local/zookeeper/conf", "/usr/local/zookeeper/data",
"/usr/local/hadoop/dfs", "/usr/local/hadoop/journal/data"]  
  
# Preset environment variables for convenience  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV HADOOP_COMMON_HOME /usr/local/hadoop  
ENV HADOOP_HDFS_HOME /usr/local/hadoop  
ENV HADOOP_MAPRED_HOME /usr/local/hadoop  
ENV HADOOP_YARN_HOME /usr/local/hadoop  
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop  
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
ENV FLINK_PREFIX /usr/local/flink  
  
# Configure hadoop  
RUN ls $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=/usr\nexport
HADOOP_PREFIX=/usr/local/hadoop\nexport HADOOP_HOME=/usr/local/hadoop\n:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN . $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
RUN mkdir $HADOOP_PREFIX/input  
RUN cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input  
  
# adding HA setup  
ADD core-site.xml $HADOOP_PREFIX/etc/hadoop/core-site.xml  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
ADD flink-conf.yaml $FLINK_PREFIX/conf/flink-conf.yaml  
  
# remove that we have proper native libraries, resp. a library for alpine  
# to include netgroup support (setnetgrent etc.)  
# see the output of HADOOP_LOGLEVEL=ALL bin/hadoop checknative -a  
# fixing the libhadoop.so like a boss  
#RUN rm -rf /usr/local/hadoop/lib/native  
#RUN mv /tmp/native /usr/local/hadoop/lib  
ADD libstub.so /usr/lib  
RUN echo "export LD_PRELOAD=/usr/lib/libstub.so" >>
/usr/local/hadoop/libexec/hadoop-config.sh && \  
echo "export LD_PRELOAD=/usr/lib/libstub.so" >>
/usr/local/hadoop/libexec/hdfs-config.sh && \  
ln -s /usr/lib/libcrypto.so.1.0.0 /usr/lib/libcrypto.so  
  
# accept unknown hosts during deployment  
ADD ssh_config /root/.ssh/config  
#RUN chmod 600 /root/.ssh/config  
#RUN chown root:root /root/.ssh/config  
# # installing supervisord - should be reenabled/substituted with amalgam8
later on  
# RUN yum install -y python-setuptools  
# RUN easy_install pip  
# RUN curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -o
- | python  
# RUN pip install supervisor  
#  
# ADD supervisord.conf /etc/supervisord.conf  
# add hadoop startup  
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
# add zookeeper startup  
ADD start-zk-bmx.sh /usr/bin/start-zk.sh  
  
# add zookeeper fencing  
ADD fence.sh /etc/fence.sh  
RUN chown root:root /etc/fence.sh && chmod a+x /etc/fence.sh  
  
ENV BOOTSTRAP /etc/bootstrap.sh  
  
# workingaround docker.io build error  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
  
# fix the 254 error code  
#RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
#RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
#RUN echo "Port 2122" >> /etc/ssh/sshd_config  
# Prep SSH - root password in reference to wurstmeister  
RUN mkdir /var/run/sshd && \  
echo 'root:wurstmeister' | chpasswd && \  
sed -i 's/#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config && \  
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa && \  
cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
# Check ssh access  
RUN /usr/sbin/sshd && ssh root@localhost ls -l  
  
# install sidecar  
ADD addtoresolv /sbin/addtoresolv  
ADD a8sidecar /usr/bin/a8sidecar  
  
# Hdfs ports  
EXPOSE 50010 50020 50070 50075 50090 8020 9000  
# Hdfs journal  
EXPOSE 8485  
# Mapred ports  
EXPOSE 10020 19888  
#Yarn ports  
EXPOSE 8030 8031 8032 8033 8040 8042 8088  
#zookeeper ports  
EXPOSE 2181 2888 3888  
#Flink ports  
EXPOSE 6123 8081  
#OTHER PORTS  
EXPOSE 49707 22 2122  
#CMD /usr/sbin/sshd && /bin/bash /usr/bin/start-zk.sh && cd /usr/local/hadoop
&& /bin/bash  
# Microservice description for advertisement by amalgam8 sidecar  
ENV A8_SERVICE=zookeeper:flink  
ENV A8_ENDPOINT_PORT=2181  
ENV A8_ENDPOINT_TYPE=tcp  
ENV A8_REGISTRY_URL=http://flink-a8-registry.eu-gb.mybluemix.net  
#ENV A8_REGISTRY_POLL=60s # default is 0secs  
ENV A8_CONTROLLER_URL=http://flink-a8-controller.eu-gb.mybluemix.net  
ENV A8_CONTROLLER_POLL=60s  
ENV A8_LOG=true  
  
ENTRYPOINT ["/usr/bin/a8sidecar", "--register", "--dns", "--dns_domain",
"local", "--dns_port", "53"]  
#default service, should be started with zookeeper1,2,3  
CMD ["--service test"]  
  

