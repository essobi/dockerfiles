FROM ubuntu:14.04  
MAINTAINER Meng Ding <dingmeng@gmail.com>  
  
USER root  
  
# Install all dependencies  
RUN apt-get update && apt-get install -y \  
curl \  
openjdk-7-jdk \  
rsync \  
ssh \  
wget  
  
ENV HADOOP_PREFIX /opt/hadoop  
ENV HADOOP_CONF_DIR ${HADOOP_PREFIX}/etc/hadoop  
ENV HADOOP_DATA_DIR /var/lib/hadoop  
ENV PATH ${HADOOP_PREFIX}/bin:$PATH  
ENV HADOOP_VERSION 3.0.0-SNAPSHOT  
  
# Download hadoop  
RUN curl -SL https://s3.amazonaws.com/hadoop-
distribution/hadoop-${HADOOP_VERSION}.tar.gz \  
| tar xz -C /opt  
  
# Install hadoop  
RUN ln -s /opt/hadoop-${HADOOP_VERSION} ${HADOOP_PREFIX} \  
&& mkdir /var/lib/hadoop && mkdir /var/lib/hadoop/namenode \  
&& mkdir /var/lib/hadoop/datanode  
  
# Format hdfs  
COPY add/config/hadoop/* ${HADOOP_CONF_DIR}/  
RUN ${HADOOP_PREFIX}/bin/hdfs namenode -format  
  
# Copy data and configuration to be used by container initialization  
RUN tar cf /tmp/hadoop-data.tar -C ${HADOOP_DATA_DIR} . \  
&& tar cf /tmp/hadoop-config.tar -C ${HADOOP_CONF_DIR} .  
  
ENV ZK_PREFIX /opt/zookeeper  
ENV ZK_CONF_DIR $ZK_PREFIX/conf  
ENV ZK_VERSION 3.4.6  
ENV PATH ${ZK_PREFIX}/bin:$PATH  
  
# Download zookeeper  
RUN curl -SL
http://apache.mirror.rafal.ca/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz
\  
| tar xz -C /opt  
  
# Install zookeeper  
RUN ln -s /opt/zookeeper-${ZK_VERSION} ${ZK_PREFIX} \  
&& mkdir /var/lib/zookeeper  
COPY add/config/zookeeper/* ${ZK_CONF_DIR}/  
  
ENV SLIDER_PREFIX /opt/slider  
ENV SLIDER_CONF_DIR $SLIDER_PREFIX/conf  
ENV SLIDER_VERSION 0.90.0-incubating-SNAPSHOT  
ENV PATH ${SLIDER_PREFIX}/bin:$PATH  
# Download slider  
RUN curl -SL https://s3.amazonaws.com/hadoop-
distribution/slider-${SLIDER_VERSION}-all.tar.gz \  
| tar xz -C /opt  
# Install slider  
RUN ln -s /opt/slider-${SLIDER_VERSION} ${SLIDER_PREFIX} \  
&& mkdir -p /opt/app_packages  
# Copy the sample application packages  
COPY add/config/slider/app_packages /opt/app_packages/  
  
# Set JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
# Create user  
RUN groupadd -r vagrant -g 1000 && useradd -r -g vagrant -u 1000 vagrant  
  
# Run  
COPY bootstrap.sh /  
ENTRYPOINT ["/bootstrap.sh"]  
  

