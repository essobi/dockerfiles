FROM quay.io/falkonry/openjdk:8-jdk-alpine-zulu  
  
RUN apk update && \  
apk add --no-cache curl tar net-tools gnupg bash perl && \  
mkdir /opt && \  
rm -rf /var/cache/apk/* /tmp/*  
  
ENV HADOOP_VERSION=2.6.0  
ENV
HADOOP_URL=https://archive.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$HADOOP_URL" -o /tmp/hadoop.tar.gz \  
&& tar -xvf /tmp/hadoop.tar.gz -C /opt/ \  
&& rm /tmp/hadoop.tar.gz*  
  
RUN ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop  
RUN cp /etc/hadoop/mapred-site.xml.template /etc/hadoop/mapred-site.xml && \  
mkdir /opt/hadoop-$HADOOP_VERSION/logs && \  
mkdir /hadoop-data  
  
ENV HADOOP_PREFIX=/opt/hadoop-$HADOOP_VERSION \  
HADOOP_CONF_DIR=/etc/hadoop \  
MULTIHOMED_NETWORK=1  
ENV USER=root \  
PATH=$HADOOP_PREFIX/bin/:$PATH  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

